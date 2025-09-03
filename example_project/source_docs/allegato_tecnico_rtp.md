# Sorgente di Contenuto: Integrazione SEPA Request-To-Pay (SRTP) su PagoPA

[cite_start]Questo documento funge da fonte di contenuto grezzo per la generazione della documentazione tecnica relativa all'integrazione dei Service Provider con i servizi PagoPA per l'invio e la ricezione di notifiche di pagamento tramite lo schema SEPA Request-To-Pay (SRTP). 

---

## 1. Panoramica del Prodotto

### 1.1. Scopo e Introduzione

[cite_start]Lo scopo di questa documentazione è fornire le specifiche tecniche per l'integrazione dei Service Provider ai servizi PagoPA per l'invio e la ricezione di notifiche di pagamento di avvisi pagoPA tramite l'utilizzo dello schema SEPA Request-To-Pay (SRTP). 

### 1.2. Lo Schema SEPA Request-To-Pay (SRTP)

[cite_start]Lo Schema SRTP è un protocollo standard europeo sviluppato dall'European Payment Council (EPC) per inviare richieste di pagamento elettronico in modo sicuro e tracciabile.  [cite_start]Consente di inviare notifiche di pagamento prima della transazione effettiva, facilitando la gestione e il controllo dei pagamenti digitali. 

[cite_start]È importante sottolineare che SRTP **non è uno strumento di pagamento**, ma ne integra le caratteristiche, fungendo da facilitatore per la realizzazione di soluzioni di pagamento digitali. 

### 1.3. Modello di Funzionamento

[cite_start]Il sistema si basa su un modello "four-corner" che coinvolge le seguenti parti: 

* [cite_start]**Creditore**: L'iniziatore della SRTP e beneficiario del trasferimento dei fondi (es. Ente Creditore). 
* **SRTP Service Provider del Creditore**: Un partecipante allo schema che offre il servizio al Creditore. [cite_start]Può essere un PSP, un fornitore di servizi di fatturazione elettronica, o qualsiasi soggetto che intende offrire il servizio. 
* [cite_start]**Debitore**: Il destinatario della SRTP e ordinante del trasferimento dei fondi (es. Cittadino). 
* [cite_start]**SRTP Service Provider del Debitore**: Un partecipante allo schema che offre il servizio al Debitore, con le stesse caratteristiche del Service Provider del Creditore. 

![Modello SRTP](https://i.imgur.com/GzQ5w18.png)

### 1.4. Principi di Applicazione su pagoPA

[cite_start]L'implementazione della SRTP per la notifica di avvisi di pagamento pagoPA si basa sui seguenti principi: 

* [cite_start]**Conformità allo Standard**: L'adozione è conforme allo standard europeo EPC. 
* [cite_start]**Adesione Volontaria**: L'adesione allo schema da parte dei Service Provider è volontaria. 
* [cite_start]**Identificazione dei Service Provider**: Ogni Service Provider è identificato tramite Bank Identifier Code (BIC) o codice fiscale. 
* [cite_start]**Esecuzione del Pagamento**: Il pagamento deve essere eseguito in conformità con le linee guida del Nodo dei Pagamenti pagoPA.  [cite_start]È responsabilità del Service Provider del Debitore garantire la trasmissione delle informazioni a un PSP aderente a pagoPA per l'esecuzione del pagamento. 
* [cite_start]**Stato Indipendente**: Lo stato di una RTP (accettata, rifiutata, etc.) non influenza lo stato dell'avviso di pagamento sottostante. 
* [cite_start]**IBAN Fittizio**: L'IBAN veicolato nei messaggi è fittizio e non deve essere usato per il pagamento. 
* [cite_start]**Modello "Accept Later / Pay Later"**: È previsto un unico modello di funzionamento, dove le date di accettazione e di pagamento coincidono con la data di scadenza dell'avviso pagoPA. 
* [cite_start]**Significato dell'Accettazione**: L'accettazione della SRTP può assumere due significati a discrezione del Service Provider: 
    1.  [cite_start]**Effettiva esecuzione del pagamento**: L'accettazione avviene dopo che l'utente ha già pagato l'avviso. 
    2.  [cite_start]**Accettazione della richiesta**: L'accettazione è slegata dal pagamento; il debitore si impegna a pagare entro la scadenza. 

---

## 2. Flusso di Interazione e Messaggi

Tutte le comunicazioni tra i Service Provider sono asincrone. [cite_start]Il ricevente prende in carico il messaggio e invia l'esito a un endpoint di callback. 

### 2.1. Diagramma di Sequenza

[cite_start]Il diagramma illustra i tre flussi principali: invio di una SRTP, ricezione dello stato e richiesta di cancellazione. 

![Diagramma Flussi SRTP](https://i.imgur.com/hY4XgI8.png)

### 2.2. Mapping Messaggi SRTP e ISO 20022

| Flusso SRTP (Dataset EPC)                                    | Messaggio ISO 20022                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **DS-02**: Invio SRTP                                        | `Creditor Payment Activation Request V10 (pain.013.001.10)`  |
| **DS-04**: Rifiuto a processare la SRTP                      | `Creditor Payment Activation Request Status Report V07 (pain.014.001.07)` |
| **DS-08**: Risposta di accettazione/rifiuto alla SRTP        | `Creditor Payment Activation Request Status Report V07 (pain.014.001.07)` |
| **DS-11**: Richiesta di cancellazione della SRTP             | `Customer Payment Cancellation Request V08 (camt.055.001.08)` |
| **DS-12**: Risposta alla richiesta di cancellazione          | `Resolution Of Investigation v09 (camt.029.001.09)`          |
[cite_start]

---

## 3. Specifica dei Messaggi

### 3.1. Invio di una SRTP (DS-02)

[cite_start]Questo messaggio descrive il contenuto di una SRTP inviata dal Service Provider del Creditore a quello del Debitore.  [cite_start]Corrisponde allo standard `pain.013.001.10`. 

#### 3.1.1. Dettaglio Campi (DS-02)

| ID Campo | Descrizione EPC | Utilizzo su pagoPA |
| :--- | :--- | :--- |
| `C001` | Iban of the Payee | [cite_start]**Sì** - IBAN fittizio, non usare per il pagamento.  |
| `E001` | Name of The Payee | [cite_start]**Sì**  |
| `E005` | Payee's identification code | [cite_start]**Sì** - Codice fiscale dell'Ente Creditore.  |
| `S002` | Payee's end-to-end reference of the RTP | [cite_start]**Sì** - `NumeroAvviso`.  |
| `N002` | Identifier of the Payee's RTP Service Provider | [cite_start]**Sì** - BIC o Codice Fiscale.  |
| `S011` | Additional unique reference provided by the Payee's RTP Service Provider | [cite_start]**Sì**  |
| `P009` | Identifier of the Payer | [cite_start]**Sì** - Codice fiscale del debitore.  |
| `P001` | Name of the Payer | [cite_start]**Sì** - Nome del Debitore.  |
| `N001` | Identifier of the Payer's RTP Service Provider | [cite_start]**Sì** - BIC o Codice Fiscale.  |
| `T002` | Amount of the RTP | [cite_start]**Sì** - Importo dell'avviso pagoPA.  |
| `T001` | Identification code of the Scheme | [cite_start]**Sì** - Valore fisso "SRTP".  |
| `S005` | Expiry Date/Time of the RTP | [cite_start]**Sì** - Data di scadenza dell'avviso.  |
| `S012` | Date and Time Stamp of the RTP | [cite_start]**Sì**  |
| `S001` | Remittance Information for the Payer | [cite_start]**Sì** - Descrizione dell'avviso.  |
| `T009` | RTP Remittance Information to be inserted in the payment | [cite_start]**Sì** - Oggetto dell'avviso.  |
| `T013` | Requested Execution Date/Time of the payment | [cite_start]**Sì** - Data di scadenza dell'avviso.  |
| `S003` | Type of payment instrument requested by the Payee | [cite_start]**Sì** - Valore fisso "PAGOPA".  |

[cite_start]*(Nota: La tabella include solo i campi utilizzati nel contesto pagoPA, come indicato nel documento originale)*. 

#### 3.1.2. Esempio Payload: `Creditor Payment Activation Request V10 (pain.013.001.10)`

```json
{
  "resourceId": "ab85fbb7a48a4a669b5436ee5b497036",
  "callbackUrl": "[http://spsrtp.api.cstar.pagopa.it](http://spsrtp.api.cstar.pagopa.it)",
  "Document": {
    "CdtrPmtActvtnReq": {
      "GrpHdr": {
        "MsgId": "ab85fbb7a48a4a669b5436ee5b497036",
        "CreDtTm": "2024-11-11T07:46:34.139037273Z",
        "Nb0fTxs": "1",
        "InitgPty": {
          "Nm": "PagoPA",
          "Id": null
        }
      },
      "PmtInf": [
        {
          "PmtInfId": "ab85fbb7a48a4a669b5436ee5b497036",
          "PmtMtd": "TRF",
          "ReqdAdvcTp": null,
          "ReqdExctnDt": {
            "Dt": "2024-12-10",
            "DtTm": null
          },
          "XpryDt": {
            "Dt": "2024-12-10",
            "DtTm": null
          },
          "Dbtr": {
            "Nm": "Mario Rossi",
            "PstlAdr": null,
            "Id": {
              "OrgId": null,
              "PrvtId": {
                "Othr": [
                  {
                    "Id": "RSSMRA74D22A0010",
                    "SchmeNm": {
                      "Cd": "POID",
                      "Prtry": null
                    }
                  }
                ]
              }
            }
          },
          "DbtrAcct": null,
          "DbtrAgt": {
            "FinInstnId": {
              "BICFI": "UNCRITMMXXX",
              "LEI": null,
              "Othr": null
            }
          },
          "CdtTrfTx": [
            {
              "PmtId": {
                "InstrId": "9b9e6b24-ba43-4545-8df3-16340553b8d4",
                "EndToEndId": "302001234876234678"
              },
              "PmtTpInf": {
                "SvcLv1": {
                  "Cd": "SRTP"
                },
                "LclInstrm": {
                  "Cd": null,
                  "Prtry": "PAGOPA"
                },
                "CtgyPurp": null
              },
              "PmtCond": null,
              "ReqdExctnDt": null,
              "Amt": {
                "InstdAmt": "100.0 "
              },
              "ChrgBr": "SLEV",
              "CdtrAgt": {
                "FinInstnId": {
                  "BICFI": null,
                  "LEI": null,
                  "Othr": {
                    "Id": "15376371009",
                    "SchmeNm": {
                      "Cd": "BOID"
                    }
                  }
                }
              },
              "Cdtr": {
                "Nm": "Comune di Roma ",
                "PstlAdr": null,
                "Id": {
                  "OrgId": {
                    "AnyBIC": null,
                    "LEI": null,
                    "Othr": [
                      {
                        "Id": "02438750586",
                        "SchmeNm": {
                          "Cd": "BOID",
                          "Prtry": null
                        }
                      }
                    ]
                  },
                  "PrvtId": null
                }
              },
              "CdtrAcct": {
                "Id": {
                  "IBAN": "XXIBAN_FITTIZIOXX"
                }
              },
              "UltmtCdtr": null,
              "InstrForCdtrAgt": [
                {
                  "InstrInf": "ATR113/fsldcsdlcvsoi123"
                }
              ],
              "Purp": null,
              "RltdRmtInf": null,
              "RmtInf": {
                "Ustrd": [
                  "oggetto /302001234876234678",
                  "ATS001/TARI 2025 rata unica"
                ],
                "Strd": null
              }
            }
          ]
        }
      ]
    }
  },
  "_links": null
}
````



### 3.2. Risposta alla SRTP (DS-08)

Questo messaggio (`pain.014.001.07`) viene usato per comunicare l'accettazione o il rifiuto di una SRTP da parte del Debitore. 

#### 3.2.1. Dettaglio Campi - Risposta Positiva (Accettazione)

| ID Campo | Obbligatorio/Opzionale | Contenuto ITA |
| :--- | :--- | :--- |
| `R001` | Obbligatorio | Tipo di risposta, valorizzato con `Acceptance`.  |
| `R002` | Obbligatorio | Mittente, valorizzato con `Payer's RTP Service Provider`.  |
| `R091` | Obbligatorio | Timestamp di ricezione della risposta dal Debitore.  |
| `R100` | Obbligatorio | Timestamp di invio del messaggio di accettazione.  |
| `R101` | Obbligatorio | Riferimento univoco della risposta fornito dal Payer's RTP Service Provider.  |
| `R092` | Opzionale | Data in cui sarà effettuato il pagamento.  |

*Nota: Il messaggio deve contenere anche una copia dei campi obbligatori della SRTP originale per tracciamento.* 

#### 3.2.2. Dettaglio Campi - Risposta Negativa (Rifiuto)

| ID Campo | Obbligatorio/Opzionale | Contenuto ITA |
| :--- | :--- | :--- |
| `R001` | Obbligatorio | Tipo di risposta (es. `Rejection`).  |
| `R002` | Obbligatorio | Mittente, valorizzato con `Payer's RTP Service Provider`.  |
| `R004` | Obbligatorio | Codice del motivo del rifiuto della SRTP.  |
| `R091` | Obbligatorio | Timestamp di ricezione della risposta dal Debitore.  |
| `R100` | Obbligatorio | Timestamp di invio del messaggio di rifiuto.  |
| `R101` | Obbligatorio | Identificativo univoco del messaggio.  |

*Nota: Il messaggio deve contenere anche una copia dei campi obbligatori della SRTP originale per tracciamento.* 

#### 3.2.3. Esempio Payload: `Creditor Payment Activation Request Status Report V07 (pain.014.001.07)`

```json
{
  "Document": {
    "CdtrPmtActvtnReqStsRpt": {
      "GrpHdr": {
        "MsgId": "string",
        "CreDtTm": "string",
        "InitgPty": {
          "Nm": "Mario Rossi",
          "Id": {
            "OrgId": {
              "AnyBIC": null,
              "LEI": null,
              "Othr": {
                "Id": "codice fiscal",
                "SchmeNm": {
                  "Cd": "POID"
                },
                "Issr": null
              }
            }
          }
        }
      },
      "OrgnlGrpInfAndSts": {
        "OrgnlMsgId": "ab85fbb7a48a4a669b5436ee5b497036",
        "OrgnlMsgNmId": "pain.013.001.10",
        "OrgnlCreDtTm": "2024-11-11T07:46:34.139037273Z",
        "OrgnlPmtInfAndSts": [
          {
            "Orgn1PmtInfId": "ab85fbb7a48a4a669b5436ee5b497036",
            "TxInfAndSts": {
              "StsId": "string",
              "OrgnlInstrId": "9b9e6b24-ba43-4545-8df3-f6340553b8d4",
              "OrgnlEndToEndId": "302001234876234678",
              "TxSts": "ACCP",
              "StsRsnInf": {
                "Orgtr": {
                  "Id": {
                    "OrgId": {
                      "AnyBIC": null,
                      "LEI": null,
                      "Othr": {
                        "Id": "codice fiscal",
                        "SchmeNm": {
                          "Cd": "POID"
                        },
                        "Issr": null
                      }
                    }
                  }
                },
                "AddtlInf": null
              },
              "OrgnlTxRef": {
                "Amt": {},
                "ReqdExctnDt": {},
                "XpryDt": {},
                "PmtTpInf": {},
                "RmtInf": {},
                "DbtrAgt": {},
                "CdtrAgt": {},
                "Cdtr": {},
                "CdtrAcct": {}
              }
            }
          }
        ]
      }
    }
  }
}
```



### 3.3. Richiesta di Cancellazione (DS-11)

Una Richiesta di Cancellazione (RfC) viene inviata dal Creditore o dal suo Service Provider.  Corrisponde allo standard `camt.055.001.08`. 

#### 3.3.1. Scenari di Utilizzo

  * **Pagamento avvenuto** su un altro canale (`AT-R106=PAID`). 
  * **Duplicazione** di SRTP (`AT-R106=DRTP`). 
  * **Annullamento** dell'avviso di pagamento (`AT-R106=MODT`). 
  * **Errori Tecnici** (`AT-R106=TECH`). 

#### 3.3.2. Caratteristiche Principali

  * La richiesta può essere effettuata fino alla data di scadenza della SRTP, a meno che non sia già stata rifiutata o cancellata. 
  * La SRTP da cancellare è identificata dall'attributo `AT-S011`. 
  * Include una copia dei dati principali della SRTP originale per tracciamento. 
  * Contiene un codice (`AT-R106`) che identifica la motivazione. 

#### 3.3.3. Dettaglio Campi (DS-11)

| ID Campo | Utilizzo su pagoPA |
| :--- | :--- |
| `R106` | **Sì** - Codice motivo della cancellazione.  |
| `R108` | **Sì** - Riferimento specifico per la RfC.  |
| `R109` | **Sì** - Timestamp della RfC.  |
| Altro | **Sì** - Copia degli attributi obbligatori della SRTP originale.  |

#### 3.3.4. Esempio Payload: `Customer Payment Cancellation Request V08 (camt.055.001.08)`

```json
{
  "resourceId": "string",
  "Document": {
    "CstmxPmtCxlReq": {
      "Assgnmt": {
        "Id": "string",
        "Assgnr": {
          "Pty": {
            "Id": {
              "OrgId": {
                "AnyBIC": null,
                "LEI": null,
                "Othr": {
                  "Id": "15376371009",
                  "SchmeNm": { "Cd": "BOID", "Prtry": null },
                  "Issr": null
                }
              }
            }
          },
          "Agt": null
        },
        "Assgne": {
          "Pty": null,
          "Agt": {
            "FinInstnId": { "BICFI": "UNICRR", "LEI": null, "Othr": null }
          }
        },
        "CreDtTm": "string"
      },
      "Undrlyg": {
        "OrgnlPmtInfAndCx1": [
          {
            "PmtCxlId": "string",
            "OrgnlPmtInfId": "string",
            "OrgnlGrpInf": {
              "OrgnlMsgId": "ab85fbb7a48a4a669b5436ee5b497036",
              "OrgnlMsgNmId": "pain.013.001.10",
              "OrgnlCreDtTm": "2024-11-11T07:46:34.139037273Z"
            },
            "TxInf": [
              {
                "CxlId": "string",
                "OrgnlInstrId": "9b9e6b24-ba43-4545-8df3-f6340553b8d4",
                "OrgnlEndToEndId": "302001234876234678",
                "CxlRsnInf": {
                  "Orgtr": {
                    "Nm": "Comune di Roma",
                    "Id": {
                      "OrgId": {
                        "AnyBIC": null,
                        "LEI": null,
                        "Othr": {
                          "Id": "02438750586",
                          "SchmeNm": { "Cd": "BOID" },
                          "Issr": null
                        }
                      },
                      "PrvtId": null
                    }
                  },
                  "Rsn": { "Cd": "PAID" },
                  "AddtlInf": [ "ATS005/2024-12-10" ]
                },
                "OrgnlTxRef": {
                  "Amt": { "InstdAmt": "100.0 " },
                  "ReqdExctnDt": { "Dt": "2024-12-10", "DtTm": null },
                  "PmtTpInf": {
                    "SvcLv1": { "Cd": "SRTP" },
                    "LclInstrm": { "Cd": null, "Prtry": "PAGOPA" },
                    "CtgyPurp": null
                  },
                  "RmtInf": {
                    "Ustrd": [
                      "TARI immobile 1234 / 302001234876234678",
                      "ATS001/TARI 2025 rata unica"
                    ],
                    "Strd": null
                  },
                  "DbtrAgt": {
                    "FinInstnId": { "BICFI": "UNCRITMMXXX", "LEI": null, "Othr": null }
                  },
                  "CdtrAgt": {
                    "FinInstnId": {
                      "BICFI": null,
                      "LEI": null,
                      "Othr": {
                        "Id": "15376371009",
                        "SchmeNm": { "Cd": "BOID", "Prtry": null },
                        "Issr": null
                      }
                    }
                  },
                  "Cdtr": {
                    "Nm": "Comune di Roma",
                    "Id": {
                      "OrgId": {
                        "Othr": [ { "Id": "02438750586" } ]
                      }
                    }
                  }
                }
              }
            ]
          }
        ]
      }
    }
  }
}
```



### 3.4. Risposta alla Richiesta di Cancellazione (DS-12)

Questo messaggio (`camt.029.001.09`) è la risposta asincrona a una richiesta di cancellazione. 

#### 3.4.1. Dettaglio Oggetti Principali

| Oggetto | Tipo |
| :--- | :--- |
| `RsltnOfInvstgtn` | `ResolutionOfInvestigationV09_EPC259-22_V3.0_DS12P` |
| `Assgnmt` | `CaseAssignment5_EPC259-22_V3.0_DS11` |
| `Sts` | `ExternalInvestigationExecutionConfirmation1Code_II_Wrapper` |
| `CxIDtls` | `UnderlyingTransaction22_EPC259-22_V3.0_DS12P` |


#### 3.4.2. Esempio Payload: `Resolution Of Investigation v09 (camt.029.001.09)`

```json
{
  "resourceId": "string",
  "SepaRequestToPayCancellationResponse": {
    "Document": {
      "Rsltn0fInvstgtn": {
        "Assgnmt": {
          "Id": "string",
          "Assgnr": { "Pty": { "Id": { "OrgId": { "AnyBIC": "string", "LEI": "string", "Othr": {} } } } },
          "Assgne": { "Pty": { "Id": { "OrgId": { "AnyBIC": "string", "LEI": "string", "Othr": {} } } } },
          "CreDtTm": "string"
        },
        "Sts": { "Conf": "CNCL" },
        "CxlDtls": {
          "OrgnlPmtInfAndSts": [
            {
              "Orgn1PmtInfId": "string",
              "TxInfAndSts": [ { "OrgnlInstrId": "string", "OrgnlEndToEndId": "string" } ]
            }
          ],
          "TxInfAndSts": [
            {
              "CxlStsId": "string",
              "OrgnlGrpInf": {
                "OrgnlMsgId": "string",
                "OrgnlMsgNmId": "string",
                "OrgnlCreDtTm": "string"
              },
              "OrgnlInstrId": "string",
              "OrgnlEndToEndId": "string",
              "OrgnlTxId": "string",
              "TxCxlSts": "ACCR",
              "CxlStsRsnInf": { "Orgtr": { "Id": {} }, "AddtlInf": [ "string" ] },
              "RsltnRltdInf": { "Chrgs": { "Amt": 0.01, "Agt": {} } },
              "OrgnlTxRef": {
                "Amt": { "InstdAmt": 0 },
                "ReqdExctnDt": { "Dt": "string" },
                "PmtTpInf": { "SvcLvl": {}, "LclInstrm": {} },
                "RmtInf": { "Ustrd": "string", "Strd": {} },
                "DbtrAgt": { "FinInstnId": {} },
                "CdtrAgt": { "FinInstnId": {} },
                "Cdtr": { "Pty": {} },
                "CdtrAcct": { "Id": {} }
              }
            }
          ]
        }
      }
    },
    "links": {
      "initialSepaRequestToPayUri": { "href": "string", "templated": false }
    }
  }
}
```



-----

## 4\. Servizio di Attivazione

### 4.1. Descrizione del Servizio

Il processo di Attivazione è l'accordo con cui un Debitore (Cittadino/Azienda) acconsente a ricevere notifiche SRTP da un Beneficiario (Ente Creditore).  PagoPA mette a disposizione un servizio centralizzato per gestire questi consensi.  Il consenso è permanente (fino a revoca) e valido per qualsiasi tipo di tributo. 

### 4.2. Autenticazione

Per utilizzare il servizio di attivazione, è richiesta l'autenticazione tramite OAuth2 (Client Credential Grant), utilizzando le credenziali (`client_id` e `client_secret`) fornite in fase di adesione. 

### 4.3. Caso d'uso: Creazione Attivazione

Questo flusso descrive la richiesta di attivazione al servizio SRTP per un debitore specifico tramite un determinato Service Provider. 

  * **API Coinvolte**: `Get AccessToken`, `Creazione Attivazione` 
  * **Diagramma**:
    1.  Il Service Provider richiede un `AccessToken`. 
    2.  Il Service Provider invia la richiesta di `CreazioneAttivazione`. 
    3.  Il servizio risponde con un `201 OK`. 

### 4.4. Caso d'uso: Cancellazione Attivazione

Questo flusso descrive la richiesta di cancellazione di un'attivazione precedentemente creata. 

  * **API Coinvolte**: `Get AccessToken`, `Cancella Attivazione` 
  * **Diagramma**:
    1.  Il Service Provider richiede un `AccessToken`. 
    2.  Il Service Provider invia la `RichiestaCancellazione`. 
    3.  Il servizio risponde con un `201 OK`. 

*(Nota: Le specifiche OpenAPI per queste chiamate non sono state caricate correttamente nel documento originale).* 

-----

## 5\. Processo di Adesione al Servizio

Per aderire al servizio, i Service Provider devono: 

1.  **Sottoscrivere la convenzione**, specificando: 
      * Identificativo del Service Provider (BIC o codice fiscale). 
      * Ruolo ricoperto (SP del Debitore, del Creditore o entrambi). 
      * Identificativo del canale pagoPA usato per i pagamenti. 
2.  **Nominare i referenti**: 
      * **Referente tecnico**: Contatto per l'integrazione. 
      * **Beta-Tester**: Utenti autorizzati a usare l'interfaccia web di test. 

A seguito della sottoscrizione, il referente tecnico riceverà le credenziali (`clientId`, `secret`) per accedere ai servizi.  Per supporto è possibile aprire un ticket all'indirizzo `ticket.cstar.srtp@pagopa.it`. 

-----

## 6\. Riferimenti

  * **Specifiche SRTP (EPC)**: [https://www.europeanpaymentscouncil.eu/what-we-do/other-schemes/sepa-request-pay](https://www.europeanpaymentscouncil.eu/what-we-do/other-schemes/sepa-request-pay) 
  * **Linee Guida Comitato Pagamenti Italia**: [https://www.bancaditalia.it/compiti/sispaga-mercati/comitato-pagamenti-italia/CPI-Tavolo-incassi-e-pagamenti-pubblici-RTP-PagoPA.pdf](https://www.bancaditalia.it/compiti/sispaga-mercati/comitato-pagamenti-italia/CPI-Tavolo-incassi-e-pagamenti-pubblici-RTP-PagoPA.pdf) 
  * **Specifiche API EPC correlate**: [https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2023-06/EPC137-22%20v3.1%20-%20SRTP%20related%20API%20Specifications%20-%20Preliminary%20Information.pdf](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2023-06/EPC137-22%20v3.1%20-%20SRTP%20related%20API%20Specifications%20-%20Preliminary%20Information.pdf) 

