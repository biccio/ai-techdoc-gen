---
description: >-
  Descrizione step-by-step per l'inserimento e la creazione dello stream
  utilizzando Postman
---

# Inserimento e creazione stream con Postman

**NOTA:** prima di procedere con l'inserimento e la creazione dello stream utilizzando Postman, assicurarsi di aver correttamente importato le definizioni delle API su Postman ed aver configurato l'ambiente di test seguendo i passaggi descritti al seguente link:

{% content-ref url="../generazione-client-e-definizioni-delle-api.md" %}
[generazione-client-e-definizioni-delle-api.md](../generazione-client-e-definizioni-delle-api.md)
{% endcontent-ref %}

### 1) Creazione e configurazione dello stream

Creare lo stream andando a configurare l'**eventType** con uno dei seguenti:

* **STATUS:** per registrare gli eventi di cambiamento di stato delle notifiche
* **TIMELINE:** per registrare gli eventi di timeline.

Nel campo **groups** dovranno essere inseriti uno o più gruppi tramite il l'id del gruppo, in modo da realizzare una segregazione tra gli eventi delle notifiche che appartengono solo ai gruppi specificati.

All'interno del **filterValues** è possibile inserire un array di eventi di tipo **STATUS/TIMELINE** che verranno utilizzati per filtrare e registrare nello stream solo questi eventi; se invece si inserisce un array con il valore `DEFAULT`, vanno riportati gli eventi che hanno ripercussione sul cambiamento di stato del workflow o che riportano dati di interesse per il mittente. Qui è possibile vedere quali eventi verranno restituiti: [Stream di timeline 2.4](stream-di-timeline/).

\
Aprire la scheda **Crea nuovo stream di eventi** ed inserire nel body il seguente payload:

<figure><img src="../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

**-NOTA:** sostituire i seguenti:

* **\<baseurlAmbiente>:** inserire la url dell'ambiente di riferimento, nel caso di UAT è il seguente: **https://api.uat.notifichedigitali.it**
* **\<apiKey>:** inserire la apiKey dell'Ente di riferimento, precedentemente generata su PND
* **\<PDNDVoucher>:** inserire inserire il Voucher generato su **PDND Interoperabilità,** assicurandosi che non sia scaduto
* **\<title>:** inserire un titolo da attribuire a questo stream
* **\<groupId>:** Id del gruppo per ottenere la segregazione tra gli eventi delle notifiche che appartengono solo ai gruppi specificati
* **\<eventType>:** inserire la tipologia di stream a scelta tra **STATUS** e **TIMELINE**&#x20;
* **\<filterValues>:** inserire un array di eventi che verranno utilizzati come filtro. Se valorizzato con array vuoto: `DEFAULT` lo stream registrerà tutti gli eventi eventi che hanno ripercussione sul cambiamento di stato del workflow o che riportano dati di interesse per il mittente
* **\<replacedStreamId>:** campo opzionale, serve per sostituire lo stream indicato tramite streamId da quello che verrà creato.

Nella response di questo servizio, si otterrà il seguente payload:\


<figure><img src="../../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

* **\<streamId>:** id dello stream che viene autogenerato dal servizio
* **\<activationDate>:** data di attivazione dello stream autogenerata dal servizio

**NOTA:** Una volta creata la stream verranno registrati tutti gli eventi emessi dalle notifiche a seguito della loro creazione, di conseguenza si consiglia di creare le stream prima di inserire le notifiche.

### 2) Prima interrogazione dello stream

La prima interrogazione dello stream permetterà di ricevere i primi 50 eventi registrati dallo stream. \
Aprire la scheda **Leggi progressi notifiche** e riprodurre questa configurazione:

<figure><img src="../../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

**NOTA:** sostituire i seguenti:

* **\<baseurl>:** inserire la url dell'ambiente di riferimento, nel caso di UAT è il seguente: **https://api.uat.notifichedigitali.it**
* **\<streamId>:** inserire l'id dello stream che si vuole interrogare

Nella response di questo servizio, si otterrà il seguente payload che rappresenta tutti gli eventi:

<figure><img src="../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

Gli eventi ottenuti dovranno essere memorizzati dal client poichè nelle successive chiamate i risultati ottenuti verranno consumati e cancellati dallo stream per lasciare il posto agli eventi successivi. \
E' poi necessario selezionare il tab Headers della response per visualizzare i valori ottenuti:

<figure><img src="../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

**NOTA:** nell'header della response ottenuta fare attenzione al campo `retry-after` che deve essere memorizzato per le successive chiamate:

* se`retryAfter = 0` è possibile richiamare immediatamente il servizio per ottenere gli eventi successivi se invece
* se`retryAfter` ≠ `0` è necessario attendere la quantità di tempo (espressa in millisecondi) del valore restituito, prima di richiamare di nuovo il servizio

E' quindi fondamentale rispettare la logica che viene rappresentata dal campo "_retry-after_" il quale fornisce l'indicazione al client su quando richiamare il servizio; pertanto si sconsiglia di creare dei processi di batch che effettuino la chiamata in un momento fisso e/o ripetuto nei giorni.

### 3) Interrogazione dello stream successive alla prima

Dalle interrogazioni successive alla prima dello stream, si otterranno i 50 eventi successivi a quello del lastEventId (l'eventId dell'ultimo evento ottenuto nelle precedenti chiamate).\
Aprire la scheda **Leggi progressi notifiche** e riprodurre questa configurazione:

<figure><img src="../../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

**NOTA:** sostituire i seguenti:

* **\<baseurlAmbiente>:** inserire la url dell'ambiente di riferimento, nel caso di UAT è il seguente: **https://api.uat.notifichedigitali.it**
* **\<streamId>:** inserire l'id dello stream che si vuole interrogare
* **\<lastEventId>:** inserire l'eventId dell'ultimo evento ottenuto nella precedente chiamata

Gli eventi ottenuti dovranno essere memorizzati dal client poichè nelle successive chiamate i risultati ottenuti verranno consumati e cancellati dallo stream per lasciare il posto agli eventi successivi.

**NOTA:** nella response ottenuta fare attenzione al campo "_retry-after_" che deve essere memorizzato per le successive chiamate:

* se`retryAfter = 0` è possibile richiamare immediatamente il servizio per ottenere gli eventi successivi se invece
* se`retryAfter` ≠ `0` è necessario attendere la quantità di tempo (espressa in millisecondi) del valore restituito, prima di richiamare di nuovo il servizio

E' quindi fondamentale rispettare la logica che viene rappresentata dal campo  "_retry-after_" il quale fornisce l'indicazione al client su quando richiamare il servizio; pertanto si sconsiglia di creare dei processi di batch che effettuino la chiamata in un momento fisso e/o ripetuto nei giorni.
