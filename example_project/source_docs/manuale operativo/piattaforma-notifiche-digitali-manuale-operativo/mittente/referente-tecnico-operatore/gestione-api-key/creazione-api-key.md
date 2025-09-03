# Creazione API Key

L’utente crea una nuova chiave premendo il bottone “Aggiungi”.

Nella nuova pagina l’utente otterrà un un secret da PN e dovrà fornire una descrizione ed, opzionalmente, i gruppi ai quali l’API Key appartiene. L’utente deve appartenere a questi gruppi.

Le APIKey associate a gruppi seguono le stesse regole previste per l'associazione tra un referente e un gruppo:

1. Una notifica creata dall’APIKey viene associata al gruppo
2. Può accedere al dettaglio solo di notifiche che sono associate a quel gruppo

A questo proposito si ricorda che al momento della creazione di una notifica il campo gruppo è obbligatorio:

* se l’operatore PA (o l’api-key) sono associati a un gruppo allora il campo gruppo, durante la creazione della notifica, è obbligatorio.
* se l’operatore PA (o l’api-key) NON sono associati a un gruppo allora il campo gruppo, durante la creazione della notifica, è facoltativo. (Indipendentemente dal fatto che su SelfCare siano censiti gruppi oppure no)
