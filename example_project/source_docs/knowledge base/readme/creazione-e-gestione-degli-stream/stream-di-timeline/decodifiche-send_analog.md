---
description: >-
  Decodifica dei campi deliveryDetailCode e deliveryFailureCause per degli
  eventi di invio cartaceo.
---

# Decodifiche SEND\_ANALOG

## Decodifica in SEND\_ANALOG\_PROGRESS

Nella tabelle sono riportate le decodifiche dell'elemento `deliveryDetailCode` all'interno dell'oggetto `details` degli eventi SEND\_ANALOG\_PROGRESS.

Esempio:

```json
{
	"elementId": "SEND_ANALOG_PROGRESS.IUN_GPTG-NEPG-ZTET-202402-E-1.RECINDEX_0.ATTEMPT_0.IDX_1",
	"timestamp": "2024-02-29T16:10:08Z",
	"legalFactsIds": [],
	"category": "SEND_ANALOG_PROGRESS",
	"details": {
		"recIndex": 0,
		"notificationDate": "2024-02-29T16:10:08Z",
		"deliveryDetailCode": "C0N080", 
		"serviceLevel": "AR_REGISTERED_LETTER",
		"sendRequestId": "SEND_ANALOG_DOMICILE.IUN_GPTG-NEPG-ZTET-202402-E-1.RECINDEX_0.ATTEMPT_0",
		"registeredLetterCode": "e0784bcfcf2b44aa8207ea801395969e"
	}
}
```

I codici possono differire a seconda del tipo di prodotto (RIR, AR, 890).

### Codici SEND\_ANALOG\_PROGRESS comuni a tutte le tipologie



<table data-header-hidden><thead><tr><th width="196"></th><th></th></tr></thead><tbody><tr><td><strong>deliveryDetailCode</strong></td><td><strong>Significato</strong></td></tr><tr><td>CON020</td><td>Originale dell’AAR (documento nativo digitale) reso disponibile dal Consolidatore e firmato digitalmente da PagoPA</td></tr><tr><td>CON080</td><td>Stampato ed Imbustato. Lo stato riguarda tutti i tipi di raccomandata (890, A/R, Raccomandata internazionale con A/R) e può avvenire più volte. Deve riportare il numero della raccomandata, quando ci sarà.</td></tr><tr><td>CON018</td><td>Accettazione Recapitista - L’evento rappresenta l’accettazione della Distinta di presa in carico da parte del Recapitista</td></tr><tr><td>PNALL001</td><td>L’indirizzo identificato per il secondo tentativo non ha superato il processo di validazione.<br>NOTA: tale evento precede l’inizio del secondo tentativo, in timeline andrebbe dunque visualizzato anche l’indirizzo oggetto della validazione</td></tr><tr><td><p>CON993</p><p>-</p><p>CON995</p></td><td>Errore di Stampa</td></tr><tr><td>CON996</td><td>Errore in fase di valutazione della stampabilità del documento.</td></tr><tr><td>CON997</td><td><p>Errore di validazione CAP/Zona Internazionale</p><p>Sarà sempre successivo a PNALL001</p></td></tr><tr><td>CON998</td><td>Errore Documento malformato (dimensioni, margini…)</td></tr></tbody></table>

### Codici SEND\_ANALOG\_PROGRESS per raccomandata AR

<table data-header-hidden><thead><tr><th width="193"></th><th></th></tr></thead><tbody><tr><td><strong>deliveryDetailCode</strong></td><td><strong>Significato</strong></td></tr><tr><td>RECRN001A*</td><td>Consegnato - pre-esito</td></tr><tr><td>RECRN001B</td><td><p>Consegnato</p><p>Con Dematerializzazione - AR</p></td></tr><tr><td>RECRN002A*</td><td>Mancata consegna - pre-esito</td></tr><tr><td>RECRN002B</td><td><p>Mancata consegna</p><p>Con Dematerializzazione - Plico</p></td></tr><tr><td>RECRN002D*</td><td>Irreperibilità Assoluta - pre-esito</td></tr><tr><td>RECRN002E</td><td><p>Irreperibilità Assoluta. È un evento finale.</p><p>Con Dematerializzazione – Plico Indagine*</p></td></tr><tr><td>RECRN010</td><td><p>Esito negativo di consegna:</p><p>Il tentativo di consegna della raccomandata A/R non è andato a buon fine per destinatario assente.</p></td></tr><tr><td>RECRN011</td><td>Inizio Giacenza</td></tr><tr><td>RECRN003A*</td><td>Consegnato presso Punti di Giacenza - pre-esito</td></tr><tr><td>RECRN003B</td><td><p>Consegnato presso Punti di Giacenza</p><p>Con Dematerializzazione - AR</p></td></tr><tr><td>RECRN003C</td><td>Consegnato presso Punti di Giacenza</td></tr><tr><td>RECRN004A*</td><td>Mancata consegna presso Punti di Giacenza - pre-esito</td></tr><tr><td>RECRN004B</td><td><p>Mancata consegna presso Punti di Giacenza</p><p>Con Dematerializzazione - Plico</p></td></tr><tr><td>RECRN004C</td><td>Mancata consegna presso Punti di Giacenza</td></tr><tr><td>RECRN005A*</td><td>Compiuta giacenza pre-esito</td></tr><tr><td>RECRN005B</td><td><p>Compiuta giacenza</p><p>Con Dematerializzazione - Plico</p></td></tr><tr><td>RECRN005C</td><td>Compiuta giacenza</td></tr><tr><td>RECRN006</td><td><p>Furto/Smarrimanto/deterioramento</p><p><strong>deliveryFailureCause</strong>: F01 F02 F03 F04</p><p><br>NOTA: SEND genera una nuova spedizione che va a sostituire la vecchia.</p></td></tr><tr><td>RECRN013</td><td><p>Non Rendicontabile</p><p><br>NOTA: SEND genera una nuova spedizione che va a sostituire la vecchia.</p></td></tr><tr><td>RECRN015</td><td><p>Causa di forza maggiore</p><p><br>NOTA: SEND <strong>non</strong> genera una nuova spedizione perché il recapitista ritenterà la consegna al valle del rientro delle cause che l'hanno bloccata.</p></td></tr></tbody></table>

### Codici SEND\_ANALOG\_PROGRESS per raccomandata 890

<table data-header-hidden><thead><tr><th width="198"></th><th></th></tr></thead><tbody><tr><td><strong>deliveryDetailCode</strong></td><td><strong>Significato</strong></td></tr><tr><td>RECAG001A*</td><td>Consegnato - pre-esito</td></tr><tr><td>RECAG001B</td><td><p>Consegnato</p><p>Con Dematerializzazione - 23L</p></td></tr><tr><td>RECAG002A*</td><td>Consegnato a persona abilitata - pre-esito</td></tr><tr><td>RECAG002B</td><td><p>Consegnato a persona abilitata</p><p>Con Dematerializzazione - 23L</p></td></tr><tr><td>RECAG003A*</td><td>Mancata consegna - pre-esito</td></tr><tr><td>RECAG003B</td><td>Mancata consegna</td></tr><tr><td>RECAG003D*</td><td>Irreperibilità Assoluta - pre-esito</td></tr><tr><td>RECAG003E</td><td><p>Irreperibilità Assoluta</p><p>Con Dematerializzazione - Plico e Indagine opzionalmente</p></td></tr><tr><td>RECAG004</td><td><p>Furto/Smarrimanto/deterioramento</p><p><strong>deliveryFailureCause</strong>: F01 F02 F03 F04<br>NOTA: SEND genera una nuova spedizione che va a sostituire la vecchia.</p></td></tr><tr><td>RECAG010</td><td>Esito negativo di consegna: Il tentativo di consegna della raccomandata 890  non è andato a buon fine per destinatario assente.</td></tr><tr><td>RECAG011A</td><td>Inizio giacenza</td></tr><tr><td>RECAG011B</td><td><p>Evento con Dematerializzazione in giacenza</p><ul><li>Dematerializzazione - 23L**</li><li>Con Avviso Ricevimento Comunicazione Avvenuto Deposito - ARCAD (in caso di recapito) - PDF o file ZIP in caso full-digital</li><li>Con Comunicazione Avvenuto Deposito - CAD (in caso di mancato recapito CAD) </li></ul></td></tr><tr><td>RECAG012A*</td><td>Distacco della 23L dal plico - pre esito<br>23L è stata accettata (staccata dal plico) decorsi 10 giorni dall'invio della AR/CAD (Comunicazione Avvenuto deposito)</td></tr><tr><td>RECAG012</td><td>Distacco della 23L dal plico<br>23L è stata accettata (staccata dal plico) decorsi 10 giorni dall'invio della AR/CAD (Comunicazione Avvenuto deposito)<br>Conferma il distacco 23L - Feedback del distacco 23L</td></tr><tr><td>RECAG005A*</td><td>Consegnato presso Punti di Giacenza - pre-esito</td></tr><tr><td>RECAG005B</td><td><p>Consegnato presso Punti di Giacenza</p><ul><li>Dematerializzazione - 23L**</li></ul><ul><li>Con Avviso Ricevimento Comunicazione Avvenuto Deposito - ARCAD (in caso di recapito) - PDF o file ZIP in caso full-digital</li></ul><ul><li>Con Comunicazione Avvenuto Deposito - CAD (in caso di mancato recapito CAD)</li></ul></td></tr><tr><td>RECAG005C</td><td>Consegnato presso Punti di Giacenza - Chiusura fascicolo</td></tr><tr><td>RECAG006A*</td><td>Consegna a persona delegata presso Punti di Giacenza - pre-esito</td></tr><tr><td>RECAG006B</td><td><p>Consegna a persona delegata presso Punti di Giacenza</p><ul><li>Dematerializzazione - 23L**</li></ul><ul><li>Con Avviso Ricevimento Comunicazione Avvenuto Deposito - ARCAD (in caso di recapito) - PDF o file ZIP in caso full-digital</li></ul><ul><li>Con Comunicazione Avvenuto Deposito - CAD (in caso di mancato recapito CAD)</li></ul></td></tr><tr><td>RECAG006C</td><td>Consegna a persona delegata presso Punti di Giacenza - Chiusura fascicolo</td></tr><tr><td>RECAG007A*</td><td>Mancata consegna presso Punti di Giacenza - pre-esito</td></tr><tr><td>RECAG007B</td><td><p>Mancata consegna presso Punti di Giacenza</p><ul><li>Dematerializzazione - 23L**</li></ul><ul><li>Con Avviso Ricevimento Comunicazione Avvenuto Deposito - ARCAD (in caso di recapito) - PDF o file ZIP in caso full-digital</li></ul><ul><li>Con Comunicazione Avvenuto Deposito - CAD (in caso di mancato recapito CAD)</li></ul></td></tr><tr><td>RECAG007C</td><td>Mancata consegna presso Punti di Giacenza - Chiusura fascicolo</td></tr><tr><td>RECAG008A*</td><td>Compiuta giacenza - pre-esito</td></tr><tr><td>RECAG008B</td><td><p>Compiuta giacenza</p><p>Con Dematerializzazione - Plico</p></td></tr><tr><td>RECAG008C</td><td>Compiuta giacenza - Chiusura fascicolo</td></tr><tr><td>RECAG013</td><td>Non Rendicontabile<br><br>NOTA: SEND genera una nuova spedizione che va a sostituire la vecchia.</td></tr><tr><td>RECAG015</td><td>Causa di forza maggiore<br><br>NOTA: SEND <strong>non</strong> genera una nuova spedizione perché il recapitista ritenterà la consegna al valle del rientro delle cause che l'hanno bloccata.</td></tr></tbody></table>

### Codici SEND\_ANALOG\_PROGRESS per raccomandata RIR (Internazionale)

<table data-header-hidden><thead><tr><th width="197"></th><th></th></tr></thead><tbody><tr><td><strong>deliveryDetailCode</strong></td><td><strong>Significato</strong></td></tr><tr><td>RECRI001</td><td>Avviato all’estero</td></tr><tr><td>RECRI002</td><td>Ingresso nel paese estero</td></tr><tr><td>RECRI003A*</td><td>Consegnato - pre-esito</td></tr><tr><td>RECRI003B</td><td><p>Consegnato</p><p>Con Dematerializzazione - AR</p></td></tr><tr><td>RECRI004A*</td><td>Non Consegnato - pre-esito</td></tr><tr><td>RECRI004B</td><td><p>Non Consegnato</p><p>Con Dematerializzazione - Plico</p></td></tr><tr><td>RECRI005</td><td><p>Furto/Smarrimanto/deterioramento</p><p><strong>deliveryFailureCause</strong>: F01 F02 F03</p><p><br>NOTA: SEND genera una nuova spedizione che va a sostituire la vecchia.</p></td></tr></tbody></table>

### Codici SEND\_ANALOG\_PROGRESS per raccomandata semplice RS

| **deliveryDetailCode** | **Significato**                                                                                                                                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RECRS010               | Esito negativo di consegna: il tentativo di consegna della raccomandata semplice non è andato a buon fine per destinatario assente.                                                               |
| RECRS011               | In giacenza                                                                                                                                                                                       |
| RECRS001C              | Consegnato - Fascicolo Chiuso                                                                                                                                                                     |
| RECRS002A              | Mancata consegna - pre-esito                                                                                                                                                                      |
| RECRS002B              | <p>Mancata consegna - </p><p>Con Dematerializzazione</p>                                                                                                                                          |
| RECRS002C\*            | Mancata consegna - Fascicolo Chiuso                                                                                                                                                               |
| RECRS002D\*            | Irreperibilità Assoluta - pre-esito                                                                                                                                                               |
| RECRS002E              | <p>Irreperibilità Assoluta </p><p>Con Dematerializzazione</p>                                                                                                                                     |
| RECRS002F              | Irreperibilità Assoluta - Fascicolo Chiuso                                                                                                                                                        |
| RECRS003C              | Consegnato presso Punti di Giacenza - Fascicolo Chiuso                                                                                                                                            |
| RECRS004A\*            | Mancata consegna presso Punti di Giacenza - pre-esito                                                                                                                                             |
| RECRS004B              | Mancata consegna presso Punti di Giacenza - Con Dematerializzazione                                                                                                                               |
| RECRS004C              | Mancata consegna presso Punti di Giacenza - Fascicolo Chiuso                                                                                                                                      |
| RECRS005A\*            | Compiuta giacenza pre-esito                                                                                                                                                                       |
| RECRS005B              | <p>Compiuta giacenza -</p><p>Con Dematerializzazione</p>                                                                                                                                          |
| RECRS005C              | Compiuta giacenza - Fascicolo Chiuso                                                                                                                                                              |
| RECRS006               | <p>Furto/Smarrimento/deterioramento<br><br>NOTA: SEND genera una nuova spedizione che va a sostituire la vecchia.</p>                                                                             |
| RECRS013               | <p>Non Rendicontabile<br><br>NOTA: SEND genera una nuova spedizione che va a sostituire la vecchia.</p>                                                                                           |
| RECRS015               | <p>Causa Forza Maggiore<br><br>NOTA: SEND <strong>non</strong> genera una nuova spedizione perché il recapitista ritenterà la consegna al valle del rientro delle cause che l'hanno bloccata.</p> |

### Codici SEND\_ANALOG\_PROGRESS per raccomandata semplice internazionale RSI

| **deliveryDetailCode** | **Significato**                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------- |
| RECRSI001              | Avviato all'estero                                                                                                    |
| RECRSI002              | Ingresso nel paese estero                                                                                             |
| RECRSI003C             | Consegnato - Fascicolo Chiuso                                                                                         |
| RECRSI004A\*           | Non Consegnato - pre-esito                                                                                            |
| RECRSI004B             | <p>Non Consegnato -</p><p>Con Dematerializzazione</p>                                                                 |
| RECRSI004C             | Non Consegnato - fascicolo Chiuso                                                                                     |
| RECRSI005              | <p>Furto/Smarrimento/deterioramento<br><br>NOTA: SEND genera una nuova spedizione che va a sostituire la vecchia.</p> |

\***NOTA pre-esiti**: _Tale informazione, che potrebbe non essere presente in timeline, rappresenta un pre-esito, ossia una prima informazione fornita dall’addetto al recapito, nelle more della trasmissione dell’esito (effettivo) in formato dematerializzato. L’informazione contenuta nel pre-esito potrebbe essere diversa da quella presente nell’esito. In tal caso, lo stato della notifica sarà modificato in coerenza con l’esito, prevalendo l’informazione dell’esito su quella del pre-esito_

## Decodifica SEND\_ANALOG\_FEEDBACK

Nella tabelle sono riportate le decodifiche dell'elemento `deliveryDetailCode` all'interno dell'oggetto `details` degli eventi SEND\_ANALOG\_FEEDBACK

Esempio:

```json
{
	"elementId": "SEND_ANALOG_FEEDBACK.IUN_GPTG-NEPG-ZTET-202402-E-1.RECINDEX_0.ATTEMPT_0",
	"timestamp": "2024-02-29T16:10:24Z",
	"legalFactsIds": [],
	"category": "SEND_ANALOG_FEEDBACK",
	"details": {
		"recIndex": 0,
		"physicalAddress": {
			"at": "Presso",
			"address": "VIA@OK_AR",
			"addressDetails": "SCALA B",
			"zip": "87100",
			"municipality": "COSENZA",
			"municipalityDetails": "COSENZA",
			"province": "CS",
			"foreignState": "ITALIA"
		},
		"sentAttemptMade": 0,
		"responseStatus": "OK",
		"notificationDate": "2024-02-29T16:10:24Z",
		"deliveryDetailCode": "RECRN001C",
		"serviceLevel": "AR_REGISTERED_LETTER",
		"sendRequestId": "SEND_ANALOG_DOMICILE.IUN_GPTG-NEPG-ZTET-202402-E-1.RECINDEX_0.ATTEMPT_0",
		"registeredLetterCode": "e0784bcfcf2b44aa8207ea801395969e"
	}
},
```

### Codici SEND\_ANALOG\_FEEDBACK per raccomandate AR

<table data-header-hidden><thead><tr><th width="215"></th><th></th></tr></thead><tbody><tr><td><strong>deliveryDetailCode</strong></td><td><strong>Significato</strong></td></tr><tr><td>RECRN001C</td><td>Consegnato. È un evento finale.</td></tr><tr><td>RECRN002C</td><td><p>Mancata consegna. È un evento finale.</p><p><strong>deliveryFailureCause</strong>: M02 M05 M06 M07 M08 M09</p></td></tr><tr><td>RECRN002F</td><td><p>Irreperibilità Assoluta</p><p><strong>deliveryFailureCause</strong>: M01 M03 M04</p></td></tr><tr><td>PNRN012</td><td>Perfezionamento in giacenza della notifica</td></tr><tr><td>RECRN003C</td><td>Consegnato presso Punti di Giacenza</td></tr><tr><td>RECRN004C</td><td>Mancata consegna presso Punti di Giacenza</td></tr></tbody></table>

### Codici SEND\_ANALOG\_FEEDBACK per raccomandate 890

<table data-header-hidden><thead><tr><th width="209"></th><th></th></tr></thead><tbody><tr><td><strong>deliveryDetailCode</strong></td><td><strong>Significato</strong></td></tr><tr><td>RECAG001C</td><td>Consegnato</td></tr><tr><td>RECAG002C</td><td>Consegnato a persona abilitata</td></tr><tr><td>RECAG003C</td><td><p>Mancata consegna</p><p><strong>deliveryFailureCause</strong>: M02 M05 M06 M07 M08 M09</p></td></tr><tr><td>RECAG003F</td><td><p>Irreperibilità Assoluta</p><p><strong>deliveryFailureCause</strong>: M01 M03 M04</p></td></tr><tr><td>RECAG011B</td><td><p>In Giacenza -</p><p>Con Dematerializzazione 23L</p></td></tr><tr><td>PNAG012</td><td>Perfezionamento giudiziario della notifica</td></tr><tr><td>RECAG005C</td><td>Consegnato presso Punti di Giacenza</td></tr><tr><td>RECAG006C</td><td>Consegna a persona delegata presso Punti di Giacenza</td></tr><tr><td>RECAG007C</td><td>Mancata consegna presso Punti di Giacenza</td></tr></tbody></table>

### Codici SEND\_ANALOG\_FEEDBACK per raccomandate RIR (internazionali)

<table data-header-hidden><thead><tr><th width="213"></th><th></th></tr></thead><tbody><tr><td><strong>deliveryDetailCode</strong></td><td><strong>Significato</strong></td></tr><tr><td>RECRI003C</td><td>Consegnato</td></tr><tr><td>RECRI004C</td><td>Non Consegnato</td></tr></tbody></table>





## Decodifica Pre-Esito

## Decodifica deliveryFailureCause <a href="#tabella-approfondimento-deliveryfailurecause" id="tabella-approfondimento-deliveryfailurecause"></a>

<table data-header-hidden><thead><tr><th width="224"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>deliveryFailureCause</strong></td><td><strong>motivo del fallimento</strong></td><td><strong>genera il 2° tentativo</strong></td></tr><tr><td>M01</td><td>perché il destinatario è irreperibile</td><td>sì</td></tr><tr><td>M02</td><td>perché il destinatario è deceduto</td><td>NO</td></tr><tr><td>M03</td><td>perché il destinatario è sconosciuto</td><td>sì</td></tr><tr><td>M04</td><td>perché il destinatario si è trasferito</td><td>sì</td></tr><tr><td>M05</td><td>perché l'invio è stato rifiutato</td><td>NO</td></tr><tr><td>M06</td><td>perché l’indirizzo è inesatto</td><td>sì</td></tr><tr><td>M07</td><td>perché l’indirizzo è inesistente</td><td>sì</td></tr><tr><td>M08</td><td>perché l’indirizzo è insufficiente</td><td>sì</td></tr><tr><td>M09</td><td>per altre motivazioni</td><td>sì</td></tr><tr><td>F01</td><td>furto</td><td></td></tr><tr><td>F02</td><td>smarrimento</td><td></td></tr><tr><td>F03</td><td>deterioramento</td><td></td></tr><tr><td>F04</td><td>rapina</td><td></td></tr><tr><td>C01</td><td>a causa di un incendio</td><td></td></tr><tr><td>C02</td><td>a causa di una strada chiusa per lavori in corso o frana</td><td></td></tr><tr><td>C03</td><td>a causa di una strada chiusa dalle autorità per eventi eccezionali</td><td></td></tr><tr><td>C04</td><td>a causa del maltempo: alluvione, neve o allagamento</td><td></td></tr><tr><td>C05</td><td>a causa di un terremoto</td><td></td></tr><tr><td>C06</td><td>a causa di un'eruzione vulcanica</td><td></td></tr><tr><td>D00</td><td>Non è stato trovato nessun nuovo indirizzo per predisporre un altro tentativo di invio.</td><td></td></tr><tr><td>D01</td><td>L'indirizzo non ha superato il processo di validazione.</td><td></td></tr></tbody></table>
