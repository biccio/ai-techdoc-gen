# Stato della notifica



Gli stati attraverso i quali inizia e si conclude il processo di notificazione, sono i seguenti:

* **Depositata**: quando la notifica risulta correttamente creata su PN dalla PA; tale stato iniziale determina il perfezionamento per il mittente e genera l'attestazione opponibile ai terzi di presa in carico
* **Invio in corso**: quando è in corso il processo di spedizione del’AAR per almeno un destinatario; tale stato raccoglie quindi i diversi elementi di timeline relativi ai singoli tentativi d'invio
* **Consegnata**: quando il processo di spedizione è terminato per tutti i destinatari ed almeno uno di essi è stato raggiunto e genera l'attestazione opponibile ai terzi di notifica digitale
* **Irreperibile:** quando non è stato possibile raggiungere nessuno dei destinatari, ovvero quando tutti i destinatari che dovevano essere raggiunti con raccomandata AR/890 non erano conosciuti all'indirizzo utilizzato per la spedizione (irreperibilità totale) ed i destinatari che dovevano essere raggiunti con PEC/SERCQ avevano i recapiti legali saturi, inattivi o invalidi.
* **Resa al mittente**: quando il recapitista dichiara il destinatario della notifica deceduto. Solo se non ci sono altri destinatari della notifica per i quali il workflow ha un altro esito.
* **Perfezionata per decorrenza termini**: quando la notifica si è perfezionata per decorrenza termini (a norma di legge) per almeno un destinatario e se nessuno dei destinatari ha preso visione della notifica stessa.
* **Avvenuto accesso**: quando almeno un destinatario, entro od oltre i termini di decorrenza, ha acceduto agli atti della notifica.
* **Annullata:** nel caso la notifica sia stata annullata della PA mittente.

I termini di perfezionamento previsti per legge (art. 26 DL 76/2020) sono i seguenti:&#x20;

1\)  il  settimo  giorno  successivo  alla  data   di   consegna dell'avviso di avvenuta ricezione in formato elettronico,  risultante dalla ricevuta che il gestore  della  casella  di  posta  elettronica certificata  o  del  servizio  elettronico  di  recapito  certificato qualificato del destinatario trasmette alla piattaforma. Se l'avviso di avvenuta ricezione e' consegnato al destinatario dopo le ore 21.00, il termine di  sette giorni si computa a decorrere dal giorno successivo;

2\) nei casi di casella postale satura, non valida o  non  attiva,  il quindicesimo giorno successivo alla data del deposito dell'Avviso di mancato recapito in piattaforma (Attestazione di mancato recapito digitale);

3\) il  decimo  giorno  successivo  al  perfezionamento della notificazione dell'avviso di avvenuta ricezione in formato cartaceo;

In ogni caso, se anteriormente a quanto previsto e descritto per il perfezionamento per decorrenza termini, il destinatario o il suo delegato accedono alla notifica tramite la piattaforma, la notificazione è **perfezionata per presa visione**. PN genera l’Attestazione opponibile ai terzi indicante la data e l’ora di avvenuto accesso alla notifica e lo Stato della notifica in time line è quello di "Avvenuto accesso".

ATTENZIONE: **Nel caso di destinatari multipli**, lo stato aggregato ha solamente valenza informativa sullo stato complessivo della notifica. In particolare lo stato di perfezionamento può non corrispondere all'effettiva data di perfezionamento per ogni diverso destinatario.
