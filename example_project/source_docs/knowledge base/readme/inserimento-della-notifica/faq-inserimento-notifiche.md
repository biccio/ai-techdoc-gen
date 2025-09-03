---
description: >-
  Domande e risposte sui casi d'uso più frequenti sulle API di inserimento
  Notifica di Piattaforma Notifiche
---

# FAQ inserimento notifiche

### Quando chiamo le API sulla pagina swagger ottengo errore

Le pagine Swagger sono esclusivamente ad uso di documentazione e non sono configurate per essere utilizzate per testare le API.

### Cosa devo fare se ricevo `{"message": "Unauthorized"}` quando chiamo le API?

Il messaggio indica che non sono disponibili le credenziali per utilizzare i servizi di PN o che non è stata completata l'integrazione con **PDND Interoperabilità**. \
Se non è stato già fatto, è necessario intraprendere il processo di accreditamento, contattando l'indirizzo preposto: [account@pagopa.it](mailto:account@pagopa.it)\
Se è stato già completato il processo di accreditamento, assicurarsi che si stia utilizzando correttamente l'API Key ed il Voucher.

### Le chiamate ai servizi esposti da PN sono sicuri?

Le chiamate ai servizi esposti da PN avvengono in modalità https utilizzando API Key. E' possibile attivare un layer aggiuntivo di sicurezza effettuando l'integrazione con **PDND Interoperabilità** che prevede l'inserimento di un Voucher da aggiungere all'API Key. Maggiori dettagli alla pagina che segue:

{% content-ref url="../integrazione-send-pdnd-interoperabilita/" %}
[integrazione-send-pdnd-interoperabilita](../integrazione-send-pdnd-interoperabilita/)
{% endcontent-ref %}

### Dopo aver fatto l'upload dei documenti della notifica nella fase 1, quanto tempo ho per inviare la notifica?

I documenti memorizzati su bucket S3 durante la fase di caricamento (1.a e 1.b del [Ciclo di vita della notifica lato mittente](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fdevelop%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa.yaml)) vengono mantenuti per 7 giorni, passati i quali vengono eliminati ed andranno ricaricati di nuovo se si vuole inoltrare la notifica.

### Quali sono i passi da seguire per effettuare l’inoltro della notifica in modalità B2B?

I passi da seguire sono i seguenti:

1. **Pre inoltro della documentazione (atto di notifica e modello di pagamento).**\
   Occorre chiamare il servizio [presignedUploadRequest ](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fmain%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa-bundle.yaml#/NewNotification/sendNewNotificationV23)per ottenere il/gli url da utilizzare per effettuare l'upload dei document&#x69;**.** Non è obbligatorio caricare il modello di pagamento.
2. **Upload della documentazione.**\
   Occorre effettuare, per ogni documento, una richiesta HTTP con metodo ed url restituiti dal servizio _presignedUploadRequest_ nella chiamata al punto precedent&#x65;**.**
3. **Invio della notifica.**\
   A seguito dell'upload dei documenti , bisogna chiamare il servizio [sendNewNotification ](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fmain%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa-bundle.yaml#/NewNotification/sendNewNotificationV23)per completare l'invio della notifica, avendo cura di valorizzare correttamente i riferimenti ai documenti caricati al punto precedente.

### Come avviene l’inoltro della notifica?

L’inoltro della notifica può avvenire in modalità _piattaforma web_ o _B2B_. La modalità _piattaforma web_ prevede l’utilizzo della webapp di Piattaforma Notifiche e consente l’inoltro puntuale di una notifica. La modalità _B2B_ prevede l’utilizzo dei servizi di Piattaforma Notifiche attraverso l'integrazione con le API e consente l’inoltro massivo di notifiche.

### Cosa NON inserire tra i metadati della notifica?

Tra i metadati della notifica **NON** bisogna mai inserire alcun tipo di dato personale o sensibile all'interno dei seguenti campi della notifica che non sono anonimizzati:

* **subject**
* **abstract**

### Quali controlli vengono effettuati contestualmente all'inserimento della notifica (controlli sincroni)?

I controlli sincroni vengono effettuati nel momento stesso in cui si invia la request al servizio di invio notifica.\
I controlli effettuati da PN sono i seguenti:

* verifica che le informazioni inserite siano sintatticamente corrette e rispettino i vincoli applicati sui campi delle entities.
* verifica che le combinazioni di **creditorTaxId/noticeCode** e **creditorTaxId/alternativeNoticeCode** siano univoche.
* verifica che la combinazione dei campi **senderPaId, paProtocolNumber, idempotenceToken** siano univoci.
* verifica che ciascun CF fornito sia corretto sintatticamente

### Quali controlli vengono effettuati a seguito dell'inserimento della notifica (controlli asincroni)?

I controlli asincroni sulla notifica partono dal momento successivo all'OK ottenuto in risposta all'inserimento della notifica e producono sempre un esito entro 24H da questo momento. L'esito dei controlli asincroni può essere verificato con l'apposito servizio [Verifica accettazione richiesta notifica](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fdevelop%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa.yaml#/SenderReadB2B/retrieveNotificationRequestStatus) o consumando il relativo evento di Timeline.\
I controlli effettuati da PN sono i seguenti:

* verifica che l'indirizzo fisico associato a ciascun destinatario sia esistente e che il CAP inserito sia specifico della località e non generico. Queste verifiche vengono effettuate con Postel.&#x20;
* verifica che lo hash sha256 inserito nella notifica corrisponda a quello dei documenti associati ad essa
* verifica che ogni allegato PDF contenga un’intestazione conforme, necessaria per l’identificazione corretta del documento.
* verifica che i metadati inseriti nel JSON fornito per la generazione degli F24 sia conforme allo schema previsto.
* verifica che la posizione debitoria inserita in caso di integrazione ASYNC sia esistente e creata sul portale GPD

**NOTA:** nel caso in cui una Notifica venga rifiutata in fase di validazione, PND fatturerà comunque alla PA mittente € 1 per ogni destinatario della notifica (a copertura dei servizi di PND).\
Vedi l'art. 4 comma 3 lettera d) dei [T\&C della piattaforma](https://docs.pagopa.it/documento-1-termini-condizioni-di-adesione-e-uso/).

### Come si sviluppa il workflow dell'invio della notifica?

Il processo di invio della notifica si sviluppa attraverso 2 diversi workflow:

* **Workflow Digitale**\
  Questo processo parte dopo aver verificato che il destinatario abbia **ALMENO UN** domicilio digitale tra quelli previsti (Domicilio digitale di piattaforma, Domicilio digitale speciale, Domicilio digitale generale). \
  Una volta avviato questo Workflow, nel caso di fallimento del primo tentativo di invio digitale, PND effettuerà un secondo tentativo di invio a distanza di 7 giorni. Al primo successo PND interromperà il tentativo di invio, mentre se anche il secondo tentativo di invio fallisce, verrà effettuato un invio con raccomandata semplice.
* **Workflow Analogico**\
  Questo processo parte solo dopo aver verificato che il destinatario **NON** abbia nessun domicilio digitale e prevede l'invio all'indirizzo del destinatario inserito nel campo _recipients.physicalAddress_ con invio di raccomandata del tipo valorizzato in _physicalCommunicationType_

### Cos'è il codice di tassonomia (taxonomyCode)?

Il codice di tassonomia `taxonomyCode` è un campo obbligatorio utilizzato per definire la tipologia di atto notificato.

Per le notifiche relative all'asseverazione del Bando è definito nell'_allegato 2 capitolo C_ del bando: [AVVISO PUBBLICO MISURA 1.4.5 PIATTAFORMA NOTIFICHE DIGITALI](https://pnrrcomuni.fondazioneifel.it/bandi_public/Bando/325)

In generale l'elenco esaustivo dei codici tassonomici è pubblicato in [questa pagina.](../../tassonomia-send.md)

### Come si individua il domicilio del destinatario di una notifica in base alla tipologia del destinatario (PF e PG)?

Quando si invia una notifica, occorre indicare la tipologia del destinatario:

* Se il destinatario è Persona Fisica (PF), l'ordine di individuazione è il seguente:
  1. Domicilio digitale di piattaforma (se disponibile, quello configurato dal destinatario per l'ente mittente della notifica; in alternativa, quello configurato dal destinatario per la genericità degli enti mittenti)
  2. Domicilio digitale speciale indicato dall’ente mittente nella creazione della notifica
  3. Domicilio digitale generale fornito dal registro pubblico **INAD**
* se il destinatario è Persona Giuridica (PG), l'ordine di individuazione è il seguente:
  1. Domicilio digitale di piattaforma (se disponibile, quello configurato dal destinatario per l'ente mittente della notifica; in alternativa, quello configurato dal destinatario per la genericità degli enti mittenti)
  2. Domicilio digitale speciale indicato dall’ente mittente nella creazione della notifica
  3. Domicilio digitale generale fornito dal registro delle imprese **IniPEC**

### Quale relazione esiste tra eventi di timeline e stati della notifica?

Non esiste una corrispondenza 1:1 tra eventi di timeline e cambiamenti di stato; in particolare, solo alcuni eventi di timeline scatenano un cambiamento di stato.

### Cosa fare quando eseguendo l’upload del documento si ottiene il seguente errore: <mark style="color:red;">`<Code>SignatureDoesNotMatch</Code>`</mark> <mark style="color:red;">`<Message>The request signature we calculated does not match the signature you provided. Check your key and signing method.</Message>`</mark>

Esistono varie casistiche che generano l’errore descritto; le più frequenti sono:

1. In _uploadAllegati_ si è utilizzato uno sha256 diverso da quello utilizzato in _presignedUploadRequest_.
2. In _uploadAllegati_ è stato inserito uno sha256 che non corrisponde al documento che si desidera effettivamente inviare.
3. Lo sha256 è corretto in _presignedUploadRequest_ e coincidente con quello caricato in _uploadAllegati_, ma il secret errato.
4. Se si utilizza Postman assicurarsi che gli header siano valorizzati correttamente e che il documento che si sta caricando sia effettivamente quello dal quale è stato generato lo Sha256(a volte è necessario rimuovere e ricaricare il file dalla scheda di Postman affinchè venga recepito)&#x20;
5. Assicurarsi che gli header siano valorizzati correttamente ed inseriti nel giusto ordine (vedi 1.b del [Ciclo di vita della notifica lato mittente](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fdevelop%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa.yaml))

### Cosa fare quando si invoca il servizio di upload di un documento, passando x-amz-checksum-sha256 del file, si ottiene il seguente errore: `Value for x-amz-checksum-sha256 header is invalid`

Assicurarsi di avere eseguito i seguenti passaggi:

1. Applicare al documento l’algoritmo di crittazione, ottenendo una rappresentazione di 64 caratteri in formato esadecimale ^\[A-Fa-f0-9]{64}$
2. Ottenere la relativa rappresentazione binaria.
3. Applicare la codifica Base64.

Esempio di codice Java:

`import org.springframework.util.Base64Utils;`\
`import java.io.ByteArrayInputStream;`\
`import java.io.InputStream;`\
`import java.security.MessageDigest;`

`MessageDigest digest = MessageDigest.getInstance("SHA-256");`\
`byte[] encodedhash = digest.digest( StreamUtils.copyToByteArray( docInputStream ) );`\
`String x-amz-checksum-sha256 = Base64Utils.encodeToString( hash )`

### Come si può verificare che lo "x-amz-checksum-sha256" sia corretto?

Aprire la shell di Git Bash o un terminal SSH ed eseguire il comando:

`cat <fullPathFile/filename.ext> | openssl dgst -binary -sha256 | openssl base64`

Il comando restituisce la codifica base64 della rappresentazione binaria di sha256, che può essere confrontato con quella generata dal codice.

### Come posso simulare l'upload di un documento su S3?

Aprire la shell di Git Bash o un terminal SSH ed eseguire il comand&#x6F;_:_

`curl -X<httpMethod> \`\
`-H"Content-type: application/pdf" \`\
`-H"x-amz-meta-secret: <secret>" \`\
`-H"trailer: x-amz-checksum-sha256" \`\
`-H"x-amz-checksum-sha256: <checkSum>" \`\
`--data-binary "@<filePath>"  \`\
`"<url>"`

**\<httpMethod>**: è il metodo http (PUT o POST) indicato nella response della preload, da utilizzare per questa chiamata\
&#xNAN;**\<secret>**: è il secret ottenuto nella response della preload\
&#xNAN;**\<checksum>**: è il checksum sha256, codificato in base 64, del contenuto binario del file da caricare\
&#xNAN;**\<file>**: è il path del file da caricare\
&#xNAN;**\<url>**: è l'url del bucket S3 ottenuto nella response della preload, sul quale effettuare l'upload del documento\
**NOTA:** l'header `-H"trailer: x-amz-checksum-sha256"` è non obbligatorio ai fini del buon esito della chiamata, per tanto può essere omesso qualora si riscontrassero problemi durante questa fase; inoltre si evidenzia che in questa chiamata **NON** deve essere inserito l'Autorization Header `"Authorization: Bearer <PDNDVoucher>`con il Vocuher.

### Quanto tempo ho per scaricare le Attestazioni Opponibili a Terzi?

Gli atti opponibili ai terzi e i documenti relativi alla notificazione analogica e digitale (forniti dall'operatore postale e dal PEC provider) vengono archiviati da PN. Su entrambe le tipologie di documento vengono posti legal hold e retention a 10 anni; pertanto possono essere scaricati anche successivamente alla loro generazione.

### Quali sono le Attestazioni Opponibili a Terzi?

Le Attestazioni opponibili ai terzi sono:

* **Notifica presa in carico** - generato dall’evento **REQUEST\_ACCEPTED** ed avente come _legalFactType: **SENDER\_ACK**_
* **Notifica digitale** - generato dall’evento **DIGITAL\_SUCCESS\_WORKFLOW** ed avente come _legalFactType: **DIGITAL\_DELIVERY**_
* **Mancato recapito digitale** - generato dall’evento **DIGITAL\_FAILURE\_WORKFLOW** ed avente come _legalFactType: **DIGITAL\_DELIVERY**_
* **Avvenuto accesso** - generato dall’evento **NOTIFICATION\_VIEWED** ed avente come _legalFactType: **RECIPIENT\_ACCESS**_
* **Deposito di avvenuta ricezione** - generato dall’evento **COMPLETELY\_UNREACHABLE** ed avente come _legalFactType_: **ANALOG\_FAILURE\_DELIVERY**
* **Malfunzionamento e ripristino** - generata nei casi di downtime del servizio PND, scaricabile direttamente dalla pagina di Piattaforma Notifiche nella sezione “**Stato della Piattaforma**”

Sono esposte nel portale anche le attestazioni prodotte da sistemi esterni quali:

* **Ricevute XML dell’esito relativo all’invio PEC** - generate dagli eventi **SEND\_DIGITAL\_PROGRESS** e **SEND\_DIGITAL\_FEEDBACK**, ed aventi come _legalFactType: **PEC\_RECEIPT**_
* **Ricevuta di accettazione raccomandata** - generato dall’evento **SEND\_ANALOG\_PROGRESS** ed avente come _legalFactType: **ANALOG\_DELIVERY**_
* **Ricevuta di consegna raccomandata** e **Ricevuta di mancata consegna raccomandata** – generato dall’evento **SEND\_ANALOG\_FEEDBACK** ed avente come _legalFactType: **ANALOG\_DELIVERY**_

### Dopo aver lanciato il servizio [sendNewNotification](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fdevelop%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa.yaml#/NewNotification/sendNewNotification) ottengo un messaggio di errore su: "Max one recipient", "No recipient physical address", "No recipient payment", "Alternative notice code equals to notice code". Cosa devo fare?

Contatta il [supporto enti](mailto:pn-supporto-enti@pagopa.it) segnalando questa situazione.

### Dopo aver lanciato il servizio [sendNewNotification](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fdevelop%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa.yaml#/NewNotification/sendNewNotification) ottengo un messaggio di errore "400: invaild request body"

Questo tipo di errore è dovuto all'errata compilazione del body della request, infatti la configurazione di OpenAPI prevede che i campi null vengano ignorati e non inseriti nella request.\
In questo caso fare è necessario fare attenzione alle seguenti:

* se il campo sullo Swagger risulta opzionale ma nella request che si sta inviando è valorizzato con null, è necessario eliminare del tutto questo campo dal body ed in generale dal JSON della request.
* se il campo è di tipo enum, fare attenzione che non sia valorizzato con stringa vuota "" ma che abbia un valore coerente con quelli dell'enum di appartenenza
* se il campo è di tipo stringa, fare attenzione che non sia valorizzato come numero intero

Se si utilizza un client Java, può capitare che pur non effettuando il set di una certa proprietà, il comportamento di default in fase di serializzazione delle proprietà non settate viene definito comunque come null. In questo caso è possibile seguire una delle seguenti soluzioni

* configurare l’ObjectMapper per far sì che includa solamente i campi NON\_NULL con la seguente configurazione: _mapper.setSerializationInclusion(Include.NON\_NULL);_
* se si utilizza la libreria Jackson per la serializzazione delle request, è possibile aggiungere questa annotation a livello di Classe:\
  &#xNAN;_@com.fasterxml.jackson.annotation.JsonInclude(com.fasterxml.jackson.annotation.JsonInclude.Include.NON\_NULL)_

### Posso riutilizzare lo stesso IUV di una notifica rifiutata?

SI, nel caso una notifica vada in stato di REFUSED tramite validazione asincrona è possibile utilizzare lo stesso IUV per fare una nuova richiesta di notifica.

### Come si possono testare più Enti?

In ambiente di collaudo UAT si prevede di creare una User per ogni Ente che permette di accedere alla piattaforma di Back-Office ed una key ad esso associata. Se si sta testando l'integrazione per più Enti bisognerà richiedere, per ogni Ente, una user ed una key ad essa associata, contattando il [supporto enti](mailto:pn-supporto-enti@pagopa.it)

### Come posso testare il caso d'uso della Multa per violazione del Codice della Strada?

E' possibile inserire una Multa per violazione del Codice della Strada su Piattaforma Notifiche avendo cura di valorizzare i campi:

1. NewNotificationRequest.recipients.payments.**noticeCode:** col numero avviso corrispondente al prezzo ridotto; questo verrà visualizzato in Piattaforma nella sezione di pagamento online con l'importo corrispondente entro 5 giorni dalla data di perfezionamento della notifica.
2. NewNotificationRequest.recipients.payments.**noticeCode:** col numero avviso corrispondente al prezzo intero; questo verrà visualizzato in Piattaforma nella sezione di pagamento online con l'importo corrispondente tra i 5 ed i 60 giorni dalla data di perfezionamento della notifica.
3. il bollettino di pagamento può essere caricato nel campo NewNotificationRequest.recipients.payment.**pagoPa** se è contenuto in un file diverso da quello dell'atto e sarà scaricabile dal destinatario nella sezione "_Scarica l'avviso PagoPA"_. \
   Se invece questo è già presente nello stesso pdf contenente l'atto, potrà essere caricato come unico pdf all'interno del campo NewNotificationRequest.**documents** e sarà scaricabile dal destinatario unitamente all'atto nella sezione "_DOCUMENTI ALLEGATI"_

### Quali sono i passaggi per visualizzare la funzione di pagamento online?

Per permettere la visualizzazione della funzione di pagamento online, la PA Mittente dovrà inserire una notifica valorizzando i campi come segue:

* NewNotificationRequest.recipients.payments.**creditorTaxId:** con la partita iva della PA Mittente
* NewNotificationRequest.recipients.payments.**noticeCode:** con il numero avviso.

A questo punto bisogna entrare nel portale lato cittadino, accedere al dettaglio della notifica appena inviata ed apparirà la voce _Paga XXX_ per pagare online come in foto.

![](<../../.gitbook/assets/image (8).png>)

Se invece la PA Mittente ha inserito il bollettino di pagamento separatamente dall'atto, all'interno del campo NewNotificationRequest.recipients.payments.**pagoPa,** entrando nel portale lato cittadino ed accedendo al dettaglio della notifica appena inviata, apparirà la voce _Paga XXX_ per pagare online e _Scarica l'avviso PagoPA_ per scaricare il bollettino di pagamento come in foto.

<img src="../../.gitbook/assets/image (46).png" alt="" data-size="original">

### Come si può testare la correttezza del Codici Fiscale?

E' possibile testare la correttezza di un codice fiscale con il regex:\
`^([A-Z]{6}[0-9LMNPQRSTUV]{2}[A-Z]{1}[0-9LMNPQRSTUV]{2}[A-Z]{1}[0-9LMNPQRSTUV]{3}[A-Z]{1})|([0-9]{11})$`

### Quali sono i passaggi per testare la visualizzazione della notifica?

Per testare la visualizzazione della notifica occorre inviare una notifica ad uno dei seguenti utenti:

* Michelangelo Buonarroti con codice fiscale: BNRMHL75C06G702B

Successivamente sarà possibile visualizzare le notifiche entrando nel portale lato cittadino da:\
[https://login.uat.notifichedigitali.it/login](https://login.uat.notifichedigitali.it/login)\
inserendo le credenziali dell’utente a cui sono state inviate le notifiche:

* per Michelangelo Buonarroti username: michelangelo e password: password123

ed entrando nel dettaglio della notifica appena inviata, che dopo alcuni secondi risulterà **Visualizzata**.\
**NOTE:** lo stato della notifica **Visualizzata NON** corrisponde necessariamente al Perfezionamento per presa visione. Per i dettagli sul perfezionamento vedi [Perfezionamento della notifica. ](../perfezionamento-della-notifica.md)

### Come gestisce un Ente le spese di notifica verso il destinatario?

L’Ente ha la possibilità di applicare un costo forfettario (**FLAT\_RATE**) o di applicare in maniera puntuale i costi della notifica in base alla modalità di consegna (**DELIVERY\_MODE**).\
Nello specifico, quando l’Ente effettua una richiesta di notifica tramite il servizio di [invio notifica](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fdevelop%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa.yaml#/NewNotification/sendNewNotification) deve valorizzare l’elemento notificationFeePolicy per indicare la politica di addebitamento dei costi di notifica.

### In quale modo l’Ente comunica a Piattaforma Notifiche il costo forfettario?

L’Ente può gestire autonomamente il costo forfettario, definendolo in fase di creazione della posizione debitoria, poiché PN non gestisce il costo forfettario di notifica.\
Il costo forfettario si applica nei casi in cui l'Ente voglia assumersi completamente i costi di notifica, oppure nel caso in cui esista una legge che impone all’Ente l'utilizzo di costi di notifica diversi da quelli previsti dal DPCM Costi di Piattaforma Notifiche.

### Con quale logica l'API notificationPrice risponde?

l'API[ NotificationPriceV23](../../api-changelog/api-versione-ga-2.3.md#nuova-api-retrievenotificationpricev23), quando riceve come parametri il codice ente creditore (**paTaxId**) e il numero avviso (**noticeCode**) di pagoPA risponde come segue:

* 0 se il _notificationFeePolicy=FLAT\_RATE_. Questo permette alla PA mittente di applicare al destinatario un costo forfettario stabilito dalla PA mittente stessa.
* € 1 (per PND) se il _notificationFeePolicy=DELIVERY\_MODE_ e la notifica NON ha comportato invio cartaceo
* € 1 (per PND) se il _notificationFeePolicy=DELIVERY\_MODE_ + X € costo dell'invio cartacea\
  **NOTA:** il costo X dell'invio cartaceo dipende dai tabellari dei prezzi di aggiudicazione delle gare pubbliche di recapito, visibili qui:\
  [https://pagopa.portaleamministrazionetrasparente.it/moduli/downloadFile.php?file=oggetto\_allegati/23501547570O\_\_OPREZZI+DI+AGGIUDICAZIONE+GARA+SERVIZI+POSTALI+E+SERVIZI+%26%238220%3BA+VALLE%26%238221%3B+DEL+RECAPITO.docx.pdf](https://pagopa.portaleamministrazionetrasparente.it/moduli/downloadFile.php?file=oggetto_allegati/23501547570O__OPREZZI+DI+AGGIUDICAZIONE+GARA+SERVIZI+POSTALI+E+SERVIZI+%26%238220%3BA+VALLE%26%238221%3B+DEL+RECAPITO.docx.pdf)

A questo punto la PA mittente può decidere a sua discrezione se addebitare al destinatario anche €1 previsti dalla legge a copertura dei costi sostenuti dalla PA stessa.

l'API[ NotificationPriceV23](../../api-changelog/api-versione-ga-2.3.md#nuova-api-retrievenotificationpricev23) fornisce inoltre, se presente, anche la **notificationViewDate** (data di visualizzazione della notifica) e la **refinementDate** (data di perfezionamento per decorrenza): se una delle due è presente nella response del servizio, significa che il costo restituito non subirà ulteriori variazioni in futuro.\
E' possibile sfruttare questa informazione per anticipare la chiamata al servizio e completare l'attualizzazione del costo di notifica anche prima del tentativo di pagamento da parte del destinatario. In tutti gli altri casi è sempre necessario completare l'attualizzazione del costo di notifica durante la fase di pagamento da parte del destinatario.\
**NOTE:** la presenza della **notificationViewDate** valorizzata **NON** comporta necessariamente il Perfezionamento per presa visione. Per i dettagli sul perfezionamento vedi: [Perfezionamento delle notifica](../perfezionamento-della-notifica.md).

### Il servizio notificationPrice può restituire valori diversi nel tempo per la stessa combinazione paTaxId/noticeCode?

Si, Il servizio[ NotificationPriceV23](../../api-changelog/api-versione-ga-2.3.md#nuova-api-retrievenotificationpricev23) restituisce valori diversi in base al ciclo di vita della notifica ed agli eventi di spedizione collegati. <mark style="color:red;">**E' quindi di fondamentale importanza che nella fase di pagamento da parte del destinatario, la PA mittente contatti il servizio**</mark> [ NotificationPriceV23](../../api-changelog/api-versione-ga-2.3.md#nuova-api-retrievenotificationpricev23) <mark style="color:red;">**completando l'attualizzazione delle spese di notifica**</mark>**.** infatti anche se negli stream viene restituito l'analogCost in relazione all’evento che introduce tale costo, il destinatario potrebbe sempre entrare nella piattaforma un attimo prima che venga letto lo stream e, se non venisse chiamato il[ NotificationPriceV23](../../api-changelog/api-versione-ga-2.3.md#nuova-api-retrievenotificationpricev23) durante la fase di pagamento, si rischia che non vengano addebitate al destinatario le corrette spese di spedizione e che quindi questo paghi un importo inferiore al dovuto.

### Come avviene la fatturazione di PN nei confronti della PA mittente?

PND fatturerà alla PA mittente, nei termini previsti dal contratto di adesione, le notifiche indipendentemente dalla scelta delle PA (**FLAT\_RATE/DELIVERY\_MODE**) i seguenti costi:

* € 1 per servizio PN per ogni destinatario della notifica (a copertura dei servizi di PND)
* il costo di tutti gli invii cartacei (a copertura dei servizi di postalizzazione)

### Cosa rappresenta lo status "Unreachable"?

Lo status **"Unreachable"** rappresenta il caso nel quale la piattaforma non è riuscita a raggiungere il destinatario; questo vale anche nei casi in cui la postalizzazione ha avuto luogo ma il destinatario è risultato irreperibile all'indirizzo noto. \
In questi casi si applicano le spese di notifica sostenute e l'atto depositato è considerato notificato.

### Quando invio la notifica ricevo un'errore sulla lunghezza dei campi dell'address, come procedo?

Può verificare questa pagina di faq creata appositamente, nel quale vengono indicate le regole sulla lunghezza e la [composizione dell'indirizzo](../validazione-della-richiesta-di-notifica/composizione-degli-indirizzi.md).

### Qual è la differenza tra l’utilizzo del prodotto postale 890 e la raccomandata AR secondo la normativa applicabile?

Il mittente deve scegliere il prodotto postale in base alla normativa allo stesso applicabile: se è un atto per cui ha l'obbligo di notificare al destinatario, dovrà scegliere 890; se è un atto per cui non è previsto obbligo di notificazione potrà avvalersi anche della raccomandata AR. L'art 26, comma 3 prevede infatti che send può essere utilizzata anche per trasmettere atti per cui non c'è obbligo di notificazione al destinatario

