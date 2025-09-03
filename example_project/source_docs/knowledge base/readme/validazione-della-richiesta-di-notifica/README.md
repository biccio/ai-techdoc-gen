---
description: >-
  Approfondimento sulla validazione che PND effettua sulle richieste di  invio
  Notifica
---

# Validazione della Richiesta di Notifica

In fase di inserimento di una Richiesta di invio Notifica, Piattaforma Notifiche effettua 2 diversi tipi di validazione per assicurarsi che le informazioni inserite siano corrette e congruenti: la **Validazione Sincrona** e la **Validazione Asincrona.**

### Validazione Sincrona

Nel momento stesso in cui si chiama il servizio di Richiesta di invio Notifica vengono effettuate delle verifiche formali sui campi inseriti: il dettaglio dei controlli applicati per ogni campo è documentato nel seguente file Swagger:[ ](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fmain%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa-bundle.yaml#/NewNotification/sendNewNotificationV23)[https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fmain%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa-bundle.yaml#/NewNotification/sendNewNotificationV23](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fmain%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa-bundle.yaml#/NewNotification/sendNewNotificationV23)\
Se la `request` inviata supera tutti i controlli, il servizio restituisce una `response` con Status: **202 Accepted** e con body contenente: **notificationRequestId, paProtocolNumber** e **idempotenceToken** che sono i riferimenti per poter verificare l'esito dei controlli asincroni che verranno effettuati da questo momento in poi.

### Validazione Asicrona

Dopo aver inserito con successo una Richiesta di invio Notifica ed aver ottenuto i riferimenti della stessa, Piattaforma Notifiche avvierà le seguenti verifiche:

* Verifica che gli SHA-256 forniti dal Mittente coincidano con quelli calcolati da PN a partire dai documenti allegati
* Verifica che il versionToken e la key di ogni allegato inserito all'interno della notifica corrispondano a quelli collegati agli allegati caricati precedentemente in fase di upload \
  (vedi 1.a e 1.b:[ ](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fmain%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa-bundle.yaml#/NewNotification/sendNewNotificationV23)[https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fmain%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa-bundle.yaml#/NewNotification/sendNewNotificationV23](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fmain%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa-bundle.yaml#/NewNotification/sendNewNotificationV23))
* Verifica con normalizzatore degli indirizzi di POSTEL che l'indirizzo fisico associato a ciascun destinatario sia idoneo all'invio postale. \
  **NOTA:** in fase di **validazione sincrona**, il CAP della notifica non è obbligatorio; questo comportamento è stato previsto per permettere l’inserimento di indirizzi esteri, per i quali il CAP potrebbe seguire regole diverse da quelle italiane. Per gli indirizzi italiani invece tale campo è obbligatorio e se non presente la notifica passerà in _REFUSED._
* Verifica della validità dei metadati F24 tramite (vedi json schema [https://raw.githubusercontent.com/pagopa/pn-f24/main/docs/openapi/json-schema-from-deref-mod.json](https://raw.githubusercontent.com/pagopa/pn-f24/main/docs/openapi/json-schema-from-deref-mod.json))

I controlli asincroni sulla Richiesta di invio Notifica producono sempre un esito entro 24H dall'inserimento. L'esito dei controlli asincroni può essere verificato con l'apposito servizio [Verifica accettazione richiesta notifica](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fdevelop%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa.yaml#/SenderReadB2B/retrieveNotificationRequestStatus) o consumando il relativo evento di Timeline; in entrambi i casi sarà possibile ottenere il codice **IUN** identificativo della Notifica e verrà avviato il processo di Notifica.
