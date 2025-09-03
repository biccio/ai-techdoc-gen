import os
import yaml
import json
import re
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from dotenv import load_dotenv
from pathlib import Path

# Carica le variabili d'ambiente da un file .env
load_dotenv()

class AIEngine:
    """
    Gestisce le interazioni con l'API di Gemini 1.5 Pro, utilizzando prompt
    esterni e un flusso di lavoro ottimizzato.
    """
    def __init__(self, diataxis_manual, pagopa_mapping, gold_standard_example, prompts_dir="prompts"):
        self.console = Console()
        self.prompts = self._load_prompts(prompts_dir)
        self.section_rules = self._parse_pagopa_mapping(pagopa_mapping)

        # Prepara il contesto base per tutti i prompt
        self.base_context = {
            "diataxis_manual": diataxis_manual,
            "pagopa_mapping": pagopa_mapping,
            "gold_standard_example": gold_standard_example,
        }

        try:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key or api_key == "YOUR_API_KEY_HERE":
                raise ValueError("GEMINI_API_KEY non è impostata nel tuo file .env.")
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(
                'gemini-2.5-pro',
                generation_config={"response_mime_type": "application/json"}
            )
        except Exception as e:
            self.console.print(f"[bold red]Errore nella configurazione di Gemini: {e}[/bold red]")
            exit()

    def _load_prompts(self, prompts_dir):
        """Carica tutti i template dei prompt dalla directory specificata."""
        prompts = {}
        prompt_path = Path(prompts_dir)
        if not prompt_path.is_dir():
            raise FileNotFoundError(f"La directory dei prompt '{prompts_dir}' non è stata trovata.")
        for f in prompt_path.glob("*.md"):
            prompts[f.stem] = f.read_text(encoding='utf-8')
        self.console.print(f"[green]Caricati {len(prompts)} template di prompt.[/green]")
        return prompts

    def _parse_pagopa_mapping(self, mapping_text):
        """Estrae le regole specifiche per ogni sezione Diataxis."""
        sections = {}
        patterns = {
            'il-prodotto': r'Explanation → il-prodotto:(.*?)(?=Reference → guida-tecnica:)',
            'guida-tecnica': r'Reference → guida-tecnica:(.*?)(?=How-To → tutorial:)',
            'tutorial': r'How-To → tutorial:(.*?)(?=Tutorial → casi-duso:)',
            'casi-duso': r'Tutorial → casi-duso:(.*)'
        }
        for section_name, pattern in patterns.items():
            match = re.search(pattern, mapping_text, re.DOTALL | re.IGNORECASE)
            if match:
                sections[section_name] = match.group(1).strip()
        return sections

    def _make_api_call(self, prompt_template_name, context_vars):
        """
        Funzione centralizzata per le chiamate API a Gemini, che formatta
        il prompt e gestisce la risposta JSON.
        """
        try:
            system_prompt = self.prompts['system_prompt'].format(**self.base_context)
            user_prompt_template = self.prompts[prompt_template_name]
            user_prompt = user_prompt_template.format(**context_vars)

            response = self.model.generate_content([system_prompt, user_prompt])
            
            return json.loads(response.text)

        except json.JSONDecodeError:
            self.console.print("[bold red]Errore API: Gemini non ha restituito un JSON valido.[/bold red]")
            self.console.print(f"Risposta ricevuta:\n{response.text}")
            return None
        except KeyError as e:
            self.console.print(f"[bold red]Errore: Template del prompt '{e}' non trovato.[/bold red]")
            return None
        except Exception as e:
            self.console.print(f"[bold red]Si è verificato un errore API inaspettato: {e}[/bold red]")
            return None

    def preprocess_sources(self, source_files_content):
        """Esegue una pre-analisi contestuale su ogni file sorgente."""
        self.console.print("\n[bold yellow]Step 1: Pre-elaborazione intelligente dei file sorgente...[/bold yellow]")
        preprocessed_summaries = {}
        for filename, content in source_files_content.items():
            self.console.print(f"  - Analisi di [cyan]{filename}[/cyan]...")
            
            context = {
                "filename": filename,
                "content": content[:8000] # Limita il contenuto per efficienza
            }
            summary = self._make_api_call('1_preprocess', context)
            if summary:
                preprocessed_summaries[filename] = summary
        
        self.console.print("[green]Pre-elaborazione completata.[/green]")
        return preprocessed_summaries

    def generate_index(self, preprocessed_summaries, product_name, product_version):
        """Genera un indice accurato utilizzando i riassunti pre-elaborati."""
        self.console.print("\n[bold yellow]Step 2: Generazione della bozza di indice...[/bold yellow]")
        context = {
            "product_name": product_name,
            "product_version": product_version,
            "summaries": json.dumps(preprocessed_summaries, indent=2)
        }
        index = self._make_api_call('2_generate_index', context)
        return index if index else {}

    def refine_index(self, current_index, user_feedback):
        """Affina l'indice in base al feedback dell'utente."""
        self.console.print("[yellow]Invio del tuo feedback a Gemini per affinare l'indice...[/yellow]")
        context = {
            "current_index": json.dumps(current_index, indent=2),
            "user_feedback": user_feedback
        }
        new_index = self._make_api_call('3_refine_index', context)
        return new_index if new_index else current_index

    def generate_final_content(self, approved_index, preprocessed_summaries, sections_to_generate):
        """Genera il contenuto markdown finale con un singolo prompt ottimizzato."""
        self.console.print("\n[bold green]Step 4: Generazione del contenuto finale...[/bold green]")
        generated_files = {}

        for section in sections_to_generate:
            if section not in approved_index or not approved_index.get(section):
                continue

            pages_in_section = approved_index[section]
            self.console.print(f"\n[bold]Generazione della sezione [blue]{section}[/blue]...[/bold]")
            
            context = {
                "section": section,
                "pages_in_section": json.dumps(pages_in_section, indent=2),
                "summaries": json.dumps(preprocessed_summaries, indent=2),
                "section_rules": self.section_rules.get(section, "Nessuna regola specifica definita.")
            }
            
            final_content = self._make_api_call('4_generate_content', context)
            
            if not final_content:
                self.console.print(f"[red]Generazione fallita per la sezione {section}. Salto.[/red]")
                continue

            for file_name, content in final_content.items():
                file_path = f"{section}/{file_name}"
                generated_files[file_path] = content
                self.console.print(f"    - [green]Contenuto finalizzato per [cyan]{file_path}[/cyan].[/green]")

        return generated_files

class ConfigLoader:
    """Carica e valida il file di configurazione del progetto."""
    def __init__(self, config_path):
        config_file = Path(config_path)
        if not config_file.is_file():
            raise FileNotFoundError(f"File di configurazione non trovato in '{config_path}'")
        with config_file.open('r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        self.validate()

    def validate(self):
        """Verifica la presenza delle chiavi di configurazione necessarie."""
        required_keys = ['product_name', 'version', 'output_path', 'source_dir', 'local_output_dir']
        if not all(key in self.config for key in required_keys):
            raise ValueError("Il file di configurazione manca di chiavi obbligatorie.")

    def get_config(self):
        return self.config

class InteractiveReviewerCLI:
    """Gestisce l'interfaccia utente a riga di comando per la revisione dell'indice."""
    def __init__(self):
        self.console = Console()

    def display_index(self, index, product_name, version):
        """Mostra l'indice proposto in un pannello formattato."""
        panel_content = f"[bold]Prodotto:[/bold] {product_name} v{version}\n\n"
        if not index:
            panel_content += "[bold red]Indice non disponibile. Controlla gli errori API.[/bold red]"
        else:
            for section, pages in index.items():
                panel_content += f"[bold blue]{section}/[/bold blue]\n"
                if not pages:
                    panel_content += "  [italic]Nessun file in questa sezione.[/italic]\n"
                    continue
                for page in pages:
                    file = page.get('file', 'N/A')
                    desc = page.get('description', 'N/A')
                    sources = ", ".join(page.get('source_files', []))
                    panel_content += f"  - [cyan]{file}[/cyan]\n    [italic]Desc: {desc}[/italic]\n    [dim]Sorgenti: {sources}[/dim]\n"
        
        self.console.print(Panel(panel_content, title="Indice Proposto", border_style="green", expand=False))

    def start_review_cycle(self, initial_index, ai_engine, product_name, version):
        """Avvia il ciclo interattivo per la revisione e la selezione delle sezioni."""
        current_index = initial_index
        while True:
            self.display_index(current_index, product_name, version)
            
            if not current_index:
                self.console.print("[bold red]Impossibile procedere senza un indice valido. Uscita.[/bold red]")
                exit()

            prompt_text = "\nInserisci le modifiche o digita [bold green]'!generate'[/bold green] per approvare e continuare:"
            user_input = Prompt.ask(prompt_text)

            if user_input.strip().lower() == '!generate':
                self.console.print("\n[bold green]Indice approvato![/bold green]")
                
                available_sections = [s for s in current_index.keys() if current_index.get(s)]
                
                while True:
                    self.console.print("\nSezioni disponibili per la generazione:", ", ".join(f"[bold blue]{s}[/bold blue]" for s in available_sections))
                    sections_prompt = "Quali sezioni vuoi generare? (digita '[bold cyan]all[/bold cyan]' o una lista separata da virgole, es. 'il-prodotto,guida-tecnica'):"
                    
                    chosen_input = Prompt.ask(sections_prompt).strip().lower()
                    
                    if chosen_input == 'all':
                        return current_index, available_sections
                    
                    chosen_sections = [s.strip() for s in chosen_input.split(',') if s.strip()]
                    valid_sections = [s for s in chosen_sections if s in available_sections]
                    invalid_sections = [s for s in chosen_sections if s not in available_sections]
                    
                    if invalid_sections:
                        self.console.print(f"[bold red]Errore: Le seguenti sezioni non sono valide o sono vuote: {', '.join(invalid_sections)}[/bold red]")
                    elif not valid_sections:
                        self.console.print("[bold red]Errore: Nessuna sezione valida selezionata.[/bold red]")
                    else:
                        return current_index, valid_sections
            else:
                current_index = ai_engine.refine_index(current_index, user_input)

class LocalPublisher:
    """Gestisce il salvataggio dei file generati in locale."""
    def __init__(self, local_output_path):
        self.local_output_path = Path(local_output_path)
        self.console = Console()
    
    def publish(self, generated_files):
        """Salva i file generati nel percorso di output locale."""
        self.console.print(f"\n[bold yellow]Step 5: Salvataggio dei file...[/bold yellow]")
        self.console.print(f"  - Percorso di output: [underline]{self.local_output_path}[/underline]")
        
        if not generated_files:
            self.console.print("[yellow]Nessun file da salvare.[/yellow]")
            return

        for file_path, content in generated_files.items():
            full_path = self.local_output_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding='utf-8')

        self.console.print(f"[green]I file sono stati salvati in '{self.local_output_path}' ✅[/green]")

class CoreController:
    """Orchestra l'intero processo di generazione della documentazione."""
    def __init__(self, config_path, knowledge_files, prompts_dir="prompts"):
        self.console = Console()
        self.config_loader = ConfigLoader(config_path)
        self.config = self.config_loader.get_config()

        try:
            diataxis_manual = Path(knowledge_files['diataxis_manual']).read_text(encoding='utf-8')
            pagopa_mapping = Path(knowledge_files['pagopa_mapping']).read_text(encoding='utf-8')
            gold_standard_content = Path(knowledge_files['gold_standard']).read_text(encoding='utf-8')
        except FileNotFoundError as e:
            self.console.print(f"[bold red]Errore: File di conoscenza o prompt non trovato: {e.filename}.[/bold red]")
            exit()
        except KeyError as e:
            self.console.print(f"[bold red]Errore: Chiave del file di conoscenza mancante: {e}.[/bold red]")
            exit()

        self.ai_engine = AIEngine(diataxis_manual, pagopa_mapping, gold_standard_content, prompts_dir)
        self.cli = InteractiveReviewerCLI()
        self.publisher = LocalPublisher(self.config['local_output_dir'])

    def read_source_files(self):
        """Legge tutti i file sorgente dalla directory specificata."""
        source_dir = Path(self.config['source_dir'])
        source_files_content = {}
        if not source_dir.is_dir():
            self.console.print(f"[bold red]Errore: La directory sorgente '{source_dir}' non è stata trovata.[/bold red]")
            return {}
        
        for file_path in source_dir.rglob('*'):
            if file_path.is_file() and file_path.name != '.DS_Store':
                relative_path = file_path.relative_to(source_dir)
                try:
                    source_files_content[str(relative_path)] = file_path.read_text(encoding='utf-8')
                except Exception as e:
                    self.console.print(f"[bold red]Errore nella lettura del file '{relative_path}': {e}[/bold red]")
        return source_files_content

    def run(self):
        """Esegue il flusso di lavoro completo per la generazione della documentazione."""
        self.console.print(Panel(f"[bold]Avvio del Generatore di Documentazione per {self.config['product_name']}[/bold]", border_style="magenta"))

        source_files = self.read_source_files()
        if not source_files:
            self.console.print("[bold yellow]Nessun file sorgente trovato. Processo interrotto.[/bold yellow]")
            return
        self.console.print(f"Letti {len(source_files)} file sorgente.")

        preprocessed_summaries = self.ai_engine.preprocess_sources(source_files)
        if not preprocessed_summaries:
            self.console.print("[bold red]Pre-elaborazione fallita. Processo interrotto.[/bold red]")
            return

        initial_index = self.ai_engine.generate_index(
            preprocessed_summaries, self.config['product_name'], self.config['version']
        )

        self.console.print("\n[bold yellow]Step 3: Revisione interattiva dell'indice...[/bold yellow]")
        approved_index, sections_to_generate = self.cli.start_review_cycle(
            initial_index, self.ai_engine, self.config['product_name'], self.config['version']
        )

        final_content = self.ai_engine.generate_final_content(
            approved_index, preprocessed_summaries, sections_to_generate
        )

        self.publisher.publish(final_content)
        
        self.console.print("\n[bold]Processo completato.[/bold]")

if __name__ == "__main__":
    # Assicura che le directory di esempio e un config di base esistano
    if not os.path.exists("example_project/source_docs"):
        os.makedirs("example_project/source_docs")
    if not os.path.exists("generated_docs"):
        os.makedirs("generated_docs")
    if not os.path.exists("example_project/config.yaml"):
        with open("example_project/config.yaml", "w", encoding='utf-8') as f:
            yaml.dump({
                "product_name": "PagoPA Prodotto Esempio",
                "version": "1.0.0",
                "output_path": "docs/v1.0",
                "source_dir": "example_project/source_docs",
                "local_output_dir": "generated_docs"
            }, f, default_flow_style=False, allow_unicode=True)
            print("Creato file di configurazione di esempio: 'example_project/config.yaml'")

    # Definisce i percorsi per i file di conoscenza e prompt
    KNOWLEDGE_FILES = {
        "diataxis_manual": "diataxis_manuale.md",
        "pagopa_mapping": "mappatura_diataxis_pagopa.md",
        "gold_standard": "prompts/gold_standard.md"
    }

    controller = CoreController(
        config_path="example_project/config.yaml",
        knowledge_files=KNOWLEDGE_FILES
    )
    controller.run()