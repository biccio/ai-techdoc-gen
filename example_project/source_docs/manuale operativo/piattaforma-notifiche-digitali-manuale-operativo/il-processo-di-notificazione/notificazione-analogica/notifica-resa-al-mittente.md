# Notifica resa al mittente



## Resa al mittente per destinatario deceduto

Durante il processo di notificazione analogica, uno tra gli eventi possibili di rendicontazione è la mancata consegna per destinatario dichiarato deceduto dall'addetto al recapito. In questo caso SEND conclude il workflow della notifica con un evento di resa al mittente e un nuovo stato della notifica di “reso al mittente”.\


Si specifica che SEND si limita a riportare l'informazione fornita dall'addetto al recapito e risultante sull'esito della notifica, senza effettuare ulteriori verifiche in merito (es. verifica tramite accesso a ANPR).

Per permettere agli enti mittenti di apprendere della mancata consegna della notifica per decesso del destinatario verrà introdotto un nuovo elemento di timeline e un nuovo stato della notifica “resa al mittente".\


In caso di notifica multi-destinatario, il workflow della notifica si concluderà con lo stato di "reso al mittente" solo nel caso in cui tutti i destinatari dovessero risultare deceduti.

**ATTENZIONE**: Per recepire anche lo stato della timeline "reso al mittente" in caso di notifiche effettuate verso destinatari dichiarati deceduti dall'addetto al recapito, è necessario effettuare un aggiornamento tecnologico delle API SEND, come da specifiche rese disponibili su DevPortal. \
In attesa che venga effettuato da parte dell'Ente Mittente, il predetto adeguamento alle nuove API sarà possibile allo stesso visualizzare lo stato della notifica accedendo all’Area Riservata di SEND.

\
\
