---
description: Approfondimento sul perfezionamento della notifica su SEND
---

# Perfezionamento della notifica

### Perfezionamento per il Mittente della notifica&#x20;

A seguito dell'inserimento di una richiesta di notifica da parte del Mittente, la Piattaforma effettua dei controlli sui dati inseriti, sia in modalità sincrona che asincrona. Superati di tali controlli, verrà generato un codice **IUN** (Identificativo Univoco della Notifica), in questo momento scatta il Perfezionamento per il Mittente e viene generata l'**Attestazione opponibile a terzi: notifica presa in carico.**\


### Perfezionamento per il Destinatario della notifica

In presenza di almeno un domicilio digitale del Destinatario, la Piattaforma avvierà il **Workflow digitale;** in assenza di domicilio digitale invece avvierà il **Workflow analogico.**

Quando un destinatario accede alla notifica, scatena l'evento **NOTIFICATION\_VIEWED** che rappresenta unicamente la presa visione della notifica da parte del singolo destinatario. \
Se la Presa Visione si verifica prima dell'evento **EFFECTIVE\_DATE**, si scatena il Perfezionamento per presa visione per il solo Destinatario che visualizza la notifica.&#x20;

Nei casi di multi-destinatario il Perfezionamento avviene in modo indipendente per ogni destinatario della notifica; nel caso in cui uno dei destinatari visualizzasse la notifica, questa passerebbe in status **VIEWED** tuttavia questa condizione non influisce sul Perfezionamento degli altri destinatari della notifica.

### Perfezionamento per il Destinatario della notifica - Workflow digitale

Il perfezionamento della notifica per il destinatario nel workflow digitale avviene nelle seguenti modalità ed in modo indipendente per ogni destinatario:

* In caso di **esito positivo** di consegna: la notifica si perfeziona per il singolo destinatario dopo 7 giorni dalla consegna dell’AAR attraverso PEC o SERCQ con l'evento **REFINEMENT** ed il passaggio allo stato **EFFECTIVE\_DATE.**\
  Nota: nel caso la consegna avvenga dopo le ore 21:00 il perfezionamento avviene dopo 8 giorni
* In caso di **esito negativo** di consegna: la notifica si perfeziona per il singolo destinatario dopo 15 giorni dalla generazione dell’AMR, che avviene in seguito al fallimento della consegna digitale, con l'evento **REFINEMENT** ed il passaggio allo stato **EFFECTIVE\_DATE.**

### Perfezionamento per il Destinatario della notifica - Workflow analogico

Il perfezionamento della notifica per il destinatario nel workflow analogico avviene nelle seguenti modalità ed in modo indipendente per ogni destinatario:

* **In caso di consegna**: la notifica si perfeziona per il singolo destinatario dopo 10 giorni dalla consegna dell’AAR in modalità cartacea, con l'evento **REFINEMENT** ed il passaggio allo stato **EFFECTIVE\_DATE.**
* **In caso di mancata consegna:** la notifica si perfeziona per il singolo destinatario dopo 10 giorni dalla mancata consegna dell’AAR in modalità cartacea, con l'evento **REFINEMENT** ed il passaggio allo stato **EFFECTIVE\_DATE.**

### Perfezionamento della notifica nei casi di multi-destinatario

Nei casi di notifica con multi-destinatario, il Perfezionamento avviene in modo indipendente per ogni destinatario, seguendo le modalità descritte in precedenza.&#x20;

Si evidenzia che il Perfezionamento è una condizione del singolo destinatario e non è applicabile alla notifica, per la quale Piattaforma esprime una descrizione sintetica di stato; se ad esempio la notifica si trova in stato **VIEWED** questo significa che almeno uno dei destinatari ne ha preso visione, ma non comporta in automatico nessun tipo di Perfezionamento, il quale dovrà essere definito attraverso l'analisi degli eventi di Timeline per ciascun destinatario.

### Sequenzialità degli eventi della Timeline

Il processo di notifica con canale analogico coinvolge il recapitista, il quale restituisce gli eventi a SEND nella sequenza temporale in cui questi avvengono effettivamente. Anche nei casi in cui questi eventi dovessero essere recepiti con ritardo dalla Piattaforma, è comunque garantita la sequenzialità e la coerenza degli eventi, senza alcuna regressione.

Se prendiamo ad esempio questa situazione:

1. **T1\[13/01/23]** Avvio della spedizione cartacea
2. **T2\[15/01/23]** L'addetto al recapito consegna la raccomandata, ma non fornisce alla piattaforma informazioni sull’avvenuta consegna. (evento **DELIVERED** non ancora acclarato)
3. **T3\[28/01/23]** Il destinatario accede a SEND e visualizza la notifica. In questa fase si scatena l’evento **NOTIFICATION\_VIEWED** e la notifica passa in stato **VIEWED**
4. **T4\[30/01/23]** Il recapitista comunica alla Piattaforma l’avvenuta consegna in data 15/01/23, il cui stato associato è **DELIVERED**

Gli eventi scatenati vengono **sempre** memorizzati nella sequenza in cui arrivano e sia gli stati che gli eventi di timeline si adeguano alle date di tali eventi; nell'esempio riportato, seppure l'evento **DELIVERED** venga acclarato in data 30/01/23, la notifica resta in stato **VIEWED** e **NON** viene riportata allo stato precedente **DELIVERED.**&#x20;

### Esempi di Perfezionamento:

1. **Notifica con singolo destinatario consegnata con successo in modalità digitale in data 01/01 e visualizzata dal destinatario in data 10/01.**\
   Sul destinatario si verifica il Perfezionamento per decorrenza termini dopo 7 giorni dalla consegna della notifica in modalità digitale, alla data del 08/01. La presa visione della notifica avvenuta in data 10/01 non comporta Perfezionamento, ma viene comunque registrato nella Timeline l'evento **NOTIFICATION\_VIEWED** e si genera l'**Attestazione opponibile a terzi: avvenuto accesso**.
2. **Notifica con singolo destinatario consegnata con successo in modalità analogica in data 01/01 e visualizzata dal destinatario in data 05/01.**\
   Sul destinatario si verifica il Perfezionamento per Presa Visione alla data del 05/01, con relativa registrazione dell'evento **NOTIFICATION\_VIEWED** nella Timeline e generazione delll'**Attestazione opponibile a terzi: avvenuto accesso;** infatti il destinatario prende visione della notifica prima che avvenga il Perfezionamento per decorrenza termini dopo 10 giorni dalla consegna dell’AAR in modalità cartacea.
3. **Notifica con singolo destinatario inviata in modalità analogica in data 01/01 ma tutti i tentativi di consegna falliscono.**\
   Sul destinatario si verifica il Perfezionamento per decorrenza termini alla data del 11/01 dopo 10 giorni dalla mancata consegna dell’AAR in modalità cartacea, con relativa registrazione dell'evento **REFINEMENT** nella Timeline.
4. **Notifica con 2 destinatari: il destinatario1 riceve con successo la notifica in modalità digitale in data 01/01 e la visualizza in data 02/01.** \
   **Il destinatario2 riceve con successo la notifica in modalità analogica in data 12/01 ma non la visualizza.**\
   Sul destinatario1 si verifica il Perfezionamento per Presa Visione alla data del 02/01, con relativa registrazione dell'evento **NOTIFICATION\_VIEWED** nella Timeline e generazione delll'**Attestazione opponibile a terzi: avvenuto accesso,** poiché questo prende visione della notifica prima che avvenga il Perfezionamento per decorrenza termini dopo 7 giorni dalla consegna dell’AAR in modalità digitale.\
   Sul destinatario2 si verifica il Perfezionamento per decorrenza termini dopo 10 giorni dalla consegna dell’AAR in modalità cartacea, alla data del 22/01 con relativa registrazione dell'evento **REFINEMENT** nella Timeline.\
   Dopo la data del 02/01 su Piattaforma Notifiche sarà possibile visualizzare la dicitura "Visualizzata" in corrispondenza di questa notifica, tuttavia questa informazione di stato sintetica non incide sul perfezionamento, il quale avviene in modo indipendente per ogni destinatario e nelle modalità espresse.
