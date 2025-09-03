---
related_topics:
- /il-prodotto/architettura-e-flussi-srtp
function: "guida-tecnica"
level: "advanced"
product:
  name: "PagoPA SRTP"
  version: "v1.0.0"
schema:
  '@context': https://schema.org
  '@type': WebAPI
  name: "Standard EPC SRTP API"
  description: "Specifica di riferimento basata sullo standard EPC133-22 v3.1 per l'interazione tra Creditor SP e Debtor SP nell'ecosistema SEPA Request-to-Pay."
  keywords:
  - "EPC"
  - "standard"
  - "API"
  - "interoperabilità"
  - "SRTP"
status: "published"
technology:
- "REST"
- "OAuth2"
- "EPC133-22"
- "HATEOAS"
- "JSON"
- "ISO 20022"
user:
  role: "provider"
  tag:
  - "epc"
  - "standard"
  - "api"
  - "interoperabilità"
---

# API Standard EPC per SEPA Request-to-Pay

Questa specifica API RESTful è l'implementazione di riferimento dello standard ufficiale `EPC133-22 v3.1` definito dallo European Payment Council (EPC). Definisce le interfacce per l'interazione tra il Service Provider del Creditore (Payee SP) e il Service Provider del Pagatore (Payer SP) per lo scambio di messaggi SEPA Request-to-Pay. L'aderenza a questa specifica garantisce l'interoperabilità tra i diversi attori dell'ecosistema.

## Authentication

Tutte le chiamate a questa API devono essere autenticate tramite il flusso OAuth2 Client Credentials. È necessario includere un token JWT valido nell'header `Authorization` della richiesta, utilizzando lo schema `Bearer`.

`Authorization: Bearer <YOUR_JWT_TOKEN>`

## Endpoints

### POST /sepa-request-to-pay-requests

Inoltra una nuova richiesta di pagamento (incapsulando un messaggio `pain.013`) dal Creditor SP al Debtor SP. La risposta a questa chiamata contiene un `sepaRequestToPayRequestResourceId` per tracciare la richiesta in modo univoco.

### GET /sepa-request-to-pay-requests/{sepaRequestToPayRequestResourceId}

Recupera lo stato corrente e i dettagli di una richiesta SRTP esistente. La risposta dell'API utilizza principi HATEOAS per fornire link auto-descrittivi ad azioni successive o risorse correlate.

### POST /sepa-request-to-pay-requests/{sepaRequestToPayRequestResourceId}/status-update

Invia un aggiornamento di stato (incapsulando un messaggio `pain.014`) relativo a una richiesta SRTP. È il meccanismo standard con cui il Debtor SP notifica al Creditor SP l'esito dell'interazione con l'utente finale (pagamento eseguito, rifiutato, scaduto, etc.).