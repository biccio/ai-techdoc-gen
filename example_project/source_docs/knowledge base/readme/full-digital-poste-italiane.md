# Full Digital - Poste Italiane

Questo sistema digitale è stato sviluppato per ottimizzare la gestione del processo delle immagini degli oggetti di ritorno. Esso consente di generare, in modalità completamente digitale, i documenti di consegna a domicilio che presso un ufficio postale, in conformità alla normativa vigente.

I documenti generati si trovano all'interno dell'evento **SEND\_ANALOG\_PROGRESS** all'interno di un file ZIP nella sezione `legalFactsIds` con i seguenti `deliveryDetailCode` :

#### Raccomandata 890

* RECAG001B - Consegnato Con Dematerializzazione - 23L
* RECAG002B - Consegnato a persona abilitata Con Dematerializzazione - 23L
* RECAG003B - Mancata consegna
* RECAG003E - Irreperibilità Assoluta Con Dematerializzazione - Plico e Indagine opzionalmente
* RECAG005B - Consegnato presso Punti di Giacenza Con Dematerializzazione - 23L
* RECAG006B - Consegna a persona delegata presso Punti di Giacenza - Dematerializzazione 23L
* RECAG007B - Mancata consegna presso Punti di Giacenza Con Dematerializzazione - Plico
* RECAG008B - Compiuta giacenza Con Dematerializzazione - Plico
* RECAG011B - In Giacenza - Con Dematerializzazione 23L

#### Raccomandata AR

* RECRN001B - Consegnato Con Dematerializzazione - AR
* RECRN002B - Mancata consegna Con Dematerializzazione - Plico
* RECRN002E - Irreperibilità Assoluta. È un evento finale. Con Dematerializzazione – Plico Indagine
* RECRN003B - Consegnato presso Punti di Giacenza Con Dematerializzazione - AR
* RECRN005B - Compiuta giacenza Con Dematerializzazione - Plico

#### Esempio in timeline

{% code fullWidth="true" %}
```json
  {
      "elementId": "SEND_ANALOG_PROGRESS.IUN_<iun>.RECINDEX_0.ATTEMPT_0.IDX_4",
      "category": "SEND_ANALOG_PROGRESS",
      "legalFactsIds": [
        {
          "key": "<url-Del-File-Da-Scaricare>",
          "category": "ANALOG_DELIVERY"
        }
      ],
      "details": {
        "recIndex": 0,
        "notificationDate": "<data-Notifica>",
        "deliveryDetailCode": "RECRN001B",
        "serviceLevel": "AR_REGISTERED_LETTER",
        "attachments": [
          {
            "id": "0",
            "documentType": "AR",
            "url": "<url-Del-File-Da-Scaricare>",
            "date": "<data-Evento>"
          }
        ]
     }
 }
```
{% endcode %}

### Documenti Generati

Il sistema produce i seguenti documenti in formato digitale:

<table><thead><tr><th>Modello</th><th align="center">Codice</th><th data-type="checkbox">c/o Domicilio</th><th data-type="checkbox">c/o Ufficio Postale</th></tr></thead><tbody><tr><td><strong>23L digitale</strong></td><td align="center">890</td><td>true</td><td>true</td></tr><tr><td><strong>ARCAD digitale</strong></td><td align="center">890</td><td>true</td><td>false</td></tr><tr><td><strong>AC digitale (23i)</strong></td><td align="center">A/R</td><td>true</td><td>true</td></tr></tbody></table>

La generazione dei documenti digitali riporta i seguenti elementi:

* **Firma digitale**: del personale addetto (portalettere), inclusi i casi di inesito.
* **Tratto grafico del ricevente**: richiesto solo se previsto dalla normativa.
* **Sigillo**: sigillo elettronico per la validità legale del documento.
* **Marca temporale**: per la tracciabilità del documento.

Il documenti prodotti sono archiviati all'interno di un file ZIP contenente:

1. **File XML**: contiene i dati relativi agli invii dei modelli 23L, 23i, e ARCAD.
2. **File XML di inesito** (DID): contiene i dettagli dell'inesito (solo in caso di notifiche non andate a buon fine).
3. **File PDF\***: una versione leggibile del file XML in formato PDF per consultazione.
4. **File XSD\*\*:** utilizzato per la validazione del file xml.

**NOTE**:\
\* il file PDF non riporta la firma digitale PADES perché i dati e la loro firma sono nel file XML. Il file PDF è generato dai dati contenuti nel XML solo al fine di rendere leggibile il contenuto.

\*\* dal 13.05.2025 tutti i file zip degli esempi contengono anche gli schemi in formato XSD per la validazione del file XML.

## Esempi

#### Raccomandata 890

* **23L digitale consegna c/o domicilio**

**File ZIP**

II file ZIP contiene il file XML firmato, gli schema XSD per la validazione e il file PDF relativi a una spedizione 890 per Raccomandata Mod. 23L consegnata a domicilio, con dettagli su codice di spedizione, data e luogo di accettazione e recapito.

{% file src="../.gitbook/assets/FPIN_Consegna_AG_da_ptl.zip" %}

#### Schema di Validazione

{% file src="../.gitbook/assets/Schema23L-v.1.0.xsd" %}

* **23L digitale consegna c/o ufficio postale**

#### File ZIP

II file ZIP contiene il file XML firmato, gli schema XSD per la validazione e il file PDF relativi a una spedizione 890 per Raccomandata Mod. 23L consegnata ad un ufficio postale, con dettagli su codice di spedizione, data e luogo di accettazione e recapito.

{% file src="../.gitbook/assets/SP04_23LFD_281526382192_381526382193.zip" %}

#### Schema di Validazione

{% file src="../.gitbook/assets/Schema23L_v.1.0daUP.xsd" %}

{% file src="../.gitbook/assets/SchemaDIDAGE.xsd" %}

* **ARCAD digitale**

**File ZIP**

II file ZIP contiene il file XML firmato, gli schema XSD per la validazione e il file PDF relativi a una spedizione 890 per ARCAD digiale , con dettagli su codice di spedizione, data e luogo di accettazione e recapito.

{% file src="../.gitbook/assets/WU2W_ARCAD_FD.zip" %}

#### Schema di validazione

{% file src="../.gitbook/assets/Schema_ARCAD.xsd" %}

#### Raccomandata A/R

* **23i digitale consegna c/o domicilio**

**File ZIP**

II file ZIP contiene il file XML firmato, gli schema XSD per la validazione e il file PDF relativi a una spedizione A/R per Raccomandata Mod. 23i consegnata a domicilio, con dettagli su codice di spedizione, data e luogo di accettazione e recapito.

{% file src="../.gitbook/assets/KUXW_Consegna_Racc_PTL.zip" %}

#### Schema di validazione

{% file src="../.gitbook/assets/Schema_23I_v.1.0.xsd" %}

{% file src="../.gitbook/assets/Schema_23I_v.2.0.xsd" %}

* **23i digitale consegna c/o ufficio postale**

#### **File ZIP**

II file ZIP contiene il file XML firmato, gli schema XSD per la validazione e il file PDF relativi a una spedizione A/R per Raccomandata Mod. 23i consegnata ad un ufficio postale, con dettagli su codice di spedizione, data e luogo di accettazione e recapito.

{% file src="../.gitbook/assets/9QM6_Consegna_Racc_da_UP.zip" %}

#### Schema di validazione

{% file src="../.gitbook/assets/Schema_DIDRK.xsd" %}

### Dettaglio dei campi del file XML

l file XML della Raccomandata 23L include campi per tracciare l’intera spedizione, come il codice identificativo dell’oggetto, la descrizione del documento inviato (es. atto giudiziario), la data e il luogo di accettazione e recapito, e i dettagli sul mittente. Questi campi certificano ogni fase del processo di notifica e rendono la spedizione conforme alle normative legali.

{% file src="../.gitbook/assets/Dettaglio campi per file FD PagoPA_V3.xlsx" %}
