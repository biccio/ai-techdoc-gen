# Invio manuale di una notifica

L’invio manuale di una notifica si effettua premendo il tasto “Invia una nuova notifica" presente nella pagina di accesso "Notifiche".

<figure><img src="../../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

La pagina "Invia una nuova notifica" prevede 5 sezioni di compilazione: informazioni preliminari, destinatario/i, posizione debitoria, dettagli posizione debitoria e allegati.



<figure><img src="../../../.gitbook/assets/Screenshot 2025-03-27 at 10.27.40.png" alt=""><figcaption></figcaption></figure>

### Prima sezione "Informazioni preliminari"

I campi obbligatori sono:&#x20;

* il _nome della PA mittente_ (precompilato)
* il _numero di protocollo_ della notifica (potrebbe essere quello dell’Ufficio Protocollo della PA o comunque un identificativo della pratica oggetto della notifica)
* l’_oggetto_ della notifica
* il _codice tassonomico:_ identifica il contenuto della notifica in base alla tassonomia dei servizi (rif: [https://developer.pagopa.it/send/guides/knowledge-base/tassonomia-send](https://developer.pagopa.it/send/guides/knowledge-base/tassonomia-send))
* _Modalità di invio cartaceo:_ la tipologia di servizio dell'eventuale invio cartaceo (raccomandato 890 o A/R)

ATTENZIONE: Nel caso l’operatore faccia parte di uno o più gruppi (vedi Configurazione gruppi) il relativo campo diventa obbligatorio.  Se invece l'operatore non appartiene a nessun gruppo, l'inserimento non è obbligatorio.

La _descrizione_ riferita all’oggetto è un campo facoltativo e, come tale liberamente valorizzabile dalla PA mittente con ulteriori dettagli che saranno visualizzati al destinatario dopo l'avvenuto accesso.

E' possibile selezionare l'invio di un atto in formati bi-lingua. Notifiche, comunicazioni e atti opponibili a terzi saranno ricevuti in due lingue: Italiano e una da selezionare tra le opzioni disponibili (Tedesco, Sloveno e Francese). Rimangono a carico del mittente la compilazione in doppia lingua dei campi descrittivi della notifica (come oggetto e descrizione) e il caricamento degli allegati con il testo bi-lingue.

L’inserimento dei dati richiesti abilita il tasto “Continua” per salvare e le informazioni inserite e passare alla sezione successiva.

Abbandonando la sezione senza aver premuto il tasto "Continua" le informazioni fino a quel momento inserite non verranno salvate.

Attenzione: da una qualunque delle cinque sezioni previste per la creazione di una nuova notifica, premendo il tasto in alto a sx "Indietro", l'operatore verrà riportato alla pagina di accesso a PN "Notifiche" e le informazioni inserite nelle sezioni non verranno salvate.

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### Seconda sezione "Destinatari"

Questo modulo prevede i seguenti campi obbligatori per ciascuno dei destinatari previsti: individuazione del soggetto giuridico destinatario (persona fisica/persona giuridica), nome, cognome, codice fiscale (anche per le persone giuridiche), indirizzo fisico del destinatario.&#x20;

Il domicilio digitale del destinatario, al contrario dell'indirizzo fisico, è un campo facoltativo.

Se la notifica riguarda più destinatari (Destinatari multipli), le informazioni richieste devono essere riportate per ciascuno di essi cliccando su “Aggiungi un destinatario”. E' possibile inserire un massimo di 5 destinatari sulla stessa notifica.

L’inserimento dei dati richiesti abilita il tasto “Continua” per passare alla sezione successiva.

Abbandonando la sezione senza aver premuto il tasto "Continua" le informazioni fino a quel momento inserite non verranno salvate.

Premendo il tasto "Torna a informazioni preliminari" l'operatore sarà riportato alla sezione precedente.

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### Terza Sezione "Posizione debitoria"

La terza sezione prevede la scelta della posizione debitoria da aggiungere. La scelta è tra quattro opzioni: avviso pagoPA, modello F24, entrambi e nessun pagamento. Nel caso in cui la scelta sia "Nessun pagamento" si procederà direttamente alla quinta sezione.

Selezionando uno dei pagamenti, si abiliterà il tasto "Continua" e sarà possibile procedere inserendo le informazioni riguardanti quest'ultimo.

<figure><img src="../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

### Quarta Sezione "Dettaglio posizione debitoria"

Nella quarta sezione si inseriranno le informazioni relative al pagamento.

Nel primo campo si selezionerà il costo di notifica che può essere di due tipologie: forfettario (già incluso nell'atto) e puntuale (a carico del destinatario).&#x20;

Selezionando il costo "puntuale" si attiveranno due aree:

* _Iva:_ Gestione IVA sui costi di invio cartaceo espressa in percentuale;
* _Costo Notifica_: quota del costo di notifica a favore dei mittenti espressa in euro.

É prevista una faq in riferimento a questo punto: [https://developer.pagopa.it/send/guides/knowledge-base/readme/pagamenti-e-spese-di-notifica](https://developer.pagopa.it/send/guides/knowledge-base/readme/pagamenti-e-spese-di-notifica).

Proseguendo con il secondo campo (non presente in caso di scelta F24), si dovrà scegliere in base alla propria integrazione con il sistema pagoPA.&#x20;

* _Sincrona_: la posizione debitoria è gestita dall'ente creditore (EC).&#x20;
* _Asincrona_: la posizione debitoria è stata caricata sul sistema Gestione Posizione Debitorie (GPD) di pagoPA.

Di seguito si riporta la faq di approfondimento sul tema: [https://developer.pagopa.it/send/guides/knowledge-base/readme/pagamenti-e-spese-di-notifica/pagamenti-pagopa](https://developer.pagopa.it/send/guides/knowledge-base/readme/pagamenti-e-spese-di-notifica/pagamenti-pagopa).

Nell'ultimo campo per l'avviso pagoPa è previsto l'inserimento obbligatorio del Codice di Avviso e il Codice Fiscale dell'ente creditore e se previsto l'allegato. Invece per l'F24 sarà necessario caricare il file in [formato JSON](https://raw.githubusercontent.com/pagopa/pn-f24/main/docs/openapi/json-schema-from-deref-mod.json) e inserire il nome del file.

Se la notifica prevede più pagamenti, per ognuno di essi le informazioni richieste devono essere riportate cliccando su “+ Aggiungi codice di avviso pagoPA/Modello F24”.

Compilando correttamente la posizione debitoria si abiliterà il tasto "Continua" e sarà possibile procedere all'ultima sezione.

<figure><img src="../../../.gitbook/assets/image (7).png" alt=""><figcaption><p>F24</p></figcaption></figure>

### Quinta Sezione "Documenti Allegati"

La quinta e ultima sezione prevede il caricamento in allegato di almeno un atto in formato PDF/A e firmato digitalmente dalla PA mittente, eventualmente contenente anche l’avviso di pagamento pagoPA (se non è stato già inserito nella sezione dei pagamenti).

La PA può allegare più atti nel caso in cui essi siano separati su file distinti, per un massimo di 10 allegati per notifica (atto + massimo 10 allegati).

Una volta allegati i file, verranno presentati all’utente le hash SHA-256 dei documenti che verranno inoltrate a PN per verifica (vedi I[l processo di notificazione](../../il-processo-di-notificazione/)) .

L’inserimento dei dati richiesti abilita il tasto “Invia” per completare la sessione di creazione della richiesta di notifica.

Abbandonando la sezione senza aver premuto il tasto "Invia" le informazioni fino a quel momento inserite non verranno salvate.

Premendo il tasto "Torna al dettaglio posizione debitoria" l'operatore sarà riportato alla sezione precedente.

<figure><img src="../../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

La richiesta di notifica viene sottoposta ad un processo di validazione che normalmente richiede qualche minuto al termine del quale, se non sono stati riscontrati errori, SEND visualizzerà la notifica, ed il relativo Identificativo Univoco della Notifica (IUN)  nella lista di notifiche inviate visibile nella pagina di accesso "Notifiche". Nel caso in cui la creazione non vada a buon fine, la relativa notifica non sarà presente in elenco.&#x20;

A questo punto l’operatore può visualizzare l'avanzamento del processo di notificazione nella pagina di accesso "Notifiche".

<figure><img src="../../../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>
