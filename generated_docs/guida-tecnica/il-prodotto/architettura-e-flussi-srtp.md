---
related_topics:
- /guida-tecnica/api-standard-epc-srtp
- /tutorial/how-to-send-a-payment-request
function: "il-prodotto"
level: "intermediate"
product:
  name: "PagoPA SRTP"
  version: "v1.0.0"
schema:
  '@context': https://schema.org
  '@type': TechArticle
  name: "Architettura e Flussi Asincroni del PagoPA SEPA Request-to-Pay (SRTP)"
  description: "Una spiegazione concettuale del modello a quattro parti (Four-Corner Model), dei flussi asincroni e dei messaggi standard ISO 20022 utilizzati nel servizio PagoPA SRTP."
  keywords:
  - "SRTP"
  - "Architettura"
  - "Four-Corner Model"
  - "ISO 20022"
  - "Flusso Asincrono"
status: "published"
technology:
- "SRTP"
- "Four-Corner Model"
- "ISO 20022"
- "pain.013"
- "pain.014"
- "Callback"
user:
  role: "provider"
  tag:
  - "architettura"
  - "flusso asincrono"
  - "iso 20022"
---

# Architettura e Flussi Asincroni SRTP

Questo documento fornisce una spiegazione concettuale delle specifiche tecniche per l'integrazione con i servizi PagoPA per l'invio e la ricezione di notifiche di pagamento tramite lo schema SEPA Request-To-Pay (SRTP). Si rivolge agli sviluppatori e agli architetti software che necessitano di comprendere il funzionamento del sistema.

## Architettura: Il Modello a Quattro Parti

Il flusso SRTP si basa su un modello a quattro parti (Four-Corner Model) che disaccoppia il Creditore dal Debitore tramite i rispettivi Service Provider. Questo modello garantisce l'interoperabilità e la standardizzazione delle comunicazioni tra tutti gli attori dell'ecosistema.

mermaid
sequenceDiagram
    autonumber
    participant C as Creditore (Ente)
    participant CSP as Creditor Service Provider
    participant PPA as Piattaforma PagoPA
    participant DSP as Debtor Service Provider
    participant D as Debitore (Cittadino)

    C->>+CSP: Invia richiesta di pagamento
    CSP->>+PPA: Inoltra richiesta SRTP (pain.013)
    PPA->>+DSP: Inoltra richiesta SRTP
    DSP->>+D: Notifica richiesta di pagamento su app
    D-->>-DSP: Autorizza o rifiuta il pagamento
    DSP-->>-PPA: Invia esito (pain.014) via callback
    PPA-->>-CSP: Notifica esito al Creditor SP
    CSP-->>-C: Notifica esito al Creditore


- **Creditor (Payee)**: L'Ente Creditore che emette un avviso di pagamento PagoPA.
- **Creditor Service Provider (Payee's SP)**: L'intermediario tecnologico del Creditore, che si interfaccia con la piattaforma PagoPA per inviare la richiesta SRTP.
- **Debtor Service Provider (Payer's SP)**: L'intermediario tecnologico del Debitore (es. la banca), che riceve la richiesta SRTP e la presenta all'utente finale per l'approvazione.
- **Debtor (Payer)**: Il cittadino/utente finale che riceve la notifica di pagamento e autorizza la transazione.

## Flusso Asincrono tramite Callback

Una caratteristica fondamentale del servizio è la sua natura asincrona. Dopo che il Creditor SP ha inviato una richiesta di pagamento (`pain.013`), la risposta con l'esito non è immediata. Il Debtor SP, una volta ottenuto il consenso (o il diniego) dal Debitore, invierà una notifica di stato (`pain.014`) a un endpoint di callback. Questo approccio garantisce la resilienza del sistema e gestisce in modo efficiente le latenze del processo di autorizzazione utente.

## Formati dei Messaggi ISO 20022

L'interoperabilità è garantita dall'uso di messaggi standard ISO 20022, veicolati in formato JSON all'interno delle chiamate API.

### `pain.013.001.07` - Creditor Payment Activation Request

Questo messaggio è utilizzato per avviare il processo di pagamento. Viene inviato dal Creditor SP e contiene tutte le informazioni necessarie per identificare la transazione e il Debitore.

- **Scopo**: Iniziare una richiesta di pagamento SRTP.
- **Contenuto Chiave**: Dettagli del Creditore, del Debitore, importo, causale e riferimenti all'avviso di pagamento PagoPA.
- **Flusso**: `Creditor SP` -> `Debtor SP`

### `pain.014.001.07` - Creditor Payment Activation Request Status Report

Questo messaggio è utilizzato per comunicare l'esito finale della richiesta di pagamento.

- **Scopo**: Fornire una risposta definitiva (positiva o negativa) alla richiesta `pain.013`.
- **Contenuto Chiave**: Riferimento alla richiesta originale, codice di stato (es. `ACSC` - AcceptedSettlementCompleted, o `RJCT` - Rejected) e motivazione dell'eventuale rifiuto.
- **Flusso**: `Debtor SP` -> `Creditor SP` (via callback)

## Integrazione con l'Avviso di Pagamento PagoPA

La richiesta SRTP (`pain.013`) deve contenere i riferimenti univoci all'avviso di pagamento PagoPA (es. `notice code` e `creditor tax code`). Questo legame garantisce che il pagamento avviato tramite SRTP riconcili correttamente la posizione debitoria originale all'interno della piattaforma PagoPA.