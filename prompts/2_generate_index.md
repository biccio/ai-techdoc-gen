Basandoti sui seguenti riassunti strutturati per il prodotto '{product_name}' v'{product_version}':

--- RIASSUNTI ---
{summaries}
--- FINE RIASSUNTI ---

Crea una bozza di indice seguendo la MAPPATURA SPECIFICA PAGOPA. Assegna ogni documento sorgente alla categoria Diataxis più appropriata (il-prodotto, guida-tecnica, tutorial, casi-duso).

Restituisci l'indice come un oggetto JSON. Le chiavi devono essere i nomi delle sezioni Diataxis mappate. I valori devono essere liste di oggetti, dove ogni oggetto contiene:
-   `file`: (string) il nome del file originale da generare (es. `panoramica-del-prodotto.md`).
-   `description`: (string) una nuova descrizione informativa che hai generato.
-   `source_files`: (array di stringhe) un elenco dei file sorgente originali usati per creare questo nuovo file.

Esempio di formato di output:
```json
{{
  "il-prodotto": [
    {{
      "file": "panoramica.md",
      "description": "Descrive gli obiettivi, il contesto normativo e il funzionamento generale del prodotto.",
      "source_files": ["source1.md", "source2.md"]
    }}
  ],
  "guida-tecnica": [
     {{
      "file": "api-reference.md",
      "description": "Specifica tecnica completa degli endpoint API, inclusi parametri e risposte.",
      "source_files": ["openapi.yaml"]
    }}
  ]
}}