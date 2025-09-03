---
description: Configurazione DEFAULT filterValues per stream di eventi di timeline
---

# Stream di timeline

Configurando uno stream senza specificare alcun elemento in filterValues verranno riportati quelli di `DEFAULT`, ovvero quelli che hanno ripercussione sul cambiamento di stato del workflow o che riportano dati di interesse per il mittente, sia di carattere legale (es: legal facts) sia di business (es: numero della raccomandata).

Se oltre a questi eventi si vogliono aggiungere altri di interesse (es: SEND\_COURTESY\_MESSAGE per sapere se sono stati inviati messaggi di cortesia ai destinatari) è sufficiente indicare nel filtro DEFAULT e le categorie di eventi ulteriori.

Questa nuova API espone l'elemento `timestamp` che rappresenta l'istante in cui la piattaforma ha ricevuto l'informazione. Mentre per gli eventi che si verificano all'esterno della piattaforma (es: consegna della raccomandata) la data in cui si è verificata è indicata in un elemento all'interno dell'oggetto details (es: negli eventi della categoria SEND\_ANALOG\_FEEDBACK il timestamp è il momento in cui SEND ha ricevuto l'informazione dell'esito della notifica cartacea, mentre elemento `notificationDate` all'interno dell'oggetto `details`indica la data di consegna della raccomandata).

Nelle tabelle sottostanti sono riportati per ogni categoria di eventi la drescrione, se hanno collegato degli atti a volore legale (LegalFact) e i dettagli di maggior interesse contenuti nell'oggetto `details`.

**NOTA**: le date sono espresse nel formato standard [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), anche detta "Zulu time", che esprime la data UTC (es: 2024-02-29T11:44:17.511990926Z corrisponde alle 12:44:17s del 29/02/2024).

## Eventi di timeline nella configurazione DEFAULT

In questa sezione sono indicati gli eventi di timeline inclusi nella configurazione "DEFAULT" e sono stati suddivisi per fase e tipologia del workflow.

### Eventi di accettazione/rifiuto notifica <a href="#eventi-di-timeline-di-validazione-della-richiesta" id="eventi-di-timeline-di-validazione-della-richiesta"></a>

Gli eventi descritti nella tabella sottostante sono relativi al processo di accettazione della notifica.

**REQUEST\_REFUSED**

Indica che la richiesta di notifica è stata rifiutata per un fallimento in fase di validazione

| details                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>notificationCost</code>: costo in euro-cents della notifica rifiutata per il mittente</li><li><p><code>refusalReasons</code>:</p><ul><li><code>detail</code>: motivo del rifiuta della notifica (<em>es: Validation failed, address is not valid. Error=Invalid Address, Cap, City and Province</em>)</li><li><code>errorCode</code>: codice identificati dell'errore (<em>es: NOT_VALID_ADDRESS</em>)</li></ul></li></ul> |

**REQUEST\_ACCEPTED**

Indica che la richiesta di notifica è stata accettata a seguito dei controlli di validazione

| legalFactsIds                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Attestazione di presa in carico della notifica<br>Con <code>category</code> = "<strong>SENDER_ACK</strong>" e <code>key</code> il riferimento per il download.</p> |

### Eventi del workflow digitale <a href="#eventi-di-timeline-di-scelta-del-workflow-digitale" id="eventi-di-timeline-di-scelta-del-workflow-digitale"></a>

Gli eventi descritti nella tabella sottostante sono relativi al processo del workflow digitale, compreso l'eventuale invio dell'AAR tramite raccomandata semplice.

**SEND\_DIGITAL\_DOMICILE**&#x20;

Indica un tentativo di invio digitale della notifica

| details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><p><code>digitalAddress</code>: indirizzo digitale del destinatario</p><ul><li><code>type</code>: <em>PEC /</em> SERCQ</li><li><code>address</code>: indirizzo PEC / riferimento SERCQ</li></ul></li><li><code>digitalAddressSource</code>: tipologia del domicilio digitale (<em>PLATFORM, SPECIAL, GENERAL</em>)</li><li><code>retryNumber</code>: numero di tentativo (con primo tentativo = 0)</li></ul> |

**SEND\_DIGITAL\_FEEDBACK**

Indica la ricezione di un esito ad un invio a domicilio digitale

<table><thead><tr><th width="763">legalFactsIds</th></tr></thead><tbody><tr><td>Con <code>category</code> = "<strong>PEC_RECEIPT</strong>" e <code>key</code> il riferimento per il download del file in formato EML che attesta la consegna della PEC.</td></tr></tbody></table>

| details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><p><code>digitalAddress</code>:</p><ul><li><code>type</code>: tipo di domicilio digitale (<code>PEC/SERCQ)</code></li><li><code>address</code>: indirizzo domicilio digitale</li></ul></li><li><code>responseStatus</code>: esito dell'invio digitale (<em>es: OK</em>)</li><li><code>notificationDate</code>: data di consegna o mancata consegna.</li><li><code>deliveryFailureCause</code>: Eventuali errori</li><li><code>deliveryDetailCode</code><em>: Codice di consegna</em></li></ul> |



Per i dettagli delle codifiche di `deliveryFailureCause` e `deliveryDetailCode` si rimanda alla pagina [decodifiche-send\_digital.md](decodifiche-send_digital.md "mention").

**DIGITAL\_SUCCESS\_WORKFLOW**

Indica il completamento con successo il workflow di invio digitale.

| legalFactsIds                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Con `category` = "**DIGITAL\_DELIVERY**" e `key`il riferimento per il download dell'attestazione generata alla conclusione dei tentativi di invio sui domicili digitali disponibili, nel caso si siano completati con un evento di consegna |

| details                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><p><code>digitalAddress</code>: indirizzo digitale del destinatario</p><ul><li><code>type</code>: tipo di domicilio digitale (<code>PEC/SERCQ)</code></li><li><code>address</code>: indirizzo domicilio digitale</li></ul></li></ul> |

**DIGITAL\_FAILURE\_WORKFLOW**

Indica il completamento con fallimento il workflow di invio digitale:tutti i tentativi di invio ai domicili digitali sono falliti

| legalFactsIds                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Con `category` = "**DIGITAL\_DELIVERY**" e `key`il riferimento per il download dell'attestazione generata alla conclusione dei tentativi di invio sui domicili digitali disponibili, nel caso si siano completati con una mancata consegna |

| details                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex:</code> indica l'indice dell'array del destinatario per il quale è fallito l'invio digitale</li></ul> |

**SEND\_SIMPLE\_REGISTERED\_LETTER**

Indica l'invio di raccomandata semplice

| details                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><code>analogCost</code>: costo dell’invio cartaceo</li><li><code>physicalAddress</code>: indirizzo fisico della spedizione</li><li><code>productType</code>: "RS"  (Raccomandata Semplice)</li><li><code>analogCost</code>: costo in euro-cents (iva esclusa)</li><li><code>numberOfPages</code>: numero di pagine</li><li><code>envelopeWeight</code>: peso in grammi</li></ul> |

**SEND\_SIMPLE\_REGISTERED\_LETTER\_PROGRESS**

Indica la ricezione di informazioni relative all'invio della raccomandata semplice

| details                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><code>registeredLetterCode</code> : codice della lettera raccomandata</li><li><code>deliveryDetailCode</code>: codice del dettaglio dell'evento di progress</li></ul> |

(\*) Per la decodifica dei codici di `deliveryDetailCode` all'interno dei details degli eventi si rimanda alla pagina [#decodifica-in-send\_analog\_progress](decodifiche-send_analog.md#decodifica-in-send_analog_progress "mention")

### Eventi del workflow Analogico <a href="#eventi-di-timeline-di-scelta-del-workflow-analogico" id="eventi-di-timeline-di-scelta-del-workflow-analogico"></a>

**SEND\_ANALOG\_DOMICILE**

Invio cartaceo dell’avviso di notifica

| details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><code>serviceLevel</code> : servizio richiesto <code>REGISTERED_LETTER_890</code><em><code>/</code></em><code>REGISTERED_LETTER_</code><em><code>AR</code></em></li><li><code>productType</code>:  tipologia del prodotto inviato <em><code>890/AR</code></em></li><li><code>analogCost</code>: costo in euro-cents (iva esclusa)</li><li><code>numberOfPages</code>: numero di pagine</li><li><code>envelopeWeight</code>: peso in grammi</li><li><code>physicalAddress:</code> indirizzo fisico della spedizione</li></ul> |

**SEND\_ANALOG\_FEEDBACK**

Ricezione esito dell'invio cartaceo

| details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>physicalAddress:</code> indirizzo fisico della spedizione</li><li><code>responseStatus:</code> contiene l’esito dell'invio cartaceo <em>(</em><code>OK / KO</code>)</li><li><code>notificationDate</code>: data di consegna o mancata consegna.</li><li><code>registeredLetterCode:</code>codice della lettera raccomandata</li><li><code>deliveryDetailCode:</code>codice del dettaglio esito invio cartaceo</li><li><code>deliveryFailureCause</code>: causa del fallimento della consegna</li><li><code>serviceLevel</code>: tipologia del prodotto inviato (<em>es: 890/AR)</em></li><li><code>newAddress</code>: Eventuale indirizzo fisico a seguito di indagine svolta in loco da parte dell'addetto al recapito postale</li><li><code>sentAttemptMade</code>: numero di tentativo (0 per il primo)</li></ul> |

(\*) Per la decodifica dei codici di e `deliveryFailureCause` e `deliveryDetailCode` all'interno dei details degli eventi di SEND\_ANALOG\_FEEDBACK si rimanda alla pagina [decodifiche-send\_analog.md](decodifiche-send_analog.md "mention")

**ANALOG\_SUCCESS\_WORKFLOW**

Completato con successo il workflow di invio cartaceo.

| details                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><code>physicalAddress:</code> indirizzo fisico della spedizione</li></ul> |

**ANALOG\_FAILURE\_WORKFLOW**

Completato con fallimento il workflow di invio cartaceo.

| details                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><code>generatedAarUrl</code>: deposito della AAR</li></ul> |

**COMPLETELY\_UNREACHABLE**

Il destinatario è risultato irraggiungibile.

| Attachments                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Con `category` = "**ANALOG\_FAILURE\_DELIVERY**" e `key` riferimento per il download del documento di Deposito dell'avviso di avvenuta ricezione (deposito AAR) sulla piattaforma |

| details                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><code>legalFactGenerationDate</code>: data di generazione del documento di deposito AAR </li></ul> |

### Eventi di chiusura del workflow <a href="#eventi-di-timeline-di-chiusura-del-workflow" id="eventi-di-timeline-di-chiusura-del-workflow"></a>

**REFINEMENT**

Perfezionamento per decorrenza termini

| details                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><code>notificationCost:</code> costo della notifica rifiutata per il mittente</li><li><code>eventTimestamp:</code> indica la data di perfezionamento della notifica per decorrenza termini</li></ul> |

**NOTIFICATION\_VIEWED**

Visualizzazione della notifica (perfeziona la notifica se non già perfezionata per decorrenza termini o da altro destinatario)

| attachments                                                                  |
| ---------------------------------------------------------------------------- |
| <p><strong>RECIPIENT_ACCESS</strong><br>Attestazione di avvenuto accesso</p> |

| details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><code>notificationCost:</code> costo di gestione della notifica per il mittente espresso in euro-cents</li><li><code>eventTimestamp:</code> data di visualizzazione della notifica</li><li><p><code>delegateInfo</code>: struttura che contiene le informazione dell'eventuale delegato che ha fatto accesso alla notifica.</p><ul><li><code>taxId</code>: codice fiscale del delegato</li><li><code>denomination</code>: denominazione delegato</li><li><code>delegateType</code>: tipologia delegato PF/PG</li></ul></li></ul> |

**NOTIFICATION\_CANCELLED**

Evento di fine della cancellazione della notifica dal parte del mittente.

| details                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ |
| <ul><li><code>notificationCost:</code> costo di gestione della notifica per il mittente espresso in euro-cents</li></ul> |

#### RETURNED\_TO\_SENDER

Resa al mittente per destinatario dichiarato deceduto

### Altri eventi di timeline <a href="#altre-eventi-di-timeline" id="altre-eventi-di-timeline"></a>

**NOTIFICATION\_RADD\_RETRIEVED**

Evento di accesso alla notifica tramite RADD

| details                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><code>eventTimestamp</code>: data di consegna della notifica</li><li><code>raddType</code>: tipologia soggetto RADD</li><li><code>raddTransactionId</code>: identificativo della transazione RADD</li></ul> |

#### ANALOG\_WORKFLOW\_RECIPIENT\_DECEASED

Evento per destinatario deceduto

| details                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex</code>: posizione del destinatario nell'array recipients</li><li><code>eventTimestamp</code>: data di consegna della notifica</li><li><code>notificationCost</code>: costo della notifica</li><li><code>physicalAddress</code>: indirizzo fisico del destinatario</li></ul> |

## **Eventi aggiuntivi al DEFAULT**

In questo paragrafo sono indicati altri eventi della timeline che non hanno effetto sullo stato della notifica e non hanno una importanza prioritaria per il mittente, ma possono essere interessanti per recuperare delle informazioni di dettaglio. Ricordiamo che questi dati sono mantenuti dalla piattaforma in modo sicuro per 10 anni e sono sempre disponibili per essere recuperati tramite le API.

### Eventi di preparazione workflow <a href="#eventi-di-timeline-di-preparazione-workflow" id="eventi-di-timeline-di-preparazione-workflow"></a>

**AAR\_GENERATION**

Generazione dell’AAR (Avviso di Avvenuta Ricezione)

| details                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex:</code> posizione del destinatario nell'array recipients</li><li><code>generatedAarUrl</code>: url per accedere all'avviso di avvenuta ricezione</li></ul> |

**SEND\_COURTESY\_MESSAGE**

Invio di un messaggio di cortesia.

| details                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex:</code> posizione del destinatario nell'array recipients</li><li><p><code>digitalAddress</code></p><ul><li><code>type</code>: tipologia messaggio di OPT_IN o un messaggio su APPIO, EMAIL o SMS</li><li><code>address</code>: indirizzo email o numero di telefono utilizzato per il messaggio.</li></ul></li></ul> |

**PROBABLE\_SCHEDULING\_ANALOG\_DATE**

Indica che il workflow può essere sospeso per 120h a fronte di un invio di un messaggio di cortesia.

| details                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex:</code> posizione del destinatario nell'array recipients</li><li><code>schedulingAnalogDate</code>: data di inizio del workflow analogico, ritardato a causa di invio di messaggi di cortesia.</li></ul> |

### Eventi di scelta del workflow

**PUBLIC\_REGISTRY\_RESPONSE**

Indica la ricezione di un domicilio digitale dai registri nazionali

| details                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <ul><li><code>recIndex:</code> posizione del destinatario nell'array recipients</li><li><p><code>digitalAddress</code>: indirizzo digitale del destinatario</p><ul><li><code>type</code>: tipo domicilio digitale</li><li><code>address</code>: indirizzo domicilio digitale</li></ul></li></ul> |

### Eventi con evidenze dell'invio

Gli eventi di PROGRESS sono eventi restituiti dai servizi esterni di invio digitale (SEND\_DIGITAL\_PROGRESS) e cartaceo (SEND\_ANALOG\_PROGRESS).

Questi eventi possono contenere anche dei legalFact esterni come il messaggio di consegna della PEC (in formato EML) nel caso di invio digitale o le scansioni della ricevuta di consegna, del plico, del avviso di ricevimento, dell'indagine del postino nel caso di invio di raccomandata.

**SEND\_DIGITAL\_PROGRESS**

Indica un evento successivo relativo all'invio della PEC.

| Attachments                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- |
| Con `category` = "**PEC\_RECEIPT**" e `key` il riferimento per il download del file in formato EML che attesta l'accettazione della PEC. |

| details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex:</code> posizione del destinatario nell'array recipients</li><li><code>eventTimestamp</code>: data e ora della accettazione</li><li><code>digitalAddress:</code> indirizzo digitale del destinatario</li><li><code>digitalAddressSource</code>: indica la tipologia di domicilio digitale (PLATFORM, SPECIAL, GENERAL)</li><li><code>retryNumber</code>: numero tentativo (0 per il primo)</li><li><code>deliveryDetailCode</code>: vedi <a data-mention href="decodifiche-send_analog.md">decodifiche-send_analog.md</a></li></ul> |

**SEND\_ANALOG\_PROGRESS**

Indica un evento successivo relativo all'invio cartaceo

| attachments                                        |                    |                                                                                                                           |
| -------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **deliveryDetailCode**                             | **documentType**   | Descrizione                                                                                                               |
| `CON018`                                           | AAR                | Accettazione Recapitista - L’evento rappresenta l’accettazione della Distinta di presa in carico da parte del Recapitista |
| `CON020`                                           | Copia Conforme AAR | Copia conforme all'originale dell'avviso di avvenuta ricezione (AAR)                                                      |
| `RECRN001B`                                        | AR                 | Ricevuta di consegna                                                                                                      |
| `RECRN002B`, `RECRN004B`, `RECRN002E`, `RECRN005B` | Plico              | Scansione Plico                                                                                                           |
| `RECRN003B`                                        | AR                 | Avviso di ricevimento                                                                                                     |
| `RECRN002E`                                        | Indagine           | Indagine in loco dell'addetto al recapito (questa spesso è inclusa nella Scansione del                                    |

| details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li><code>recIndex:</code> posizione del destinatario nell'array recipients</li><li><code>notificationDate</code>: data evento</li><li><code>deliveryDetailCode</code>: codice consegna (*)</li><li><code>serviceLevel</code>: tipologia di servizio</li><li><code>registeredLetterCode</code>: identificativo raccomandata</li><li><p><code>attachments</code>: array dei documenti allegati con struttura </p><ul><li><code>id</code>: indice nell'array</li><li><code>documentType</code>: tipo documento</li><li><code>url</code>: identificativo per il download</li><li><code>date</code>: data produzione documento</li></ul></li></ul> |

**PREPARE\_ANALOG\_DOMICILE\_FAILURE**

Invio cartaceo non possibile: non è stato trovato nessun indirizzo valido per predisporre il tentativo.

| details                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><code>failureCause :</code> indica il motivo del fallimento del secondo invio tramite i codici</p><ul><li><code>D00</code>: Non è stato trovato nessun nuovo indirizzo per predisporre un altro tentativo di invio.</li><li><code>D01</code>: L’indirizzo non ha superato il processo di validazione.</li><li><code>D02</code>: L’indirizzo è già stato usato per effettuare un tentativo di invio.</li></ul> |

(\*) Per la decodifica dei codici di `deliveryDetailCode` all'interno dei details degli eventi di SEND\_ANALOG\_PROGRESS si rimanda alla pagina&#x20;
