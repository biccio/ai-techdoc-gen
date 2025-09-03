---
description: Descrizione step-by-step per l'inserimento della notifica utilizzando Postman
---

# Inserimento Notifica con Postman

**NOTA:** prima di procedere con l'inserimento Notifica con Postman, assicurarsi di aver correttamente importato le definizioni delle API su Postman ed aver configurato l'ambiente di test seguendo i passaggi descritti al seguente link:

{% content-ref url="../generazione-client-e-definizioni-delle-api.md" %}
[generazione-client-e-definizioni-delle-api.md](../generazione-client-e-definizioni-delle-api.md)
{% endcontent-ref %}

### 1) Generare il checksum sha256, codificato in base 64, del contenuto binario dei pdf di Notifica.pdf e di Pagamento.pdf che verranno caricati su PND

Entrare nella cartella che che contiene i file Notifica.pdf e Pagamento.pdf e lanciare i seguenti comandi utilizzando un terminal ssh (ad es. git bash):

* comando per generare lo sha256, codificato in base 64 per la Notifica:

```bash
cat Notifica.pdf | openssl dgst -binary -sha256 | openssl base64
```

* comando per generare lo sha256, codificato in base 64 per il Pagamento:

```bash
cat Pagamento.pdf | openssl dgst -binary -sha256 | openssl base64
```

L'output ottenuto per ogni file dovrà essere memorizzato per i futuri utilizzi\
**NOTA:** i file Notifica.pdf e Pagamento.pdf dovranno essere sostituiti con i file corrispondenti ai pdf che si vuole caricare su Piattaforma Notifiche

### &#x20;2) Eseguire l'operazione di pre-caricamento dei file

Aprire la scheda **richiesta di pre-caricamento allegati** ed inserire nel body il seguente payload:\


<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

**NOTA:** sostituire i seguenti:

* **\<shaDellaNotifica>:** è lo sha256 della Notifica che si ottiene come output al punto 1.1
* **\<shaDelPagamento>:** è lo sha256 del Pagamento che si ottiene come output al punto 1.2
* il valori **\<preloadIdx1>** e **\<preloadIdx2>** sono a discrezione del chiamante e servono per associare un indice alle richieste presenti nell'array di questa request

Nella response di questo servizio, si otterrà il seguente payload:

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

**NOTA:** i valori ottenuti nella response dovranno essere memorizzati per i futuri utilizzi; nello specifico:

* **\<preloadIdx1>** e **\<preloadIdx2>:** hanno il solo scopo di fare riferimento agli elementi mettendo in correlazione request/response
* **\<secret1>** e **\<secret2>:** andranno utilizzati nella chiamata di upload dei documenti
* **\<httpMethod1> e \<httpMethod2>:** corrispondono al http method da utilizzare nella chiamata di upload dei documenti
* **\<url1>** e **\<url2>:** sono le url da utilizzare nella chiamata di upload dei documenti
* **\<key2>** e **\<key2>:** sono le keys da utilizzare in fase di inserimento notifica, rispettivamente per i 2 file

### 3) Effettuare l'upload dei documenti&#x20;

Ora bisogna effettuare l'operazione di upload verso il _safeStorage_ per entrambi i documenti. Cliccando sulle url ottenute, si aprirà una scheda Postman già parzialmente configurata con l'url di interesse. Sarà ora necessario compilare gli headers nella sezione "Headers" inserendo i parametri ottenuti nella precedente chiamata:

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

Spostarsi poi nella sezione "Body" e selezionare il radio button "binary", selezionando il file che si vuole caricare:

<figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

**NOTA:** avendo 2 documenti, le chiamate da effettuare per effettuare l'upload sono 2, pertanto sarà necessario utilizzare i riferimenti **\<url1>, \<httpMethod1>** e **\<secret1>** nella chiamata di caricamento del primo file e **\<url2>, \<httpMethod2>** e **\<secret2>** nella chiamata di caricamento del secondo file. Per effettuare questa chiamata sarà necessario selezionare il "Desktop Agent" di Postman, dalla sezione dedicata in basso.

<figure><img src="../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

Dopo aver lanciato la richiesta per entrambi ed aver ottenuto esito positivo, bisogna memorizzare i valore di x-amz-version-id: **\<versionIdNotifica>** e **\<versionIdPagamento>** che si ottengono nella sezione "Header" della response, rispettivamente il primo nella response del primo upload ed il secondo nella response del secondo upload, che verranno utilizzati nella prossima chiamata:

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### 4) Effettuare l'inserimento della notifica

A questo punto è possibile effettuare l'inserimento della Notifica nella scheda **Richiesta invio notifica**, inserendo correttamente il body della request:

<figure><img src="../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

**NOTA:**

* **\<payloadDellaNotifica>:** corrisponde al json contenente tutti i dati della notifica; per inserire correttamente i riferimenti ai pdf caricati in precedenza, seguire le seguenti istruzioni:
  * Valorizzare i seguenti riferimenti al file Notifica.pdf\
    documents.digests.sha256: **\<shaDellaNotifica>**\
    documents.contentType: **"application/pdf"**\
    documents.ref.key: **\<key1>**\
    documents.ref.versionToken: **\<versionIdNotifica>**
  * Valorizzare i seguenti riferimenti al file Pagamento.pdf\
    recipients.payment.pagoPaForm.digests.sha256: **\<shaDelPagamento>**\
    recipients.payment.pagoPaForm.contentType: **"application/pdf"**\
    recipients.payment.pagoPaForm.ref.key: **\<key2>**\
    recipients.payment.pagoPaForm.ref.versionToken: **\<versionIdPagamento>**

Se la chiamata è andata a buon fine si otterrà una response con httpStatus: 202 ACCEPTED ed il seguente body:

<figure><img src="../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

**NOTA:** nel body della response si otterranno i seguenti campi:\
&#xNAN;**\<notificationRequestId>:** questo identificativo viene assegnato alla richiesta di notifica appena inserita e potrà essere utilizzato in seguito per verificare se sia stata accettata o meno dalla Piattaforma Notifiche.\
**\<paProtocolNumber>** e **\<idempotenceToken>:** questi campi sono gli stessi che sono stati inseriti nella precedente richiesta di inserimento Notifica e potranno essere utilizzati, in modo alternativo al **\<notificationRequestId>** ed insieme tra loro, per conoscere lo stato di accettazione della notifica su Piattaforma Notifiche.
