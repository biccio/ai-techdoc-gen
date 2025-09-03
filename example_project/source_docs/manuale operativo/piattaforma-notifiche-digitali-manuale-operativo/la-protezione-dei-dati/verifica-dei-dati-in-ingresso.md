# Verifica dei dati in ingresso

PN garantisce la corretta attribuzione dei documenti informatici alla notifica attraverso l’utilizzo di hash SHA-256. La PA mittente, nel momento in cui genera la richiesta di creazione di una notifica, fornisce a PN anche lo SHA-256 del documento. PN calcola lo SHA-256 del documento ricevuto e lo confronta con ciò che la PA ha fornito. Solo in caso di coincidenza tra le due hash la richiesta di creazione della notifica è accettata.

Inoltre, PN verifica la validità dei CF forniti della PA mittente e la presenza dell'indirizzo fisico del destinatario/i per garantire la possibilità di effettuare la notificazione.
