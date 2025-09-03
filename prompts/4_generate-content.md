Il tuo compito è generare il contenuto Markdown finale per le pagine della sezione '{section}'.

**PAGINE DA GENERARE:**
{pages_in_section}

**RIASSUNTI DEI FILE SORGENTE DISPONIBILI:**
{summaries}

**REGOLE SPECIFICHE PER QUESTA SEZIONE ('{section}'):**
{section_rules}

**ISTRUZIONI OBBLIGATORIE:**
1.  **Aderenza Totale**: Segui scrupolosamente le regole specifiche della sezione e i principi generali della mappatura PagoPA. Il pubblico è composto da sviluppatori esperti; vai dritto al punto.
2.  **Qualità Gold Standard**: Il risultato finale deve essere impeccabile e della stessa qualità dell'esempio "gold standard".
3.  **YAML Frontmatter Completo**: All'inizio di OGNI file, includi un blocco YAML Frontmatter completo e pertinente, ricco di metadati schema.org come mostrato nell'esempio.
4.  **Diagrammi Mermaid**: Se il contenuto descrive un flusso, un processo o una sequenza (specialmente nei `tutorial` e `casi-duso`), DEVI includere un diagramma di sequenza `mermaid` per illustrarlo.
5.  **Contenuto**: Scrivi il corpo del documento in Markdown, seguendo le migliori pratiche di technical writing. Sii chiaro, conciso e preciso. Includi link slug-based alle sezioni pertinenti della `guida-tecnica` dove necessario.

**FORMATO DI OUTPUT:**
Restituisci un singolo oggetto JSON dove le chiavi sono i nomi dei file da generare (es. `panoramica.md`) e i valori sono il contenuto Markdown COMPLETO (inclusivo di Frontmatter). Non aggiungere commenti o testo al di fuori dell'oggetto JSON.