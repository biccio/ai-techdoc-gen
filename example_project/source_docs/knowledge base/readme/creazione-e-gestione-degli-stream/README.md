---
description: >-
  Informazioni utili sui passi da seguire per creare, configurare e consumare
  correttamente una stream
---

# Creazione e gestione degli stream

Lo stream permette di raccogliere tutti gli eventi emessi dalle notifiche che vengono inserite dalla PA a seguito della sua creazione; lo stream può immagazzinare un massimo di 50 eventi per volta, raggiunto questo limite la PA deve consumare lo stream per poter visualizzare gli altri eventi successivi.

Il campo `eventType` può essere valorizzato in 2 modi:

* **STATUS:** permette di registrare gli eventi di cambiamento di stato delle notifiche
* **TIMELINE:** permette di registrare gli eventi di timeline delle notifiche.

il campo `filterValues` può contenere il tipo di eventi che si vogliono filtrare all'interno dello stream, se lasciato vuoto `[]` permetterà di raccogliere tutti gli eventi emessi.

È possibile sapere se sono presenti altri eventi da visualizzare tramite il valore del parametro `retry-after`presente nell'header del body della response ottenuta a seguito della prima chiamata a questo servizio:&#x20;

* se`retry-after = 0` significa che sono presenti altri eventi oltre a quelli ricevuti nella response; per ottenere i successivi è necessario consumare i precedenti, effettuando una nuova chiamata a questo servizio, nella quale valorizzare il campo `lastEventId` con l'eventId dell'ultimo evento ottenuto nella precedente chiamata.
* se`retry-after` ≠ `0` significa che non sono presenti altri eventi nello stream oltre a quelli appena ottenuti, pertanto è necessario attendere la quantità di tempo (espressa in millisecondi) del valore restituito, prima di richiamare di nuovo il servizio

_"Consumare gli eventi"_ consiste nella loro eliminazione dallo stream per liberare lo spazio agli eventi successivi; quindi per conservarli è necessario che la PA li persista sulla propria base dati.

Ogni PA può configurare un massimo di 5 stream, nel caso si voglia modificare la configurazione di uno stream è necessario cancellarlo e crearne uno nuovo con la configurazione desiderata.

Se la PA non consuma gli eventi, questi vengono eliminati <mark style="color:red;">**dopo 7 giorni dalla loro creazione**</mark> (non tutti gli eventi, ma solo quelli creati da più di 7 giorni); a questo punto l'unico modo per poter recuperare quelli eventi è chiamare l’api [retrieveSentNotification](https://petstore.swagger.io/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpagopa%2Fpn-delivery%2Fdevelop%2Fdocs%2Fopenapi%2Fapi-external-b2b-pa.yaml#/SenderReadB2B/retrieveSentNotification) che restituisce tutti gli eventi di timeline di una determinata notifica. Questo processo al contrario dell'utilizzo degli stream, non è ottimizzato perchè costringe la PA ad effettuare N chiamate per ogni notifica inserita; pertanto si consiglia di utilizzare sempre gli stream in ambiente di produzione.
