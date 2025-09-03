---
related_topics:
- /docs/guida-tecnica/api-del-servizio-di-attivazione
- /docs/tutorial/how-to-initiate-an-activation
function: "il-prodotto"
level: "beginner"
product:
  name: "PagoPA SRTP"
  version: "v1.0.0"
schema:
  '@context': https://schema.org
  '@type': TechArticle
  name: "Understanding the SEPA Request-to-Pay (SRTP) Scheme in PagoPA"
  description: "An explanation of the SRTP conceptual framework, including the Four-Corner Model, the lifecycle of a request, and a detailed look at the service activation flow."
  keywords:
  - "SRTP"
  - "SEPA Request to Pay"
  - "Four-Corner Model"
  - "Activation"
  - "pain.013"
  - "pain.014"
status: "published"
technology:
- "SEPA"
- "SRTP"
- "pain.013"
- "pain.014"
user:
  role: "all"
  tag:
  - "srtp"
  - "overview"
  - "architecture"
  - "activation"
  - "four-corner model"
---

# Lo Schema SEPA Request-to-Pay (SRTP)

Lo schema SEPA Request to Pay (SRTP), definito dall'European Payment Council (EPC), standardizza lo scambio di messaggi per avviare un pagamento. Non è un meccanismo di pagamento in sé, ma un livello di messaggistica che opera in concerto con schemi di pagamento esistenti, in particolare con il SEPA Instant Credit Transfer (SCT Inst).

L'obiettivo primario dell'SRTP è di consentire a un beneficiario (Creditor) di inviare una richiesta di pagamento direttamente a un pagatore (Debtor) in formato digitale, che quest'ultimo può approvare o rifiutare tramite il proprio ambiente di pagamento (es. app di mobile banking).

## Il Modello a Quattro Corner

L'SRTP si basa su un'architettura di interoperabilità nota come "modello a quattro corner", che disaccoppia il beneficiario dal pagatore tramite i rispettivi Service Provider.

Gli attori di questo modello sono:

1.  **Creditor (Beneficiario):** L'entità che deve ricevere il pagamento. Nel contesto di PagoPA, è l'Ente Creditore (es. un Comune, un'Agenzia Fiscale).
2.  **Creditor Service Provider (CSP):** L'intermediario tecnologico che agisce per conto del Creditor, inviando le richieste di pagamento SRTP.
3.  **Debtor Service Provider (DSP):** L'intermediario tecnologico che agisce per conto del Debtor, ricevendo le richieste SRTP e presentandole all'utente per l'approvazione. Tipicamente, è la banca o l'istituto di pagamento del Debtor.
4.  **Debtor (Pagatore):** La persona fisica o giuridica che deve effettuare il pagamento. Nel contesto di PagoPA, è il Cittadino o l'Impresa.

mermaid
graph LR
    C(Creditor) -- Richiesta --> CSP(Creditor Service Provider)
    CSP -- Messaggio SRTP --> DSP(Debtor Service Provider)
    DSP -- Notifica --> D(Debtor)
    D -- Accetta/Rifiuta --> DSP
    DSP -- Risposta SRTP --> CSP
    CSP -- Esito --> C


## Il Ruolo di PagoPA

PagoPA agisce come orchestratore centrale e garante dell'interoperabilità all'interno di questo modello per i pagamenti verso la Pubblica Amministrazione. La piattaforma gestisce il registro dei Service Provider, instrada i messaggi tra CSP e DSP, e governa i processi di consenso e attivazione del servizio, assicurando che le comunicazioni avvengano in modo standardizzato e sicuro.

## Ciclo di Vita di una Richiesta SRTP

Il processo SRTP si articola in fasi distinte:

1.  **Attivazione (Activation):** Una fase preliminare in cui il Debtor autorizza esplicitamente il proprio DSP a ricevere richieste SRTP da un determinato Creditor. Questo processo di consenso è fondamentale e deve essere completato prima che qualsiasi richiesta di pagamento possa essere inviata.
2.  **Invio Richiesta di Pagamento:** Il CSP invia un messaggio `pain.013` (CreditorPaymentActivationRequest) al DSP tramite la piattaforma PagoPA. Questo messaggio contiene tutti i dettagli per il pagamento, inclusi importo, causale e IBAN del beneficiario.
3.  **Interazione con il Debtor:** Il DSP notifica la richiesta al Debtor sul suo canale preferito (es. notifica push sull'app). Il Debtor può visualizzare i dettagli e scegliere di accettare o rifiutare la richiesta.
4.  **Esecuzione del Pagamento:** In caso di accettazione, il DSP avvia un pagamento SCT Inst verso il Creditor.
5.  **Rendicontazione dello Stato:** Il DSP comunica l'esito della richiesta (accettata, rifiutata, scaduta) al CSP tramite un messaggio `pain.014` (PaymentStatusReport), chiudendo il ciclo.

## Approfondimento: Il Flusso di Attivazione

L'attivazione del servizio SRTP è un prerequisito fondamentale che precede qualsiasi transazione di pagamento. Questo processo stabilisce un accordo trilaterale tra il Cittadino (Debtor), l'Ente Creditore (Creditor) e il Service Provider del Debitore (DSP), orchestrato da PagoPA. Durante l'attivazione, il Cittadino fornisce il consenso esplicito a ricevere richieste di pagamento da un specifico Ente Creditore tramite il DSP prescelto.

### Diagramma del Flusso

Il diagramma seguente illustra la sequenza di interazioni tra i vari attori per completare l'attivazione del servizio. Il flusso è avviato dal Cittadino all'interno dell'ambiente sicuro del proprio DSP (es. l'app della propria banca) e coinvolge una redirezione verso la piattaforma PagoPA per la raccolta del consenso formale.

mermaid
sequenceDiagram
    autonumber

    participant C as Cittadino
    participant App as App del DSP
    participant DSP as Service Provider Debitore
    participant PPA as Piattaforma PagoPA
    participant CSP as Service Provider Creditore
    participant EC as Ente Creditore

    Note over EC, PPA: Prerequisito: L'Ente Creditore ha fornito a PagoPA il consenso per operare in SRTP.

    C->>App: Avvia l'attivazione SRTP per un Ente Creditore
    App->>DSP: Inoltra richiesta di attivazione (dati utente, codice fiscale EC)
    DSP->>PPA: Chiama POST /activations
    PPA-->>DSP: Risponde 201 Created (activationId, consentUrl)
    DSP-->>App: Restituisce il consentUrl
    App->>C: Redirect del Cittadino al consentUrl di PagoPA
    
    activate C
    C->>PPA: Si autentica (SPID/CIE) e fornisce il consenso
    deactivate C

    PPA->>PPA: Memorizza il consenso e lo stato dell'attivazione
    PPA-->>DSP: Invia notifica di callback asincrona (attivazione completata)
    DSP->>DSP: Aggiorna stato attivazione a 'COMPLETED'
    DSP-->>App: Notifica l'esito positivo dell'attivazione
    App->>C: Mostra conferma di avvenuta attivazione


### Fasi Dettagliate

1.  **Inizializzazione (Passi 1-2):** Il Cittadino, all'interno dell'applicazione del proprio Service Provider (DSP), esprime l'intenzione di attivare il servizio SRTP per un determinato Ente Creditore, identificato tramite Codice Fiscale.

2.  **Creazione dell'Attivazione (Passo 3):** Il sistema backend del DSP invoca l'endpoint `POST /activations` esposto da PagoPA. La richiesta contiene l'identificativo dell'Ente Creditore e le informazioni relative al Cittadino.

3.  **Ottenimento URL di Consenso (Passi 4-5):** PagoPA crea una risorsa di attivazione in stato `PENDING` e restituisce un `activationId` univoco e un `consentUrl`. Quest'ultimo è un URL sicuro e temporaneo che punta a una pagina di consenso gestita da PagoPA.

4.  **Raccolta del Consenso Utente (Passi 6-7):** L'applicazione del DSP reindirizza il Cittadino al `consentUrl`. Su questa pagina, il Cittadino si autentica con un'identità digitale forte (SPID/CIE) e visualizza i dettagli del consenso che sta per fornire. Una volta confermato, il consenso viene registrato in modo sicuro dalla piattaforma PagoPA.

5.  **Notifica Asincrona (Passi 8-12):** A seguito del consenso, PagoPA aggiorna lo stato dell'attivazione e notifica il DSP tramite una chiamata di callback asincrona. Questo design disaccoppiato è robusto e adatto a gestire processi che richiedono l'interazione dell'utente. Ricevuta la callback, il DSP finalizza l'attivazione e informa il Cittadino che il servizio è ora attivo e pronto per ricevere richieste di pagamento.
