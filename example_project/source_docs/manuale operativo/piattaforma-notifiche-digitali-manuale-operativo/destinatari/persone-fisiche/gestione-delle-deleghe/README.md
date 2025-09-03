# Gestione delle deleghe

Le persone fisiche possono delegare altre persone fisiche o persone giuridiche ad accedere alle proprie notifiche per proprio conto.

Il processo parte dal delegante che crea una delega per un delegato e prosegue con il delegato che accetta la delega. La delega ha un periodo di validità che determina quali notifiche possono essere visualizzate dal delegato, ovvero quelle che hanno data di creazione all’interno del periodo di validità.

La data di inizio validità è posta a 120 giorni prima della creazione della delega. La data di fine validità è posta in un qualsiasi istante successivo alla data di creazione.

La delega può essere associata ad una particolare PA mittente in modo tale da restringere il campo di validità della delega stessa. Se non specificata, la delega permette l’accesso alle notifiche generate da tutte le PA.

La delega viene accettata dal delegato inserendo in PN un codice che viene fornito dal delegante e che era stato a sua volta fornito da PN in fase di creazione della delega.

La delega può essere in qualsiasi momento revocata dal delegante o rifiutata dal delegato.

Delegante e delegato possono avere una sola delega attiva in un dato istante. Seil delegante vuole cambiare/aggiungere gli enti per il quale ha fornito la delega (o la data di scadenza ad esempio), deve revocare la delega già attiva e crearne una nuova con le informazioni aggiornate.

Una delega assume uno dei seguenti stati: in attesa di conferma, attiva, revocata, rifiutata, conclusa.

Per tutta la durata di validità di una delega attiva, il delegato potrà accedere a PN e decidere di agire per conto del delegante, potendo in tal senso effettuare qualunque operazione che il delegante avrebbe potuto effettuare sulle proprie notifiche.

Periodicamente PN verifica le deleghe presenti a sistema e rimuove quelle con data di fine validità precedente all’istante corrente.
