---
description: >-
  In questa pagina è descritto il funzionamento del normalizzatore degli
  indirizzi
---

# Normalizzatore

Il normalizzatore degli indirizzi è il componente della piattaforma che decide se un indirizzo fisico è "postalizzabile" e nel caso tenta di correggere gli errori per aumentare le probabilità di successo nella consegna cartacea.&#x20;

* I caratteri supportati nella _denomination_ verranno estesi a tutti quelli del charset ISO\_LATIN\_1.
* L’indirizzo verrà fatto transitare attraverso il normalizzatore che deciderà, provando diversi livelli di normalizzazione, se l’indirizzo è da considerarsi "postalizzabile" o meno. Le notifiche con indirizzi postalizzabili verranno accettate, rifiutate in caso contrario.

Il normalizzatore in caso di:

* **indirizzo italiano** proverà a correggere CAP(_zip_) e Provincia(_province_) utilizzando Città (_municipality_), Località/Frazione (_municipalityDetails_) e Via (_address_).
* **indirizzo estero** validerà esclusivamente il paese (_country)_. In questo caso i caratteri accettati saranno sempre e comunque gli ISO\_LATIN\_1.

In questo scenario:

* potranno essere inseriti **CAP generici** visto che sarà compito dell normalizzatore provare a correggerli. Se non dovesse riuscire la notifica verrebbe però rifiutata.
* potranno essere inserite **città con più di 36 caratteri**, il normalizzatore ne restituirà una versione compatibile con i sistemi di postalizzazione.
