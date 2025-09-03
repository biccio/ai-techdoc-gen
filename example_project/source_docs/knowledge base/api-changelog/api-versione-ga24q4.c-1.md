---
description: Aggiornamento versione 251Q1 ambiente produzione 28/03/2025
---

# API VERSIONE GA25Q1.B

#### Nuove funzionalità GA25Q1.B

* **Invio Manuale con pagamento:** consentito l'invio manuale di notifiche con pagamenti, tramite l'aggiunta di sezioni per posizioni debitorie pagoPA e F24 durante la creazione di nuove notifiche.
* **Controllo della pubblicazione dell'evento di accettazione della notifica:** aggiunta api di creazione di stream con configurazione **waitForAccepted** che controlla gli eventi di TIMELINE successivi all'accettazione o al rifiuto della notifica&#x20;

**Invio Manuale con pagamento**

Introdotta la possibilità di inviare notifiche dal portale mittente di SEND con i pagamenti. Accedendo e facendo click su crea nuova notifica compariranno due nuove sezioni dedicate alla posizione debitoria che consentono di caricare una posizione pagoPa e/o un F24. Link alla guida specifica: [https://developer.pagopa.it/send/guides/manuale-operativo/piattaforma-notifiche-digitali-manuale-operativo/mittente/amministratore-referente-amministrativo/invio-manuale-di-una-notifica](https://developer.pagopa.it/send/guides/manuale-operativo/piattaforma-notifiche-digitali-manuale-operativo/mittente/amministratore-referente-amministrativo/invio-manuale-di-una-notifica)

## Controllo della pubblicazione **dell'evento di accettazione della notifica**

In fase di creazione di uno stream è stato introdotto il campo **waitForAccepted** un flag booleano che controlla la pubblicazione l'evento di accettazione della notifica.&#x20;

Per gli stream di **TIMELINE**, se impostato su true, garantisce che l'evento REQUEST\_ACCEPTED sia pubblicato sullo stream prima degli eventi successivi del workflow-

Gli eventi dello stato `IN_VALIDATION`  vengono comunque pubblicati. Per gli stream di tipo `STATUS`, assicura che il primo stato pubblicato sia **ACCEPTED** o **REFUSED**. Sebbene normalmente gli eventi dello stream arrivino nell'ordine cronologico in cui si verificano, non è garantito che possano arrivare in un ordine differente. Gli ID dello stream sono comunque sempre ordinati e crescenti, ma la data dell'evento potrebbe non essere sempre successiva agli eventi precedenti.

