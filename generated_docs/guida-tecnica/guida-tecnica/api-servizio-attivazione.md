---
related_topics:
- /il-prodotto/architettura-e-flussi-srtp
function: "guida-tecnica"
level: "intermediate"
product:
  name: "PagoPA SRTP"
  version: "v1.0.0"
schema:
  '@context': https://schema.org
  '@type': WebAPI
  name: "Activation Service API"
  description: "Descrive gli endpoint REST per la gestione del ciclo di vita delle attivazioni SEPA Request-to-Pay (SRTP), un processo avviato dal Debtor Service Provider."
  keywords:
  - "attivazione"
  - "API"
  - "OAuth2"
  - "SRTP"
status: "published"
technology:
- "REST"
- "OAuth2"
- "JWT"
- "JSON"
user:
  role: "service_provider_debtor"
  tag:
  - "attivazione"
  - "api"
  - "oauth2"
---

# API del Servizio di Attivazione

Questa API RESTful gestisce il ciclo di vita delle attivazioni SEPA Request-to-Pay (SRTP). L'attivazione è un processo avviato dal Service Provider del Pagatore (Debtor Service Provider) per registrare il consenso del proprio utente a ricevere richieste di pagamento.

## Authentication

Tutte le chiamate a questa API devono essere autenticate tramite il flusso OAuth2 Client Credentials. È necessario includere un token JWT valido nell'header `Authorization` della richiesta, utilizzando lo schema `Bearer`.

`Authorization: Bearer <YOUR_JWT_TOKEN>`

## Endpoints

### POST /activations

Crea una nuova richiesta di attivazione SRTP. Il corpo della richiesta contiene i dati identificativi del debitore e le condizioni dell'attivazione.

### GET /activations

Recupera un elenco delle attivazioni esistenti. L'API supporta filtri e paginazione per permettere una gestione efficiente di grandi volumi di dati.

### GET /activations/{activationId}

Ottiene i dettagli completi di una specifica attivazione, identificata tramite il suo `activationId` univoco. Questo endpoint è utile per verificare lo stato corrente di un'attivazione.

### PUT /activations/{activationId}

Aggiorna lo stato di un'attivazione esistente. Questa operazione è tipicamente utilizzata per confermare, sospendere o revocare un'attivazione a seguito di un'azione esplicita dell'utente.