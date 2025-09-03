# API di stato della Piattaforma

## API di stato della piattaforma

La piattaforma SEND offre una serie di API che permettono agli utenti autorizzati di monitorare lo stato dei servizi e consultare lo storico dei disservizi. Queste API permettono anche di scaricare atti opponibili a terzi per i disservizi risolti, garantendo la trasparenza e la tracciabilità delle interruzioni dei servizi.

Il file di definizione openAPI è esposto all'indirizzo [https://raw.githubusercontent.com/pagopa/pn-downtime-logs/refs/tags/pn-openapi-devportal/docs/openapi/api-external-v1.yaml](https://raw.githubusercontent.com/pagopa/pn-downtime-logs/refs/tags/pn-openapi-devportal/docs/openapi/api-external-v1.yaml)

### Funzionalità principali

Le API della piattaforma SEND sono progettate per:

1. **Verifica dello stato dei servizi**: verifica in tempo reale della presenza di disservizi attivi sulla piattaforma SEND.
2. **Consultazione dello storico dei disservizi**: consultazione dell'elenco dei disservizi risolti in un determinato periodo e con riferimento agli atti opponibili a terzi associati a ciascun disservizio.
3. **Scaricamento atti opponibili a terzi**: Per i disservizi risolti, è possibile ottenere e scaricare gli atti opponibili a terzi che documentano l'evento.

NOTA: Gli atti opponibili a terzi sono generati solo per disservizi che sono stati risolti e riportano la data di inizio e di fine del disservizio.

### Descrizione delle API

Le API fornite dalla piattaforma SEND possono essere suddivise in tre principali categorie, ognuna dedicata a una funzione specifica:

#### API per lo Stato di SEND

Queste API consentono di verificare lo stato attuale della piattaforma SEND, e se ci sono problemi o disservizi in corso.

* Verifica lo stato della piattaforma\
  operationId: `status`\
  path: `/status`\
  \
  Utilizzando questa API, è possibile sapere se la piattaforma SEND sta funzionando correttamente o se ci sono disservizi in corso. Se tutto è operativo, viene restituita una conferma che elenca i servizi attivi. Se invece ci sono disservizi, l'API fornisce un elenco dei componenti che presentano un disservizio corrente:
  * NOTIFICATION\_CREATE: la possibilità di creare nuove notifiche.
  * NOTIFICATION\_VISUALIZATION: la possibilità di visualizzare le notifiche e scaricare gli atti.
  * NOTIFICATION\_WORKFLOW: l'avanzamento del processo di notifica.

#### API per il Recupero dei Disservizi Risolti

Queste API permettono di consultare lo storico dei disservizi risolti e di scaricare gli atti opponibili a terzi, documenti ufficiali che attestano l'interruzione del servizio.

*   Recupera la lista dei disservizi risolti\
    operationId: `getResolved`&#x20;

    path: `/downtime/v1/resolved`\
    \
    Recupera l'elenco dei disservizi che sono stati risolti in un determinato periodo, come ad esempio in un mese o in un anno specifico. Per ciascun disservizio risolto, viene fornito un identificativo unico che permette di recuperare ulteriori dettagli sull'atto opponibile a terzi.
*   Ottieni dettagli sull'atto opponibile\
    operationId: `getLegalFact`

    path: `/downtime/v1/legal-facts/{legalFactId}`\
    \
    Per ogni disservizio risolto, è possibile ottenere ulteriori informazioni sull'atto opponibile a terzi che documenta il disservizio. In caso l'atto sia già disponibile, l'utente può scaricarlo direttamente. Se l'atto non è ancora pronto, l'API fornirà una stima del tempo di attesa per il suo recupero.
