---
description: >-
  Approfondimento sull'attualizzazione delle spese di notifica di SEND nei
  pagamenti
---

# Pagamenti pagoPA

L'attualizzazione della posizione debitoria è un'operazione che permette di integrare le spese di notifica sostenute da Piattaforma Notifiche per la spedizione, al costo richiesto dall'atto spedito dalla PA Mittente verso il destinatario.\


L'integrazione con il sistema di pagamento pagoPA può avvenire in due modalità:

* Sincrona
* Asincrona

## Modalità Sincrona

Nella modalità sincrona la posizione debitoria è presso il sistema dell'Ente Creditore (EC) che coincide nella maggior parte dei casi con l'ente mittente della notifica, ma potrebbe essere anche un altro ente.

Le spese di notifica variano in base al processo di spedizione eseguito per una notifica e possono subire variazioni nel tempo (es: a seguito di un secondo invio cartaceo); pertanto sarà necessario richiamare il servizio **notificationPrice**, che restituisce il costo sostenuto per la spedizione **aggiornato all'istante in cui viene chiamato**, durante la fase di pagamento, ovvero dopo che il destinatario ha avuto accesso alla notifica e tenta di effettuare il pagamento.

### Descrizione del processo step-by-step

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption><p>Diagramma del processo di attualizzazione delle spese di Notifica</p></figcaption></figure>

1. **Accesso Notifica**: il destinatario/delegato accede al dettaglio della notifica e clicca sul pulsante “Paga”
2. **Pagamento**: il destinatario/delegato viene mandato sul sito checkout di pagoPA passando i dati Codice Ente Creditore, Numero Avviso.
3. **Attualizzazione**: pagoPA nella fase di verifica e nella fase di attivazione chiede all’ente creditore di attualizzare l’importo
4. **Richiesta costo notifica**: l’ente creditore chiama Piattaforma Notifiche per conoscere il costo delle spese di notifica e aggiungerli all’importo dell’atto passando i dati Codice Ente Creditore, Numero Avviso (chiamata al servizio **notificationPrice**)

#### Ottimizzazione del processo limitando le chiamate al servizio **notificationPrice** tramite analisi degli eventi da stream di timeline <a href="#ottimizzazioni" id="ottimizzazioni"></a>

E' possibile limitare le richieste di attualizzazione delle spese di notifica, utilizzando lo stream degli eventi di timeline per intercettare il momento nel quale il costo non subirà più variazioni, eseguendo l'operazione di attualizzazione in anticipo.&#x20;

Di seguito delle linee guida per eseguire questa ottimizzazione:

* **il costo della notifica non varia** dopo il perfezionamento della notifica (per presa visione o per decorrenza termini) a seguito degli eventi **REFINEMENT** e **NOTIFICATION\_VIEWED**, cioè dopo che la notifica è transitata in stato **EFFECTIVE\_DATE** o **VIEWED**.\
  **NOTA:** si evidenza che l'evento **NOTIFICATION\_VIEWED** non corrisponde automaticamente al Perfezionamento per presa visione, ma rappresenta solamente l'atto di presa visione della notifica da parte del destinatario. Il Perfezionamento per presa visione può essere attribuito **solamente** quando la presa visione dell'atto avviene **prima** del Perfezionamento per decorrenza termini(vedi:[https://app.gitbook.com/o/KXYtsf32WSKm6ga638R3/s/8hvzBYw259fYwQSqzmf6/\~/changes/15/knowledge-base-di-piattaforma-notifiche/focus-sul-perfezionamento-della-notifica](../perfezionamento-della-notifica.md)).
* **il costo della notifica può variare**:
  * Nel **workflow digitale** solo in caso di fallimento di tutti gli invii su domicilio digitale e viene inviata una raccomanda semplice.
  * Nel **workflow cartaceo** viene attribuito un primo costo per la spedizione associato al primo tentativo di invio della raccomandata AR/890. In caso di fallimento del primo tentativo potrebbe essere attribuito un altro costo, legato al secondo tentativo di invio a seguito del reperimento di un altro indirizzo attraverso l'indagine del postino o dal recupero dai registri nazionali.

E' possibile quindi ottimizzare il processo descritto al punto "**4 Richiesta costo notifica**", eseguendo l’attualizzazione delle spese di notifica chiamando il servizio **noificationPrice** al verificarsi di uno degli eventi descritto sopra (**REFINEMENT,NOTIFICATION\_VIEWED**) ed anticipare quindi questa operazione a prima che il destinatario effettui il tentativo di pagamento.\
**NOTA:** Il Partner pagoPA in questo caso però deve essere avvisato del fatto che è stata completata in anticipo l'operazione di attualizzazione delle spese di notifica, per allineare i propri terminali.

### Modalità Asincrona

Nella modalità asincrona di integrazione con pagoPA le posizione debitorie sono caricate preventivamente dall'EC sul sistema Gestione Posizioni Debitorie (GPD) di pagoPA.\
All'atto del pagamento pagoPA chiamerà GPD per recuperare l'importo dell'atto collegato al numero avviso e il costo di notifica che viene continuamente aggiornato da SEND nel momento stesso in cui di verifica l'evento che genera una variazione del costo di notifica.

Questa soluzione presenta una maggior robustezza perché le chiamate per recuperare i dettagli della posizione debitoria avvengono su sistemi in gestione PagoPA senza interagire con i sistemi remoti dell'EC e non necessità da parte dell'EC di attualizzare le spese di notifica implementando la chiamata alle API di SEND.&#x20;

