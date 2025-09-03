# Il processo di notificazione

Il processo di notificazione inizia con la PA mittente che richiede a Piattaforma Notifiche (PN) di prendere in carico l’effettuazione di una notifica.

Questa operazione avviene in tre fasi: caricamento dei documenti, creazione della notifica, verifica dei dati forniti.

Nella prima fase, la PA fornisce a PN gli atti da notificare unitamente agli avvisi pagoPA, se previsto il pagamento da parte del destinatario.

Nella seconda fase, la PA genera la richiesta di creazione della notifica, fornendo i seguenti dati (sono indicati con l'asterisco \* quelli obbligatori):



*   per ogni destinatario:

    * Codice Fiscale\*
    * l'indicazione del tipo di persona fisica o giuridica\*
    * nome e cognome o ragione sociale\*
    * indirizzo fisico di ogni destinatario del domicilio noto alla PA\*
    * domicilio digitale speciale eventualmente eletto
    * Codice Avviso e Codice Fiscale dell’Ente creditore relativi all’avviso pagoPA
    * numero di protocollo\*
    * oggetto della notifica\*
    * descrizione estesa della notifica
    * codice tassonomico\*
    * la modalità da adottare per l’eventuale spedizione analogica (890/AR)\*
    * importo e data di scadenza del pagamento (a soli fini informativi per il mittente)
    * lista dei documenti facenti parte della notifica (attraverso gli identificativi forniti da PN nella precedente fase) e l'hash SHA-256 dei documenti stessi\*

    PN ricevute queste informazioni, verifica che siano sintatticamente corrette e che non ci siano stati utilizzati combinazioni di numero di protocollo (paProtocolNumber)/identificativo univoco generato dal sistema di integrazione del mittente (IdempotenceToken) oppure Codice Avviso/Codice Fiscale dell’Ente creditore già utilizzati in altre notifiche non annullate. Nel caso in cui le verifiche abbiano successo restituisce al mittente un token (notificationRequestId) che servirà, in alternativa all'utilizzo degli stream, alla PA stessa per ricevere l’esito delle successive attività di verifica poste in atto da PN.

La piattaforma permette di inserire molteplici avvisi di pagamento (es. per gestire le rate della TARI), dando la possibilità al destinatario di selezionare l'avviso/i per i quali vuole procedere al pagamento.\
Per il caso d'uso relativo alle sanzioni al codice della strada saranno inserite, per ciascun destinatario, le due coppie di Codice Avviso e Codice Fiscale dell’Ente creditore contenti l'avviso che deve essere pagato entro 5 giorni dalla data di perfezionamento della notifica e quello che contiene l'avviso che deve esser pagato passati i 5 giorni e comunque entro i 60 giorni dal perfezionamento. Il destinatario vedrà entrambi i pagamenti disponibili e sceglierà quale pagare.

Nella terza ed ultima fase, PN verifica che lo SHA-256 fornito dalla PA coincida con quello calcolato da PN a partire dai documenti allegati. PN effettua inoltre un'attività di verifica e normalizzazione dell'indirizzo fisico fornito per ciascun destinatario allo scopo di garantire la possibilità di notificare al destinatario in forma cartacea. L'indirizzo originale fornito dalla PA mittente verrà riportato nelle attestazioni opponibili ai terzi mentre verrà utilizzato l'indirizzo normalizzato per l'avvio in postalizzazione. Nel caso in cui l'indirizzo fisico fornito dalla PA mittente non sia postalizzabile la notifica verrà rifiutata. Se le verifiche hanno successo, PN genera lo IUN che viene restituito alla PA mittente unitamente al token (notificationRequestId) generato all’atto di creazione della notifica.&#x20;

La generazione dello IUN, conclude il processo di deposito/creazione della notifica su PN e perfeziona la notifica per la PA mittente. Nel caso in cui, invece, le verifiche non abbiano successo, PN informa la PA della presenza di errori nella richiesta inoltrata inviando un codice di errore unitamente al token  (notificationRequestId) generato all’atto di creazione della notifica.

I documenti allegati devono essere in formato PDF e conformi a quanto richiesto dagli articoli 20 e 21 del CAD, perciò firmati digitalmente dalla PA mittente. I documenti trasmessi dalla PA mittente vengono conservati per 120 giorni a partire dalla data di perfezionamento della notifica per il destinatario. PN genera un’attestazione opponibile ai terzi contenenti le informazioni relative alla data e all’ora di ricezione della richiesta di creazione della notifica da parte del mittente ed agli indirizzi forniti dal mittente per raggiungere il destinatario. La messa a disposizione di questa attestazione conferma l’inizio delle operazioni di notificazione.

Nel caso in cui la PA mittente non sia in grado di determinare se un Codice Fiscale appartenga ad una persona fisica o ad una persona giuridica, si suggerisce di assumere che il Codice Fiscale appartenga alla persona fisica.

<figure><img src="../../.gitbook/assets/image (120).png" alt=""><figcaption></figcaption></figure>

Una volta che una notifica è stata correttamente creata dalla PA mittente, PN genera un documento denominato Avviso di Avvenuta Ricezione (AAR) che contiene le informazioni relative all’esistenza della notifica, il suo IUN e le indicazioni sulle modalità che il destinatario può utilizzare per accedere agli atti notificati e depositati in piattaforma. PN a questo punto verifica se è possibile effettuare la notificazione attraverso canali digitali. Questo è possibile se la PA mittente ha fornito un domicilio digitale (speciale), oppure se esiste negli archivi di PN un domicilio digitale (di piattaforma) collegato al destinatario oppure, infine, se è possibile reperire un domicilio digitale (generale) nei registri pubblici (IniPEC, IPA, INAD). Nel caso in cui i registri pubblici restituiscano più di un domicilio digitale riconducibile al destinatario PN utilizzerà solamente il primo indirizzo restituito.

Se non è possibile determinare alcun domicilio digitale, la notificazione avverrà attraverso il canale analogico.

In entrambi i casi, se il destinatario ha configurato su PN un indirizzo e-mail o l’abilitazione su app IO per gli avvisi di cortesia di PN, o un numero di cellulare al quale inviare SMS), verrà generato un Avviso di cortesia non a valore legale, che permette al destinatario di accedere e prendere visione della notifica e dei relativi allegati anche prima di aver ricevuto la notifica attraverso i canali di comunicazione a valore legale (domicilio digitale o 890/AR).

L’Avviso di cortesia viene inviato su tutti i recapiti disponibili.

Nel caso sia stato possibile inviare l’Avviso di cortesia ad un cittadino da raggiungere con notificazione analogica, la notificazione viene ritardata di 5 giorni (120 ore) per permettere eventualmente al cittadino di accedere alla notifica su PN e perfezionare di conseguenza la stessa. In questo caso la spedizione dell’AAR cartaceo non avviene ed il cittadino ne risparmia i costi.

Il destinatario può accedere agli atti notificati ed alle relative attestazioni opponibili a terzi con le seguenti modalità:

* accedendo al portale di PN, utilizzando la propria identità digitale e selezionando la notifica in base al relativo IUN e quindi accedendo agli atti oggetto di notifica scaricabili sul portale. Il destinatario ha inoltre la possibilità di accedere alle attestazioni opponibili ai terzi attraverso i singoli link presenti nella sezione "Stato della notifica".
* attraverso l’app IO, nel caso sia stata abilitata la ricezione degli avvisi di cortesia di PN. Selezionando il messaggio si accede al dettaglio della singola notifica che permette di accedere agli atti notificati e, nella sezione "Stato della notifica" alle relative attestazioni opponibili ai terzi;
* utilizzando il link di accesso rapido presente nell’AAR, al dettaglio della singola notifica che permette di accedere agli atti notificati e, nella sezione "Stato della notifica", alle relative attestazioni opponibili ai terzi;
* per il tramite di una persona a ciò delegata dal destinatario, previa ogni opportuna attività di delega tramite la specifica funzione sul portale di PN;
* con le modalità descritte per l’accesso a PN tramite i servizi RADD (Rete Assorbimento Digital Divide), messi a disposizione per i destinatari in digital divide.

(\*) NB Si invita la PA (nelle procedure interne precedenti al caricamento degli atti sulla Piattaforma) al rispetto della normativa vigente in materia di protocollazione, compresa l'indicazione della segnatura di protocollo.
