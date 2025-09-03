---
related_topics:
- /tutorial/how-to-send-a-status-response
function: "guida-tecnica"
level: "intermediate"
product:
  name: "PagoPA SRTP"
  version: "v1.0.0"
schema:
  '@context': https://schema.org
  '@type': WebAPI
  name: "Callback Service API"
  description: "Specifica l'interfaccia che un Creditor Service Provider deve esporre per ricevere notifiche di stato asincrone (pain.014) dal Debtor Service Provider."
  keywords:
  - "callback"
  - "API"
  - "pain.014"
  - "notifica stato"
status: "published"
technology:
- "REST"
- "Callback"
- "JSON"
- "pain.014"
- "Digital Signature"
user:
  role: "service_provider_creditor"
  tag:
  - "callback"
  - "api"
  - "notifica stato"
  - "pain.014"
---

# API del Servizio di Callback

Questa specifica descrive l'interfaccia che un Service Provider del Creditore (Creditor SP) deve esporre per ricevere notifiche asincrone di stato dal Service Provider del Pagatore (Debtor SP).

L'URL di questo endpoint viene fornito dinamicamente dal Creditor SP all'interno del messaggio di richiesta di pagamento originale (`pain.013`). Il Debtor SP invocherà questo URL per comunicare l'esito finale della transazione.

## Sicurezza

A differenza di altre API, questo endpoint non è protetto da OAuth2. L'autenticità e l'integrità della notifica sono garantite dalla validazione della firma digitale contenuta all'interno del messaggio `pain.014` ricevuto.

## Endpoint

L'API espone un singolo endpoint per la ricezione delle risposte.

### POST /send

Accetta una notifica di stato relativa a una richiesta SRTP precedentemente inviata.

- **Scopo**: Ricevere il messaggio `pain.014` (Creditor Payment Activation Request Status Report) che indica l'accettazione (`ACSC`), il rifiuto (`RJCT`) o un altro stato terminale della transazione.

- **Corpo della Richiesta**: Il payload della richiesta è un oggetto JSON che incapsula il messaggio `pain.014` standard ISO 20022. L'implementazione del Creditor SP **deve** validare la firma e il contenuto del messaggio per garantire autenticità e integrità.