---
description: >-
  Pagamenti multipli, Supporto F24, Modalità di integrazione asincrona con
  pagoPA
---

# API VERSIONE GA 2.1

## **Nuove funzionalità GA 2.1**

* **Pagamenti multipli**: possibilità di collegare più modelli di pagamento alla notifica (pagamenti alternativi o rateali).
* **Supporto modello di pagamento F24**: possibilità di collegare alla notifica pagamenti gestiti con modelli di pagamento F24 con invio dei metadati e gestione delle spese di notifica.
* **Modalità di integrazione asincrona con pagoPA**: integrazione con il modulo Gestione delle Posizioni Debitorie (GPD) di pagoPA con aggiornamento automatico dei costi di notifica. Modalità che semplifica l'integrazione, sollevando l'ente creditore dall'implementazione della chiamata all'API _notificationCost_ e dell'aggiornamento dell'importo; rendendo il pagamento meno soggetto a errori di comunicazione.

File di definizione OpenAPI: [https://raw.githubusercontent.com/pagopa/pn-delivery/v2.2.0-RC.1/docs/openapi/api-external-b2b-pa-bundle.yaml](https://raw.githubusercontent.com/pagopa/pn-delivery/v2.2.0-RC.1/docs/openapi/api-external-b2b-pa-bundle.yaml)

## Le modifiche alle API per supportare queste funzionalità

Nuova operation "Richiesta invio notifiche" _`sendNewNotificationV21`_\
`POST /delivery/v2.1/requests`&#x20;

### Pagamenti multipli

Ad ogni destinatario _`recipients`_ è possibile associare N pagamenti nell'array _`payments`_.

**ATTENZIONE**: il payload dei _`recipients`_ è cambiato e prevede un array _`payments`_ di pagamenti al posto del precedente  _`payment`_, quindi non utilizzate lo stesso payload della versione precedente altrimenti le notifiche saranno create senza pagamenti.

Gli elementi dell'arra&#x79;_`NotificationPaymentItem`_ possono essere di tipo _`pagoPa`_&#x6F; _`f24`_.

#### **Pagamento pagoPA**

Per il pagamento di tipo pagoPA deve essere valorizzato l'elemento _pagoPa_ il formato rimane identico ad eccezione del campo _`applyCost`_.

```json
"pagoPa": {
    "noticeCode": "",
    "creditorTaxId": "",
    "applyCost": true,
    "attachment": {
        "digests": {
            "sha256": "<shaDelPagoPA>"
        },
        "contentType": "application/pdf",
        "ref": {
            "key":<KeyRicevutaDall'Upload>,
            "versionToken": "<versionIdPagoPA>"
        }
    }
}
```

Se la notifica prevede l'attualizzazione dell'importo (`notificationFeePolicy=DELIVERY_MODE`) deve essere indicato su quale dei pagamenti devono essere riportati i costi della notifica indicando _`applyCost=true`_.

In caso di integrazione asincrona con pagoPA (_`pagoPaIntMode =ASYNC`_) il campo deve essere `true` per almeno numero avviso per destinatario se  e _`NotificationFeePolicy=DELIVERY_MODE`_

**NOTA**: Eliminato il campo `noticeCodeAlternative` che diventa uno dei pagamenti della notifica di tipo pagoPA.

#### **Pagamento F24**

Per il pagamento di tipo F24 deve essere valorizzato l'elemento f24:

```json
"f24": {
    "title": "<titoloF24>",
    "applyCost": true,
    "metadataAttachment": {
        "digests": {
            "sha256": "<shaF24>"
        },
        "contentType": "application/json",
        "ref": {
            "key": "<KeyRicevutaF24",
            "versionToken": "<versionIdF24>"
        }
    }
}
```

Il campo _`title`_ deve riportare una descrizione visibile al destinatario per capire quale modello F24 vuole visualizzare. Il campo non deve riportare nessun dato personale come nominativo, codice fiscale o altri dati protetti per privacy policy.

Il campo _`applyCost`_ di tipo boolean per indicare che devono essere addebitate le spese di notifica sulla modello F24 (si veda dettaglio). Una sola riga del modello F24 dovrà essere marcata con _`applyCost=true`_(tutte le altre devono riportar&#x65;_`applyCost=false`_) e dovrà riportare la cifra di costo di notifica a compensazione della PA mittente.

L'elemento _`metadataAttachment`_ deve riportare i riferimenti al file json dei metadati relativi ai dati che saranno riportati nel modello F24.

### Metadati F24

Per poter generare dinamicamente il modello F24 con l'importo che comprenda i costi della notifica nel modello F24, SEND richiede l'invio di un file in formato JSON contenente i dati del modello con indicazione di una riga nella quale andare ad aggiungere i costi della notifica (campo `applyCost`).\
Tale riga sarà già valorizzata con un importo che comprende il costo della notifica a copertura per la PA mittente (es: 100 eurocent).\
Se la notifica contiene N destinatari e M pagamenti F24 dovranno essere caricati N x M file di metadati per ogni modello.

### **Come si invia il file dei metadati F24**

Il file dei metadati del modello F24 è caricato sulla piattaforma con le stesse modalità degli altri documenti allegati alla notifica, tramite la chiamata all'api `newNotification/presignedUploadRequest` per ottenere gli url per il caricamento dei file.

Se la chiamata è andata a buon fine la response ci restituirà una URL e un secret che ci serviranno per eseguire l'upload dei file allegati, compreso il json dei metadati.

Una volta ricevuto l'URL per il caricamento del documento su S3 bisognerà impostare la chiamata da effettuare avendo cura di inserire negli headers:

* `Content-type: application/json`
* il valore di `x-amz-meta-secret` con ciò che ci ha restituito la chiamata precedente
* il valore di `x-amz-checksum-sha256` con lo sha del file json contenente i metadati

Ecco un esempio della chiamata:

```json
curl -X PUT \
-H "Content-type: application/json" \
-H "x-amz-meta-secret: <secretRicevuto>" \
-H "x-amz-checksum-sha256: <shaF24>" \
--data-binary '@F24.json' \
<urlRicevuta> --verbose
```

Allo stesso modo degli altri allegati la chiamata di upload restituirà l'header **x-amz-version-id** che dovrà essere utilizzato durante l'inserimento della notifica, nel campo ref.**versionToken** in corrispondenza del relativo pagamento F24.

**Le tipologie di F24 che si possono caricare sono le seguenti:**

_`f24Standard`_: F24 Ordinario

_`f24Simplified`_: F24 Semplificato

_`f24Excise`_: Accise

_`f24Elid`_:  F24 Elementi Identificativi

Lo schema di validazione per il file json dei metadata è pubblicato al seguente url:

* In formato Json Schema: [https://github.com/pagopa/pn-f24/blob/814485f5f2026a32110f71fde0ff6b7c763f49d1/docs/openapi/json-schema-from-deref-mod.json](https://github.com/pagopa/pn-f24/blob/814485f5f2026a32110f71fde0ff6b7c763f49d1/docs/openapi/json-schema-from-deref-mod.json)
* In formato OpenAPI: [https://raw.githubusercontent.com/pagopa/pn-f24/main/docs/openapi/schemas-f24.yaml](https://raw.githubusercontent.com/pagopa/pn-f24/480f99ca2faae7b33c05359fc1594fdd8edf4103/docs/openapi/schemas-f24.yaml)

## Indicazione della modalità di integrazione con pagoPA&#x20;

Nuovo elemento _`pagoPaIntMode`_ per indicare la modalità di integrazione con pagoPA dei numeri avviso pagoPA contenuti nella notifica.

**NOTA**: tutti i numeri avviso contenuti nella notifica devono avere la stessa modalità di integrazione.

* **ASYNC: modalità asincrona**
* **SYNC (default): modalità sincrona**

Aggiunto campo _`paFee`_&#x64;i tipo integer per indicare l'ammontare (espresso in eurocent) a copertura dei costi sostenuti dalla PA mittente in base a quanto previsto dal Decreto 30 maggio 2022 «Individuazione dei costi e dei criteri e modalità di ripartizione e ripetizione delle spese di notifica degli atti tramite la piattaforma di cui all'art. 26, comma 14 del decreto-legge 16 luglio 2022, n. 76». Il campo _`paFee`_ è necessario per imputare il valore corretto nel calcolo del costo della notifica per il modello di pagamento F24 e per la modalità d'integrazione asincrona con pagoPA.

### Altre modifiche

Aggiunto campo opzionale _`paymentExpirationDate`_ di tipo date con formato YYYY-MM-DD, serve per indicare la data di scadenza della pagamento della notifica (nel caso questo dato sia determinabile dalla PA mittente). Questo dato avrà il solo scopo informativo per l'utente, non ha alcuna implicazione sul workflow della notifica o del pagamento.
