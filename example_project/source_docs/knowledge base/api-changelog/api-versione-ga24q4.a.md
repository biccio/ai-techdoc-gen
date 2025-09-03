---
description: Aggiornamento in produzione 28/10/2024
---

# API VERSIONE GA24Q4.A

### Nuove funzionalità GA24Q4.A

Con l'obiettivo di rendere al mittente più semplice il calcolo del rispetto degli SLA, è stata creata la versione **stream v2.4** che arricchisce i precedenti elementi di timeline con ulteriori dati.

#### Campi aggiunti

In ogni elemento di timeline sono stati aggiunti i seguenti campi:

* **`ingestionTimestamp`**: Istante in cui l'evento è registrato sulla timeline da SEND.
* **`eventTimestamp`**: Istante in cui avviene l'evento descritto in questo elemento di timeline.
* **`notificationSentAt`**: Istante del deposito della notifica da parte del mittente (dal quale vengono calcolate le SLA).

**NOTA**: il campo `timestamp` è rimasto per retrocompabilità ma è deprecato e non deve essere utilizzato.

Le modifiche agli elementi di timeline si applicano sulle seguenti API:

#### <kbd>**Dettagli della notifica**</kbd>

#### [**/delivery/v2.4/notifications/sent/{iun}**](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fmain%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa-bundle.yaml#/SenderReadB2B/retrieveSentNotificationV24)&#x20;

#### **Gestione degli stream** _di eventi che PN mette a disposizione_

Gli stream creati con la versione versione 2.4 (POST **`delivery-progresses/v2.4/streams/{streamId}`** )possono essere letti o modificati con le relative versioni 2.4:

* **`delivery-progresses/v2.4/streams`** Elenca stream di eventi
* GET **`delivery-progresses/v2.4/streams/{streamId}`** Leggi metadata dello stream
* PUT **`delivery-progresses/v2.4/streams/{streamId}`** Modifica di uno Stream
* DELETE **`delivery-progresses/v2.4/streams/{streamId}`** Elimina uno Stream
* **`delivery-progresses/v2.4/streams/{streamId}/action/disable`** Disabilita uno stream
* **`/delivery-progresses/v2.4/streams/{streamId}/events`** Leggi progressi notifiche













