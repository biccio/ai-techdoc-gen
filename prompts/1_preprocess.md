#### File: `prompts/1_preprocess.md`

```markdown
Analizza il seguente file sorgente (`{filename}`).

--- CONTENUTO DEL FILE ---
{content}
--- FINE CONTENUTO ---

Estrai le seguenti informazioni in un oggetto JSON. A seconda del tipo di file, adatta la tua analisi:

-   **Se è un file di specifica (YAML/YML/OpenAPI)**:
    -   `purpose`: (string) Una singola frase concisa che descrive lo scopo principale dell'API.
    -   `key_entities`: (array di stringhe) Un elenco dei 3-5 endpoint più importanti (es. 'POST /activations').
    -   `target_audience`: (string) 'Backend Developer'.
    -   `technologies`: (array di stringhe) Un elenco di tecnologie chiave (es. 'REST', 'OAuth2', 'JSON').

-   **Se è un file di testo (MD, ecc.)**:
    -   `purpose`: (string) Lo scopo principale di questo file in una singola frase concisa.
    -   `key_entities`: (array di stringhe) Un elenco delle 5-7 entità più importanti descritte (es. concetti chiave, flussi utente, nomi di API, messaggi ISO).
    -   `target_audience`: (string) Il pubblico principale di destinazione (es. 'Developer', 'Software Architect', 'Technical Project Manager').
    -   `technologies`: (array di stringhe) Un elenco delle tecnologie o degli standard menzionati (es. 'SRTP', 'pain.013').

Rispondi solo con l'oggetto JSON.