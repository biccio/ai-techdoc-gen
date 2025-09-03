# Pagamento

Nella pagina che mostra i dettagli di una specifica notifica che non è stata annullata e che non è ancora stata pagata, alla voce “Da pagare” è presente un bottone che attiva il percorso di pagamento dell’Avviso di Pagamento associato alla notifica utilizzando pagoPA.

L’utente viene così indirizzato su una schermata dove sono già caricati tutti i dati necessari per procedere con il pagamento, il percorso è quello utilizzato da pagoPA per ogni altro tipo di pagamento.

<figure><img src="../../../../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

In caso di esito positivo, ricaricando la pagina il pagamento risulterà effettuato e sarà visibile in timeline l’evento di avvenuto pagamento.

La presenza di questo evento, o il fatto che il pagamento sia in corso, disabilita il bottone di pagamento presente sulla pagina.

E' anche possibile utilizzare l’avviso pagoPA o l’F24 allegati alla notifica per effettuare il pagamento attraverso canali diversi da quelli online offerti da PN. In questo caso non verrà aggiunta alla notifica un evento di avvenuto pagamento ed il bottone rimarrà abilitato fino a quando l’utente non entrerà nella notifica attraverso il portale o appIO successivamente all’avvenuto pagamento e, nel caso dell’F24, successivamente alla chiusura della posizione debitoria da parte della PA mittente.

ATTENZIONE: nel caso di destinatari multipli co-obbligati il pagamento della notifica è effettuato da uno di essi. La PA gestirà la riscossione delle spese di notifica degli altri co-obbligati al di fuori di Piattaforma Notifiche.
