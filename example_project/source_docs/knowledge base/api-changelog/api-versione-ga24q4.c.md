---
description: Aggiornamento versione ambiente UAT 23/01/2025 , produzione 10/02/2025
---

# API VERSIONE GA24Q4.C

### Nuove funzionalità GA24Q4.C

* **Codici Tassonomici:** Introdotta la validazione dei codici tassonomici attraverso una lista predefinita, con controllo generico e senza modifiche alle API esistenti.
* **Mancata Consegna per Decesso:** Modificato il workflow per generare un nuovo stato finale della notifica invece del perfezionamento automatico dopo 10 giorni.

## Codici Tassonomici

Il codice tassonomico, finora registrato come una semplice stringa senza controlli, sarà validato rispetto alla seguente lista di codici tassonomici: [https://developer.pagopa.it/send/guides/knowledge-base/tassonomia-send](https://developer.pagopa.it/send/guides/knowledge-base/tassonomia-send). Il controllo non sarà specifico per ogni ente, ma applicato in modo generico. Le API esistenti resteranno invariate, mantenendo il codice come stringa e consentendo una configurazione dinamica dei codici validi senza modifiche alla definizione OpenAPI.



## Resa al mittente per destinatario dichiarato deceduto

Nel processo di notificazione analogica, SEND perfezionava la notifica 10 giorni dopo aver ricevuto dal recapitista l'evento di mancata consegna a causa del decesso del destinatario. Con la modifica introdotta, il workflow è stato aggiornato: invece di concludersi con il perfezionamento della notifica, il processo ora genera un nuovo stato finale della notifica, adattandosi alla gestione specifica di questa casistica.

Questo nuovo stato finale, denominato **RETURNED\_TO\_SENDER**, indicherà la "resa al mittente per destinatario dichiarato deceduto" e sarà accompagnato da un nuovo elemento nella timeline, **ANALOG\_WORKFLOW\_RECIPIENT\_DECEASED**.

È importante sottolineare che l'acquisizione del dato relativo al decesso, necessaria per la definizione di questo nuovo stato, avviene tramite SEND senza che vengano effettuate verifiche sui registri anagrafici. Questa modalità tutela la piattaforma da dichiarazioni errate o inveritiere da parte del recapitista.

#### Retro-compatibilità con utilizzo della API precedenti

Per mantenere la retro-compatibilità con le API precedenti si è optato per una soluzione che non riporta il nuovo stato **RETURNED\_TO\_SENDER**  e non riporta sulla timeline il nuovo evento **ANALOG\_WORKFLOW\_RECIPIENT\_DECEASED**.

La notifica prima dell’attivazione di questa funzionalità si perfezionava per decorrenza termini, mentre ora rimane in stato DELIVERING.

Chiamando le API di dettagli della notifica delle versioni precedenti alla **/delivery/v2.6/requests** si può verificare comunque la restituzione della mancata consegna per destinatario deceduto verificando l’elemento di **SEND\_ANALOG\_FEEDBACK** con la deliveryFailureCause=”M02”.

Esempio:

```json
"notificationStatusHistory": [
  {
   "status": "ACCEPTED",
   "activeFrom": "2025-01-08T14:07:18.78682696Z",
   "relatedTimelineElements": [
     …   
   ]
  },
  {
   "status": "DELIVERING",
   "activeFrom": "2025-01-08T14:13:04.153778659Z",
   "relatedTimelineElements": [
      …
    ]
  }
],
…
{
  "elementId": "SEND_ANALOG_FEEDBACK.IUN_DPDA-LVZM-JREL-202501-N-1.RECINDEX_0.ATTEMPT_0",
  "timestamp": "2025-01-08T14:15:25Z",
  "ingestionTimestamp": "2025-01-08T14:15:28.044726415Z",
  "eventTimestamp": "2025-01-08T14:15:25Z",
  "notificationSentAt": "2025-01-08T14:07:18.78682696Z",
  "category": "SEND_ANALOG_FEEDBACK",
  "details": {
     "recIndex": 0,
     "physicalAddress": {
          …
      },
      "sentAttemptMade": 0,
      "responseStatus": "OK",
      "notificationDate": "2025-01-08T14:15:25Z",
      "deliveryFailureCause": "M02",
      "deliveryDetailCode": "RECAG003C",
      "serviceLevel": "REGISTERED_LETTER_890",
      "registeredLetterCode": "08837543a362465da814595b8e8fa5a0"
  }
}
```

Analogamente gli stream delle versioni precedenti la v2.5 **/delivery-progresses/v2.5/streams/{streamId}/events** verranno esclusi lo stato **RETURNED\_TO\_SENDER** (per gli stream di status) e l’evento **ANALOG\_WORKFLOW\_RECIPIENT\_DECEASED** per gli stream di tipo eventi di timeline.

Esempio:

```json
{
        "eventId": "00000000000000000000000000000000000033",
        "notificationRequestId": "RFBEQS1MVlpNLUpSRUwtMjAyNTAxLU4tMQ==",
        "iun": "DPDA-LVZM-JREL-202501-N-1",
        "newStatus": "DELIVERING",
        "element": {
            "elementId": "SEND_ANALOG_FEEDBACK.IUN_DPDA-LVZM-JREL-202501-N-1.RECINDEX_0.ATTEMPT_0",
            "timestamp": "2025-01-08T14:15:25Z",
            "ingestionTimestamp": "2025-01-08T14:15:28.044726415Z",
            "eventTimestamp": "2025-01-08T14:15:25Z",
            "notificationSentAt": "2025-01-08T14:07:18.786826960Z",
            "category": "SEND_ANALOG_FEEDBACK",
            "details": {
                "recIndex": 0,
                "physicalAddress": {
      …
                },
                "sentAttemptMade": 0,
                "responseStatus": "OK",
                "notificationDate": "2025-01-08T14:15:25Z",
                "deliveryFailureCause": "M02",
                "deliveryDetailCode": "RECAG003C",
                "serviceLevel": "REGISTERED_LETTER_890",
                "sendRequestId": "SEND_ANALOG_DOMICILE.IUN_DPDA-LVZM-JREL-202501-N-1.RECINDEX_0.ATTEMPT_0",
                "registeredLetterCode": "08837543a362465da814595b8e8fa5a0"
            }
        }
    },
```

#### Utilizzo della API nuove

Utilizzando la nuova versione delle API /delivery/v2.6/requests per ottenere il dettaglio della notifica si otterrà nello stato della notifica il nuovo **RETURNED\_TO\_SENDER**  e l’evento **ANALOG\_WORKFLOW\_RECIPIENT\_DECEASED** nella timeline.

<pre class="language-json" data-full-width="false"><code class="lang-json">"notificationStatusHistory": [
  {
   "status": "ACCEPTED",
   "activeFrom": "2025-01-08T14:07:18.78682696Z",
   "relatedTimelineElements": [
     …   
   ]
  },
  {
   "status": "DELIVERING",
   "activeFrom": "2025-01-08T14:13:04.153778659Z",
   "relatedTimelineElements": [
      …
    ]
  }
  {
   "status": "RETURNED_TO_SENDER",
   "activeFrom": "2025-01-08T14:15:25Z",
   "relatedTimelineElements": [
     …
   ]
<strong>  }
</strong>    …
  {
  "elementId": "SEND_ANALOG_FEEDBACK.IUN_DPDA-LVZM-JREL-202501-N-1.RECINDEX_0.ATTEMPT_0",
  "timestamp": "2025-01-08T14:15:25Z",
  "ingestionTimestamp": "2025-01-08T14:15:28.044726415Z",
  "eventTimestamp": "2025-01-08T14:15:25Z",
  "notificationSentAt": "2025-01-08T14:07:18.78682696Z",
  "legalFactsIds": [],
  "category": "SEND_ANALOG_FEEDBACK",
  "details": {
     "recIndex": 0,
     "physicalAddress": {
        …
      },
      "sentAttemptMade": 0,
      "responseStatus": "OK",
      "notificationDate": "2025-01-08T14:15:25Z",
      "deliveryFailureCause": "M02",
      "deliveryDetailCode": "RECAG003C",
      "serviceLevel": "REGISTERED_LETTER_890",
      "sendRequestId": "SEND_ANALOG_DOMICILE.IUN_DPDA-LVZM-JREL-202501-N-1.RECINDEX_0.ATTEMPT_0",
      "registeredLetterCode": "08837543a362465da814595b8e8fa5a0"
  }
},
{
  "elementId": "ANALOG_WORKFLOW_RECIPIENT_DECEASED.IUN_DPDA-LVZM-JREL-202501-N-1.RECINDEX_0",
  "timestamp": "2025-01-08T14:15:25Z",
  "ingestionTimestamp": "2025-01-08T14:15:30.846053255Z",
  "eventTimestamp": "2025-01-08T14:15:25Z",
  "notificationSentAt": "2025-01-08T14:07:18.78682696Z",
  "legalFactsIds": [],
  "category": "ANALOG_WORKFLOW_RECIPIENT_DECEASED",
  "details": {
     "recIndex": 0,
     "physicalAddress": {
…
     },
   "notificationCost": 100,
   "notificationDate": "2025-01-08T14:15:25Z"
}
</code></pre>
