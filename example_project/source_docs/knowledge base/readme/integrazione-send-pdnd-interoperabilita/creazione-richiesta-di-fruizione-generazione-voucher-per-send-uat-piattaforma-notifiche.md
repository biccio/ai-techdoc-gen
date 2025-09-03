---
description: >-
  Informazioni utili sui passi da seguire per generare il Voucher che permette
  di utilizzare i servizi PND da Interoperabilità
---

# Creazione richiesta di fruizione generazione Voucher per SEND - UAT (Piattaforma Notifiche)

Di seguito vengono elencati i passaggi che permettono si generare il Voucher necessario per chiamare i servizi PND a seguito del completamento dell'adesione ad Interoperabilità. \
I seguenti passaggi sono anche documentati nei seguenti videotutorial:\
[https://docs.pagopa.it/interoperabilita-1/videotutorial](https://docs.pagopa.it/interoperabilita-1/videotutorial)

### Effettuare il login

E' possibile accedere ad Interoperabilità da qui: \
[https://selfcare.pagopa.it/auth/login](https://selfcare.pagopa.it/auth/login)\
inserendo le credenziali SPID/CIE dell'Amministratore. Una volta entrati, apparirà l'elenco degli Enti associati e sarà necessario selezionare quello di interesse ed accedere, poi selezionare la card:\
![](<../../.gitbook/assets/image (6).png>)

e selezionare "Collaudo"

![](<../../.gitbook/assets/image (29).png>)

### Creare una richiesta di fruizione per l'e-service di SEND - UAT

Per inviare una richiesta di fruizione bisogna prima cercare l'e-service andando su _Fruizione > Catalogo e-service:_

<figure><img src="../../.gitbook/assets/image (5).png" alt="" width="366"><figcaption></figcaption></figure>

poi avviare la ricerca dell'e-service di SEND - UAT e cliccare su _Richiedi fruizione_ creando una bozza di richiesta dove inserire tutte le informazioni richieste, tra cui gli attributi, che si dividono in:

* **Attributi certificati:** vengono verificati tramite le banche dati delle istituzioni.
* **Attributi Verificati:** vengono verificati dall’erogatore del servizio a seguito dell'invio della documentazione da parte del fruitore.
* **Attributi Dichiarati:** vengono dichiarati da chi effettua la richiesta di fruizione sotto la propria responsabilità

Maggiori dettagli sugli attributi sono qui: [https://docs.pagopa.it/interoperabilita-1/manuale-operativo/attributi](https://docs.pagopa.it/interoperabilita-1/manuale-operativo/attributi) \
il video-tutorial è qui:\
&#x20;[https://www.youtube.com/watch?v=zmyQIQHAo\_0\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3\_Q\&index=8](https://www.youtube.com/watch?v=zmyQIQHAo_0\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3_Q\&index=8)

Quando la richiesta di fruizione è stata compilata con successo, cliccare su "Inoltra richiesta di fruizione"

<figure><img src="../../.gitbook/assets/image (44).png" alt="" width="375"><figcaption></figcaption></figure>

Una volta che la richiesta di fruizione è stata inviata, questa verrà esaminata dall'Erogatore che dovrà approvarla. È sempre possibile verificare lo stato delle richieste di fruizione presentate andando su _Fruizione > Le tue richieste_.

Maggiori dettagli sulla richiesta di fruizione sono qui: [https://docs.pagopa.it/interoperabilita-1/manuale-operativo/richieste-di-fruizione](https://docs.pagopa.it/interoperabilita-1/manuale-operativo/richieste-di-fruizione)\
il video-tutorial è qui:\
[https://www.youtube.com/watch?v=2O81jdLHpgQ\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3\_Q\&index=8](https://www.youtube.com/watch?v=2O81jdLHpgQ\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3_Q\&index=8)

### Creare una finalità per l'e-service di SEND - UAT

A seguito dell'approvazione della richiesta di fruizione per l'e-service di SEND - UAT è necessario creare una finalità andando su _Fruizione > Le tue finalità_ e cliccando "Aggiungi"_._

<figure><img src="../../.gitbook/assets/image (33).png" alt="" width="563"><figcaption></figcaption></figure>

Compilare tutti i dati che appaiono sul Form, in particolare:

* **e-service da associare:** che dovrà corrispondere a quello di SEND - UAT
* **numero di chiamate stimate API/giorno:** corrisponde alla stima di chiamate al giorno che verranno effettuate verso l’erogatore. Questo valore potrà essere aggiornato in seguito e potrebbe essere necessaria l'attivazione manuale da parte dall’erogatore.

nella pagina successive bisogna compilare la sezione di analisi del rischio ed infine cliccare su "Crea bozza finalità" per pubblicare la finalità.

<figure><img src="../../.gitbook/assets/image (27).png" alt="" width="563"><figcaption></figcaption></figure>

Maggiori dettagli sulla creazione di finalità sono qui: [https://docs.pagopa.it/interoperabilita-1/manuale-operativo/finalita](https://docs.pagopa.it/interoperabilita-1/manuale-operativo/finalita)\
il video-tutorial è qui: \
[https://www.youtube.com/watch?v=bCHRgeBJucI\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3\_Q\&index=9](https://www.youtube.com/watch?v=bCHRgeBJucI\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3_Q\&index=9)

### Associare un client ad una finalità

Il client è un contenitore di materiale crittografico nel quale vengono inseriti un numero discrezionale di operatori di sicurezza, che sono autorizzati a caricare la chiave pubblica del materiale crittografico in loro possesso. \
Per creare un nuovo client bisogna andare nella sezione _Fruizione > I tuoi client e-service_ e cliccando su "Aggiungi"

<figure><img src="../../.gitbook/assets/image (49).png" alt="" width="563"><figcaption></figcaption></figure>

Compilare tutti i dati che appaiono sul Form, selezionando tra gli operatori quelli abilitati ad operare nel back-office. \
Una volta creato un client, sarà possibile associarlo ad una finalità, entrando in _Fruizione > Le tue finalità,_ poi nel tab "Client associati" cliccare su "Aggiungi"

<figure><img src="../../.gitbook/assets/image (12).png" alt="" width="563"><figcaption></figcaption></figure>

Infine apparirà un menù a tendina che permette di selezionare i client da associare:\


<figure><img src="../../.gitbook/assets/image (26).png" alt="" width="302"><figcaption></figcaption></figure>

I client possono anche essere riutilizzabili su più finalità e modificati successivamente.

Maggiori dettagli sul client sono qui: [https://docs.pagopa.it/interoperabilita-1/manuale-operativo/client-e-materiale-crittografico](https://docs.pagopa.it/interoperabilita-1/manuale-operativo/client-e-materiale-crittografico)\
I video-tutorial sono qui:\
[https://www.youtube.com/watch?v=w3ynRRMyrxg\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3\_Q\&index=10](https://www.youtube.com/watch?v=w3ynRRMyrxg\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3_Q\&index=10)\
[https://www.youtube.com/watch?v=w3ynRRMyrxg\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3\_Q\&index=10](https://www.youtube.com/watch?v=w3ynRRMyrxg\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3_Q\&index=10)

### Caricare una chiave pubblica

prima di caricare una chiave pubblica, entrare nella sezione _Fruizione > I tuoi client_ selezionare "Ispeziona" sul client di riferimento ed assicurarsi che sia presente "_IL TOKEN PUò ESSERE STACCATO: SI_" come segue:

<figure><img src="../../.gitbook/assets/image (21).png" alt="" width="563"><figcaption></figcaption></figure>

Poi accedere al tab "Chiavi pubbliche" e cliccare su "Aggiungi"

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Apparirà un pop up che permette di inserire il nome e la chiave pubblica associata al client.\


<figure><img src="../../.gitbook/assets/image (1).png" alt="" width="304"><figcaption></figcaption></figure>

Per generare il materiale crittografico, bisogna aprire il terminale e incollare i comandi che seguono, uno alla volta:

```
openssl genrsa -out <nomeChiave>.rsa.pem 2048
openssl rsa -in <nomeChiave>.rsa.pem -pubout -out <nomeChiave>.rsa.pub
openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt -in <nomeChiave>.rsa.pem -out <nomeChiave>.rsa.priv
```

Sostituendo \<nomeChiave> con il nome che si vuole dare al file contenente la chiave.

Il comando genererà una coppia di chiave pubblica e privata, ed un certificato che in questo caso non è necessario utilizzare. La chiave pubblica appena ottenuta, deve essere copiata nel riquadro "Chiave pubblica" del pop up del client; quella privata rimarrà in mano all'aderente, che la manterrà al sicuro e la userà per firmare la richiesta per ottenere un voucher dal server autorizzativo di PDND Interoperabilità.\
il video-tutorial è qui:\
[https://www.youtube.com/watch?v=q6zuJ2wn8vM\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3\_Q\&index=11](https://www.youtube.com/watch?v=q6zuJ2wn8vM\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3_Q\&index=11)

### Generare un Voucher

A questo punto è necessario generare il Voucher da inserire come Authorization header nelle chiamate verso i servizi B2B di SEND - UAT.

**1)** Il primo passo è costruire una _client assertion_ valida e firmarla con la propria chiave privata (che deve essere l'omologa della chiave pubblica depositata sul client su PDND Interoperabilità del punto sopra) come segue:\


<figure><img src="../../.gitbook/assets/image (10).png" alt="" width="375"><figcaption></figcaption></figure>

nel prima pagina "Client assertion", potremo selezionare la chiave pubblica di riferimento e generare la client assertion con i comandi script che troviamo nella sezione in basso \


<figure><img src="../../.gitbook/assets/image (30).png" alt="" width="294"><figcaption></figcaption></figure>

**NOTA:** modificare la variabile \<PATH\_CHIAVE\_PRIVATA> con il path della chiave privata generata al punto precedente. Per creare la client assertion è possibile utilizzare il codice:\
[https://github.com/pagopa/pn-b2b-client/blob/develop/create-client-assertion/src/main/java/it/pagopa/pdnd/CreateClientAssertionApp.java](https://github.com/pagopa/pn-b2b-client/blob/develop/create-client-assertion/src/main/java/it/pagopa/pdnd/CreateClientAssertionApp.java)

E' disponibile il corrispettivo codice java della classe per generare la "Client assertion" [CreateClientAssertionApp](https://github.com/pagopa/pn-b2b-client/blob/develop/create-client-assertion/src/main/java/it/pagopa/pdnd/CreateClientAssertionApp.java).&#x20;

**2)** Salviamo l'output ottenuto ed andiamo nella seconda pagina "Stacco access token", dove dovremo lanciare il comando che troviamo nella pagina in basso:

<figure><img src="../../.gitbook/assets/image (14).png" alt="" width="447"><figcaption></figcaption></figure>

**NOTA:** modificare la variabile \<LA\_TUA\_CLIENT\_ASSERTION> con l'output ottenuto al punto precedente **1)**.\
Per riprodurre il comando si può anche prendere come esempio questo codice: [https://github.com/pagopa/pn-b2b-client/blob/102ba3b4d790a3ccd378bd187525d8cb6937ff07/src/main/java/it/pagopa/pn/client/b2b/pa/impl/PnPaB2bExternalClientImpl.java#L199-L212](https://github.com/pagopa/pn-b2b-client/blob/102ba3b4d790a3ccd378bd187525d8cb6937ff07/src/main/java/it/pagopa/pn/client/b2b/pa/impl/PnPaB2bExternalClientImpl.java#L199-L212)

**3)** Come risposta al comando otterremo una response che contiene **access\_token, expires\_in** e **token\_type.** &#x20;

L'**access\_token(PDNDVoucher)** appena ottenuto corrisponde al Voucher che potrà essere utilizzato nelle chiamate verso i servizi B2B di SEND - UAT inserendolo come Header: `"Authorization: Bearer <PDNDVoucher>"`\
il video-tutorial è qui:\
[https://www.youtube.com/watch?v=fb-CDltaeqw\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3\_Q\&index=12](https://www.youtube.com/watch?v=fb-CDltaeqw\&list=PLZcD-ZoVxFzi1f2-taSdg7a3d2UQse3_Q\&index=12)

### Chiamare i servizi SEND - UAT

Per chiamare i servizi PND sarà necessario utilizzare la baseUrl dell'Ambiente UAT: [https://api.uat.notifichedigitali.it](https://api.uat.notifichedigitali.it) \
Inoltre sarà necessario generare delle nuove APIKey per l'Ambiente UAT effettuando l'accesso da qui: [https://selfcare.uat.notifichedigitali.it/](https://selfcare.uat.notifichedigitali.it/) con le stesse credenziali ottenute in fase di Onboarding, poi selezionare l'Ente di riferimento, cliccare su Piattaforma Notifiche UAT:\
![](<../../.gitbook/assets/image (43).png>)

e generare le APIKey da utilizzare unitamente al Voucher appena creato.
