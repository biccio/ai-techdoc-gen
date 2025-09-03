# Invio notifiche tramite API B2B

I servizi di SEND offrono API di inoltro notifiche.&#x20;

L’inoltro si effettua in due fasi: nella prima fase si effettua l’upload degli allegati (atti, modelli di pagamento ed eventuali metadati), nella seconda fase si procede all’inoltro della richiesta di invio della notifica, fornendo tutte le informazioni necessarie, inclusi i riferimenti ai documenti precedentemente caricati in piattaforma e la loro hash SHA-256 calcolata dalla PA mittente ed utilizzata da SEND per confermare il contenuto del file allegato.&#x20;

Se le informazioni fornite per la notifica sono sintatticamente corrette, SEND restituisce un identificativo temporaneo che verrà utilizzato per trasmettere alla PA l’esito delle ulteriori e successive verifiche.&#x20;

A questo punto SEND verifica che tutti i file siano disponibili, abbiano formato PDF (firmati digitalmente) o JSON conforme allo schema (per i metadati dei modelli di pagamento F24). Verifica inoltre la validità dei CF prodotti dalla PA e dell’esistenza di un indirizzo fisico per ciascun destinatario e che siano utilizzabili come indirizzi per il recapito.&#x20;

Qualora l’operazione di verifica abbia successo, viene generato lo IUN (Identificativo Univoco della Notifica) che viene restituito alla PA assieme all’identificativo temporaneo precedentemente generato.

In caso contrario verrà inviato, assieme all’identificativo temporaneo, un codice di errore che indica il motivo del fallimento della verifica e il dettaglio dell'anomalia rilevata.&#x20;

Dal momento della creazione con successo di una notifica, la PA riceverà aggiornamenti sullo stato della stessa attraverso un meccanismo di stream intelligente fornito da SEND. Ciascun aggiornamento di stato conterrà lo IUN della notifica alla quale si riferisce.

## Notifiche con pagamenti

SEND permette di notificare atti a cui possono essere collegati dei pagamenti. Le modalità di pagamento supportate sono:  pagoPA e modelli F24.&#x20;

Per i pagamento tramite pagoPA il mittente può allegare il bollettino in formato PDF/A e i dati: Codice Fiscale ente creditore e numero avviso. Tramite questi dati il destinatario sarà in grado di effettuare il pagamento direttamente dal portale SEND e dall'app IO.

Per i pagamento tramite modello F24 il mittente dovrà fornire i metadati degli elementi compenenti il modello e SEND renderà disponibile al destinatario il file PDF con eventuale aggiunta dei costi di notifica sulla voce indicata dal mittente.
