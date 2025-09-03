# Notificazione digitale

In presenza di almeno un domicilio digitale, PN notifica l’AAR attraverso PEC o SERCQ. In presenza di domicili digitali diversi, questi verranno utilizzati, ove disponibili, secondo il seguente ordine di priorità:

1. Domicilio digitale di piattaforma (configurato dal destinatario nella sezione "Recapiti" della piattaforma)
2. Domicilio digitale speciale (indicato dall’ente mittente nella creazione della notifica; si invita l’ente ad informare debitamente i destinatari che abbiano eletto un domicilio speciale presso l’ente stesso relativamente alle modalità e tempistiche di aggiornamento, modifica e/o cancellazione del predetto domicilio, nonché degli effetti conseguenti a tali modifiche e/o cancellazioni.)
3. Domicilio digitale generale (fornito da IniPEC, IPA o INAD)

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

PN interromperà il tentativo di invio al primo successo. Nel caso di fallimento nel primo tentativo di invio digitale (es. casella postale satura o indisponibilità momentanea a causa di disservizio del fornitore della PEC o SERCQ), la notifica in via digitale sarà ritentata dopo almeno 7 giorni dal primo fallimento. La distanza tra il primo ed il secondo tentativo può variare da 7 a 9 giorni in base al carico del sistema.

PN deve effettuare l’invio a tutti i domicili digitali individuati in fase di avvio del workflow, compresi eventuali domicili per i quali è stato individuato un cambiamento tra il primo e il secondo tentativo, questo comporta la necessità di effettuare un tentativo al nuovo indirizzo a prescindere da quale sia stato l'esito del tentativo sull'indirizzo precedente.&#x20;

Nel caso in cui il processo di notificazione attraverso PEC o SERCQ fallisca anche al secondo tentativo, la piattaforma genera e mette a disposizione un Avviso di Mancato Recapito (AMR) collegato allo IUN visibile al destinatario nel caso egli acceda al portale di PN e verifichi lo Stato della notifica. Per informare comunque il destinatario dell'esistenza della notifica, PN invia l’AAR con raccomandata semplice al domicilio fisico del destinatario (nazionale o internazionale a seconda dell'indirizzo fornito dalla PA mittente).

La notifica si perfeziona per il destinatario dopo 7 giorni dalla consegna dell’AAR attraverso PEC o SERCQ oppure 15 giorni dopo la generazione dell’AMR. In particolare se l'avviso di avvenuta ricezione AAR è consegnato/l’eventuale AMR é generato al destinatario dopo le ore 21.00, il numero di giorni indicati in precedenza per il perfezionamento viene incrementato di 1 (art. 26 D.L. 76/2020).
