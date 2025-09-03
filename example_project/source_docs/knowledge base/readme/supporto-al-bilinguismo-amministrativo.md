# Supporto al bilinguismo amministrativo

Le amministrazioni pubbliche tenute a redigere gli atti in doppia lingua per garantire il bilinguismo amministrativo perfetto possono utilizzare questa funzionalità di SEND, che permette di ottenere notifiche, comunicazioni e atti opponibili a terzi in due lingue. Il mittente deve garantire la doppia lingua nei campi descrittivi delle notifiche, nei documenti e negli atti allegati.

### Lingue per il Bilinguismo Amministrativo

Questa funzionalità supporta le lingue **tedesco**, **francese** e **sloveno**, in linea con le specifiche necessità locali. Per attivare il bilinguismo, è necessario valorizzare il campo _`additionalLanguages`_ nella API di creazione della notifica con uno dei seguenti valori:&#x20;

* DE (tedesco)
* FR (francese)
* SL (sloveno)&#x20;

E' possibile indicare una sola lingua aggiuntiva per volta. In assenza di lingue aggiuntive, la lingua di default per la generazione dei documenti, degli atti opponibili a terzi, ecc. sarà l'italiano.

### Documenti Oggetto di Traduzione

I documenti che devono essere tradotti includono:

* **Avviso di Avvenuta Ricezione (AAR)**
* **Attestazioni Opponibili a Terzi**
* **Avvisi inviati tramite PEC e email di avvenuta ricezione**

Ogni notifica bilingue dovrà includere **l’AAR** e tutte le attestazioni opponibili a terzi della notifica.&#x20;

### Responsabilità per le Traduzioni

Le traduzioni dei campi oggetto (subject) e descrizione (abstract), degli atti allegati e di altri documenti, sono di responsabilità dell’ente mittente.

### Traduzioni di Comunicazioni

Le comunicazioni di avvenuta ricezione di PEC e e-mail sono forniti in doppia lingua come impostato sul parametro _`additionalLanguages`_.

I messaggi SMS a causa delle limitazioni di spazio non sono tradotti.
