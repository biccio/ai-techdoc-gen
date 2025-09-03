---
description: Spese di notifica sui modelli F24
---

# Pagamenti F24

SEND permette di inserire notifiche con allegati pagamenti tramite modello F24.

Poiché le spese di notifica non sono note a priori e sono variabili nel tempo non è possibile inserire nella notifica il file PDF del modello F24 che è per sua natura statico. Per questo motivo il PDF del modello F24 viene generato dalla piattaforma partendo da un file json contenente i metadati delle sue componenti alle quali viene aggiunto il costo di notifica al momento della generazione.

Il costo della notifica sarà aggiunto in fase di generazione del modello F24 sui pagamenti che riportano l'indicazione `applyCost=true` e nella riga del riquadro degli addebiti che riporta l'indicazione `applyCost=true`.

Per facilitare il controllo del file metadati per la generazione del file json è stato pubblicato il link [https://raw.githubusercontent.com/pagopa/pn-f24/main/docs/openapi/json-schema-from-deref-mod.json](https://raw.githubusercontent.com/pagopa/pn-f24/main/docs/openapi/json-schema-from-deref-mod.json) con lo schema Json di validazione.
