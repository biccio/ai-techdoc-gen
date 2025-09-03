---
description: >-
  Inserimento dei campi IVA sui costi di invio cartaceo (vat), indicazione della
  quota del costo di notifica a favore dei mittenti (PaFee) e nuova API
  retrieveNotificationPrice.
---

# API VERSIONE GA 2.3

## **Nuove funzionalità GA 2.3**

* **Gestione IVA sui costi di invio cartaceo**
* **Quota del costo di notifica a favore dei mittenti**
* **API di recupero dei costi della notifica: retriveNotificationPriceV23**

File di definizione OpenAPI [https://raw.githubusercontent.com/pagopa/pn-delivery/v2.4.0/docs/openapi/api-external-b2b-pa-bundle.yaml](https://raw.githubusercontent.com/pagopa/pn-delivery/v2.4.0/docs/openapi/api-external-b2b-pa-bundle.yaml)

## Le modifiche alle API per supportare queste funzionalità

La gestione dei nuovi dati _**`vat`**_ e _**`paFee`**_ ha comportato l'aggiunta di nuove API e la determinazione di valori di default per retro-compatibilità di quelle esistenti. Questo permette alla piattaforma di effettuare il calcolo complessivo dei costi di notifica necessari per attualizzare l'importo nel caso di integrazione asincrona con pagoPA o nel caso di pagamento tramite modello F24.

Per semplicità di integrazione è stata realizzata una nuova API per recuperare tutti gli elementi che compongono il costo di notifica (retrieveNotificationPriceV23).

Le nuove operation sulle API sono:

* **sendNewNotificationV23:** Richiesta invio nuova notifica.
* **NewNotificationRequestStatusResponseV23**: Verifica accettazione richiesta notifica.
* **FullSentNotificationV23**: Lettura dettagli notifica.
* **retrieveNotificationPriceV23**: Recupero delle componenti del costo di notifica.

### Gestione IVA sui costi di invio cartaceo

Per permettere al mittente la gestione dell'applicazione dell'IVA ai costi di invio cartaceo, in base al proprio regime fiscale,  è stato aggiunto alla richiesta di notifica l'elemento _**`vat`**_.

Il valore specificato nel campo _**`vat`**_ (IVA) deve essere un valore intero ed è obbligatorio in caso di _`notificationFeePolicy=DELIVERY_MODE` o di notifiche con allegati di pagamento modello F24._

Il valore di default nei casi di non obbligatorietà è 22 ( intesa come iva 22%)

Esempio: IVA al 22% -> specificare l'elemento _**`vat`**_ = 22

### **Quota del costo di notifica a favore dei mittenti**

Il campo _**`paFee`**_ (quota del costo di notifica a favore dei mittenti), indica l'importo in eurocent da applicare al mittente per coprire i costi della spedizione (Decreto Costi del  30 maggio 2022 all'art. 5, comma 1, lettera a).

Questo campo diventa obbligatorio per le notifiche che hanno:

* il campo _`notificationFeePolicy=DELIVERY_MODE`_
* la modalità di integrazione con pagoPA asincrona (_`pagoPaIntMode=ASYNC`_)
* Nel caso la notifica abbia collegato un pagamento tramite modell&#x6F;_`F24`_

Di default, se non è obbligatorio, l'importo predefinito è di 100 eurocent.

Esempio: quota di copertura spese mittente 1€ -> specificare l'elemento _**`paFee`**_ = 100&#x20;

### **Nuova API retrieveNotificationPriceV23**&#x20;

La nuova operation `retrieveNotificationPriceV23` (path`/delivery/v2.3/price/{paTaxId}/{noticeCode}`) affianca la precedente operation `retrieveNotificationPrice` e restituisce tutte le componenti del costo della notifica:

* **partialPrice**: indica il costo totale di notifica in eurocent che non include la componente a rimborso della PA (indicata nell'elemento `paFee` della notifica) e non include l'iva sul costo degli invii cartacei (calcolata sulla percentuale nell'elemento `vat` della notifica);
* **totalPrice**: indica il costo totale di notifica in eurocent che include la componente a rimborso della PA (indicata nell'elemento `paFee` della notifica) e l'iva sul costo degli invii cartacei (calcolata sulla percentuale nell'elemento `vat` della notifica).  Presente solo se entrambi i campi paFee e vat sono stati valorizzati.
* **sendFee**: costo base di SeND per notificazione.
* **analogCost**: costo totale dei prodotti postali.
* [**vat**](api-versione-ga-2.3.md#iva): costo IVA applicata ai costi di invio cartaceo.
* [**paFee**](api-versione-ga-2.3.md#quota-del-costo-di-notifica-a-favore-dei-mittenti): quota del costo di notifica a favore del mittente.
* **refinementDate**: data di perfezionamento per decorrenza termini.
* **notificationViewDate**: data di visualizzazione della notifica da parte di un destinatario.\
  \
  **NOTA sul perfezionamento**: \
  Perfezionamento per decorrenza termini: è valorizzata solo il campo **refinementDate** oppure sono valorizzati entrambi ma **refinementDate** è precedente a **notificationViewDate**.\
  Perfezionamento per presa visione: è valorizzato solo **notificationViewDate**.\
  Casi anomali: a causa di un ritardo nella rendicontazione dell'invio cartaceo da parte del recapitista potrebbe accadere che una notifica in un determinato momento risulti visualizzata (valorizzato solo **notificationViewDate**), successivamente potrebbe restituire una **refinementDate** è precedente a **notificationViewDate**.\
  Per ulteriori dettagli: [https://app.gitbook.com/o/KXYtsf32WSKm6ga638R3/s/8hvzBYw259fYwQSqzmf6/\~/changes/15/knowledge-base-di-piattaforma-notifiche/focus-sul-perfezionamento-della-notifica](../readme/perfezionamento-della-notifica.md)

### Altre modifiche

#### Aggiunto evento di timeline NOTIFICATION\_RADD\_RETRIEVED

Questo nuovo evento di timeline è stato aggiunto per registrare l'accesso alla notifica da uno sportello RADD (Rete di Assorbimento del Divario Digitale). Tale accesso alla notifica non perfeziona la notifica e non modifica lo stato del workflow della notifica.
