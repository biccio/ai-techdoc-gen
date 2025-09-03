# Log di sistema - anonimizzazione e conservazione

PN anonimizza le informazioni che possono ricondurre all’identificazione di persone. Ad esempio, PN utilizza un servizio che genera una versione anonimizzata del CF e che mantiene permanentemente la relazione tra il CF e la sua versione anonimizzata.

Le informazioni presenti nei log di sistema e nei record di notifica sono anonimizzate.

Solo i documenti allegati alle notifiche e le attestazioni opponibili ai terzi possono contenere informazioni in chiaro.

I log di sistema vengono prodotti su database, indicizzati per versione anonimizzata del CF e partizionati per data. Ogni record di log può contenere più di un CF anonimizzato.

PN non effettua operazioni di update o delete sui record di log.

I log vengono conservati per al massimo 10 anni. I log degli ultimi 120 giorni sono sempre presenti in DB per accesso rapido, i log vengono inoltre trasferiti giornalmente su file system e conservati con le stesse modalità utilizzate per gli atti opponibili ai terzi.

I log di accesso a mezzo SPID o CIE sono conservati per 24 mesi.

I log necessari per comprovare le informazioni contenute nelle attestazioni opponibili ai terzi sono conservati per 10 anni.

Gli audit log che non sono necessari per comprovare le informazioni contenute nelle attestazioni opponibili ai terzi sono conservati per 5 anni.

I log di sistema di PN non necessari per comprovare le informazioni contenute nelle attestazioni opponibili ai terzi sono conservati per 36 mesi.
