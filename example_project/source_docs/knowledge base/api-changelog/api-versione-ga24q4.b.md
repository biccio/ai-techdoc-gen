---
description: Aggiornamento versione ambiente UAT 15/11/2024, produzione 27/11/2024
---

# API VERSIONE GA24Q4.B

## Nuovo elemento SEND\_ANALOG\_PROGRESS per copia conforme AAR

In questa versione, rilasciata in produzione il 27/11/2024, è stato aggiunto l'evento di SEND\_ANALOG\_PROGRESS con `deliveryDetailCode=CON020`.

L'interfaccia delle API rimane invariata in termini di struttura degli eventi, per cui non sono necessari adattamenti al codice client.

Il nuovo elemento in timeline ha lo scopo di veicolare al mittente la copia conforme digitale e firmata da PagoPA in formato PDF della stampa della AAR effettuata dal consolidatore. Questo PDF rispecchia in modo fedele la stampa del foglio inviato che consta nell'AAR al quale il consolidatore aggiunge le informazioni per il recapito in posizione tale da essere visualizzati nella finestrella della busta, i riferimenti del numero di raccomandata e i codici a barre utilizzati nel processo di recapito.

Esempio di evento SEND\_ANALOG\_PROGRESS di tipo CON020.

```json
{
 "iun": "URDQ-EUYE-YMRH-202410-X-1",
 "timelineElementId": "SEND_ANALOG_PROGRESS.IUN_URDQ-EUYE-YMRH-202410-X-1.RECINDEX_0.ATTEMPT_0.IDX_3",
 "category": "SEND_ANALOG_PROGRESS",
 "details": {
  "attachments": [
   {
    "date": "2024-10-21T09:21:20.327062759Z",
    "documentType": "Copia Conforme AAR",
    "id": "0",
    "url": "safestorage://PN_PRINTED-84a63cffbc2b4705ad6d36829836e791.pdf"
   }
  ],
  "deliveryDetailCode": "CON020",
  "nextSourceAttemptsMade": 0,
  "notificationDate": "2024-10-21T09:21:05Z",
  "recIndex": 0,
  "registeredLetterCode": "73d7b51e937941b5a2fbcc3bcc2f4ad8",
  "sendRequestId": "SEND_ANALOG_DOMICILE.IUN_URDQ-EUYE-YMRH-202410-X-1.RECINDEX_0.ATTEMPT_0",
  "serviceLevel": "AR_REGISTERED_LETTER"
 },
 "legalFactId": [
  {
   "category": "ANALOG_DELIVERY",
   "key": "safestorage://PN_PRINTED-84a63cffbc2b4705ad6d36829836e791.pdf"
  }
 ],
 "notificationSentAt": "2024-10-21T09:14:03.834866977Z",
 "paId": "56ed074c-13b6-4d61-ba49-221953e6b60f",
 "statusInfo": {
  "actual": "DELIVERING",
  "statusChanged": false,
  "statusChangeTimestamp": "2024-10-21T09:18:23.858470923Z"
 },
 "timestamp": "2024-10-21T09:21:26.162395956Z"
}
```

Il download della copia conforme può essere effettuato come per gli altri documenti tramite il paramento `key` contenuto nell'elemento `attachments`.

A titolo di esempio si evidenziano le parti aggiunte in fase di stampa.&#x20;

<figure><img src="../.gitbook/assets/CopiaAAR.jpg" alt=""><figcaption><p>Esempio degli elementi aggiunti in fase di stampa</p></figcaption></figure>

## API di stato della piattaforma

Questa versione aggiunge la pubblicazione delle API di:

* stato della piattaforma&#x20;
* recupero dei disservizi e dei relativi atti opponibili

Per i dettagli aprire la pagina [#api-di-stato-della-piattaforma](api-versione-ga24q4.b.md#api-di-stato-della-piattaforma "mention")

## Supporto al bilinguismo

Da questa versione SEND consente di inviare notifiche e atti in doppia lingua (italiano + tedesco, francese o sloveno) per garantire il bilinguismo amministrativo. Le traduzioni sono a cura dell’ente mittente. Sono state predisposte delle FAQ apposite per il seguente tema: [BILINGUISMO](https://developer.pagopa.it/send/guides/knowledge-base/readme/supporto-al-bilinguismo-amministrativo).





####

