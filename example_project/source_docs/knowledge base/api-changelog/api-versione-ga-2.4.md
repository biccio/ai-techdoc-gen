---
description: Steam V2.4
---

# API VERSIONE GA 2.4

## **Nuove funzionalità GA 2.4**

La versione GA 2.4 aggiunge una nuova API per gli stream degli eventi del workflow della notifiche.

* Segregazione degli stream per gruppi
* Esposizione dettagli degli eventi di timeline
* Configurazione default del filtro degli eventi di timeline
* Disabilitazione di uno stream
* Migrazione degli stream alla nuova versione

File di definizione OpenAPI [https://raw.githubusercontent.com/pagopa/pn-delivery/v2.5.0/docs/openapi/api-external-b2b-pa-bundle.yaml](https://raw.githubusercontent.com/pagopa/pn-delivery/v2.5.0/docs/openapi/api-external-b2b-pa-bundle.yaml)

### Segregazione degli stream per gruppi&#x20;

Gli stream della versione GA2.4 possono essere associati ad uno o più gruppi, in modo da realizzare una segregazione tra gli eventi delle notifiche che appartengono solo ai gruppi specificati.

I gruppi specificati in fase di creazione/aggiornamento, devono essere tra quelli che l'api-key può gestire. In caso non si voglia inserire nessun gruppo in fase di creazione dello stream, tutte le informazioni saranno disponibile solo alle api-key che non sono associate ad alcun gruppo.

Ugualmente la lettura di uno stream collegato ad uno o più gruppi è possibile solo ad api-key associate a tutti i gruppi a cui è associato lo stream. Mentre l'api-key non associata ad alcun gruppo può gestire stream e leggere da stream associati a qualsiasi gruppo.

Questa modifica permette ad un ente mittente che ha partner tecnologici su ambiti differenti (es: contravvenzione per violazioni del codice della strada e sollecito tributi) di creare api-key, stream e notifiche associate ai rispettivi gruppi in modo che non sia possibile ad in partner tecnologico di creare, leggere, cancellare, disabilitare gli stream dell'altro. Oltre ad ottenere il vantaggio di ricevere gli eventi delle sole notifiche di suo interesse (associate allo stesso gruppo dello stream).

### Esposizione dettagli degli eventi di timeline

&#x20;La nuova API arricchisce gli eventi di timeline con i dettagli. Dalla lettura dello stream si ottengono tutte le informazioni contenuti nell'elemento di timeline della notifica, in questo modo è possibile eliminare la chiamata ai dettagli della notifica per ottenere queste informazioni.&#x20;

Per i dettagli si rimanda alla pagina [stream-di-timeline](../readme/creazione-e-gestione-degli-stream/stream-di-timeline/ "mention")

### Configurazione default del filtro degli eventi di timeline&#x20;

Per aiutare gli enti nella configurazione del filtro sui numerosi eventi di timeline è stato definito un filtro DEFAULT che contiene tutti gli elementi di principale interesse per il mittente.

Per i dettagli si rimanda alla pagina [stream-di-timeline](../readme/creazione-e-gestione-degli-stream/stream-di-timeline/ "mention")

### Disabilitazione di uno stream

La disabilitazione dello stream è un'operazione che permette il mittente di migrare da uno stream ad un altro senza perdere eventi. Lo stream disabilitato non riceve più eventi ma continua ad essere disponibile per la lettura di quelli già presenti. Quando tutti gli eventi dello stream disabilitato sono stati letti lo stream può essere cancellato con la sicurezza di non aver perso eventi.

Sullo stream disabilita non sono possibili operazioni oltre alla lettura degli eventi presenti.

Lo stream viene automaticamente rimosso dopo 14 giorni dalla sua disabilitazione.

### Migrazione degli stream alla nuova versione

La creazione di uno stream della nuova API prevede un campo per indicare lo stream che va a sostituire. Quest'ultimo viene disabilitato appena creato lo stream nuovo quindi è possibile eseguire una migrazione alla nuova API senza perdita di eventi.
