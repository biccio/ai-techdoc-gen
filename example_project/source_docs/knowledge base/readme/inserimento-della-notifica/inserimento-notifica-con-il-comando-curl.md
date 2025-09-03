---
description: >-
  Descrizione step-by-step per l'inserimento della notifica utilizzando il
  comando curl
---

# Inserimento Notifica con il comando curl

**NOTA:** i comandi che verranno descritti di seguito dovranno essere lanciati con un terminal SSH, su OS Windows si può utilizzare ad esempio git bash.

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

Lanciare il seguente comando:

```bash
curl --location 'https://<baseurlAmbiente>/delivery/attachments/preload' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'x-api-key: <apiKey>' \
--header 'Authorization: Bearer <PDNDVoucher>' \
--data '[
{
  "preloadIdx": "<preloadIdx1>",
  "contentType": "application/pdf",
  "sha256": "<shaDellaNotifica>"
},
{
  "preloadIdx": "<preloadIdx2>",
  "contentType": "application/pdf",
  "sha256": "<shaDelPagamento>"
}]'
```

**NOTA:** sostituire i seguenti:

* **\<baseurlAmbiente>:** inserire la url dell'ambiente di riferimento, nel caso di UAT è il seguente: **https://api.uat.notifichedigitali.it**
* **\<apiKey>:** inserire la apiKey dell'Ente di riferimento, precedentemente generata su PND&#x20;
* **\<PDNDVoucher>:** inserire inserire il Voucher generato su **PDND Interoperabilità,** assicurandosi che non sia scaduto
* **\<shaDellaNotifica>:** è lo sha256 della Notifica che si ottiene come output al punto 1.1
* **\<shaDelPagamento>:** è lo sha256 del Pagamento che si ottiene come output al punto 1.2
* il valori **\<preloadIdx1>** e **\<preloadIdx2>** sono a discrezione del chiamante e servono per associare un indice alle richieste presenti nell'array di questa request

Nella response di questo servizio, si otterrà il seguente payload:

```json
[
  { 
    "preloadIdx": "<preloadIdx1>", 
    "secret": "<secret1>", 
    "httpMethod": "<httpMethod1>", 
    "url": "<url1>", 
    "key": "<key1>"
  },
  { 
    "preloadIdx": "<preloadIdx2>", 
    "secret": "<secret2>", 
    "httpMethod": "<httpMethod2>", 
    "url": "<url2>", 
    "key": "<key2>" 
  }
]
```

**NOTA:** i valori ottenuti nella response dovranno essere memorizzati per i futuri utilizzi; nello specifico:

* **\<preloadIdx1>** e **\<preloadIdx2>:** hanno il solo scopo di fare riferimento agli elementi mettendo in correlazione request/response
* **\<secret1>** e **\<secret2>:** andranno utilizzati nella chiamata di upload dei documenti
* **\<httpMethod1> e \<httpMethod2>:** corrispondono al http method da utilizzare nella chiamata di upload dei documenti
* **\<url1>** e **\<url2>:** sono le url da utilizzare nella chiamata di upload dei documenti
* **\<key2>** e **\<key2>:** sono le keys da utilizzare in fase di inserimento notifica, rispettivamente per i 2 file

### 3) Effettuare l'upload dei documenti&#x20;

Effettuare l'operazione di upload verso il _safeStorage_ per entrambi i documenti di interesse effettuando le seguenti chiamate:

* Upload del documento Notifica.pdf

```bash
curl -X <httpMethod1> \
-H "Content-type: application/pdf" \
-H "x-amz-meta-secret: <secret1>" \
-H "x-amz-checksum-sha256: <shaDellaNotifica>" \
--data-binary '@Notifica.pdf' \
<url1> --verbose
```

**NOTA:** nella chiamata fare attenzione a sostituire i campi parametrici con le informazioni ottenute agli altri punti. Da notare che il comando **--data-binary** è necessario per fare l'upload del documento e bisognerà inserire la **@** prima del path del file che si sta caricando.\
E' importante lanciare la curl con il --verbose che permetterà di visualizzare nell'header della response di esito positivo il valore di x-amz-version-id: **\<versionIdNotifica>** utile per la prossima chiamata.\
Assicurarsi di **NON** inserire in questa chiamata l'Autorization Header `"Authorization: Bearer <`PDNDVoucher`>`con il Vocuher.

* Upload del documento Pagamento.pdf

```bash
curl -X <httpMethod2> \
-H "Content-type: application/pdf" \
-H "x-amz-meta-secret: <secret2>" \
-H "x-amz-checksum-sha256: <shaDelPagamento>" \
--data-binary '@Pagamento.pdf' \
<url2> --verbose
```

**NOTA:** nella chiamata fare attenzione a sostituire i campi parametrici con le informazioni ottenute agli altri punti. Da notare che il comando **--data-binary** è necessario per fare l'upload del documento e bisognerà inserire la **@** prima del path del file che si sta caricando.\
E' importante lanciare la curl con il --verbose che permetterà di visualizzare nell'header della response di esito positivo il valore di x-amz-version-id: **\<versionIdPagamento>** utile per la prossima chiamata.\
Assicurarsi di **NON** inserire in questa chiamata l'Autorization Header `"Authorization: Bearer <`PDNDVoucher`>`con il Vocuher.

### 4) Effettuare l'inserimento della notifica

A questo punto è possibile effettuare l'inserimento della Notifica con la seguente chiamata:

```bash
curl --location 'https://<baseurlAmbiente>/delivery/v2.3/requests' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'x-api-key: <apiKey>' \
--header 'Authorization: Bearer <PDNDVoucher>' \
--data-raw '<payloadDellaNotifica>'
```

**NOTA:**

* **\<baseurlAmbiente>:** inserire la url dell'ambiente di riferimento, nel caso di UAT è il seguente: **https://api.uat.notifichedigitali.it**
* **\<apiKey>:** inserire la apiKey dell'Ente di riferimento, precedentemente generata su PND
* **\<PDNDVoucher>**: inserire inserire il Voucher generato su **PDND Interoperabilità**, assicurandosi che non sia scaduto
* **\<payloadDellaNotifica>:** corrisponde al json contenente tutti i dati della notifica; per inserire correttamente i riferimenti ai pdf caricati in precedenza, seguire le seguenti istruzioni:
  * Valorizzare i seguenti riferimenti al file Notifica.pdf\
    documents.digests.sha256:  **\<shaDellaNotifica>**\
    documents.contentType: **"application/pdf"**\
    documents.ref.key: **\<key1>**\
    documents.ref.versionToken: **\<versionIdNotifica>**
  * Valorizzare i seguenti riferimenti al file Pagamento.pdf\
    recipients.payment.pagoPaForm.digests.sha256: **\<shaDelPagamento>**\
    recipients.payment.pagoPaForm.contentType: **"application/pdf"**\
    recipients.payment.pagoPaForm.ref.key: **\<key2>**\
    recipients.payment.pagoPaForm.ref.versionToken: **\<versionIdPagamento>**

Se la chiamata è andata a buon fine si otterrà una response con httpStatus: 202 ACCEPTED ed il seguente body:

```json
{
    "notificationRequestId": <notificationRequestId>,
    "paProtocolNumber": <paProtocolNumber>,
    "idempotenceToken": <idempotenceToken>
}
```

**NOTA:** nel body della response si otterranno i seguenti campi:\
&#xNAN;**\<notificationRequestId>:** questo identificativo viene assegnato alla richiesta di notifica appena inserita e potrà essere utilizzato in seguito per verificare se sia stata accettata o meno dalla Piattaforma Notifiche.\
**\<paProtocolNumber>** e **\<idempotenceToken>:** questi campi sono gli stessi che sono stati inseriti nella precedente richiesta di inserimento Notifica e potranno essere utilizzati, in modo alternativo al **\<notificationRequestId>** ed insieme tra loro, per conoscere lo stato di accettazione della notifica su Piattaforma Notifiche.
