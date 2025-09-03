---
description: >-
  Informazioni utili sulla generazione dei client e sulle modalità di utilizzo
  delle API
---

# Generazione client e definizioni delle API

#### Generazione dei client <a href="#generazione-dei-client" id="generazione-dei-client"></a>

E' possibile generare il client per tutti i linguaggi di programmazione, con il tool **openapi-generator** la cui documentazione è presente al seguente link: [https://openapi-generator.tech](https://openapi-generator.tech/) Dopo aver scaricato il tool sulla propria macchina, bisognerà lanciare il seguente comando:

```
openapi-generator-cli generate -i <urlFileSwagger> -g <lang> -o <dest>
```

sostituendo:

* **\<urlFileSwagger>:** con la url del file Swagger del quale si vuole generare il client. E' possibile utilizzare: [https://raw.githubusercontent.com/pagopa/pn-delivery/v2.1.0/docs/openapi/api-external-b2b-pa-bundle.yaml](https://raw.githubusercontent.com/pagopa/pn-delivery/v2.1.0/docs/openapi/api-external-b2b-pa-bundle.yaml)​​
* **\<lang>:** con il linguaggio per il quale si vuole generare il client
* **\<dest>:** con il path nel quale si vuole generare il client

#### Client b2b Java <a href="#client-b2b-java" id="client-b2b-java"></a>

E' anche possibile utilizzare il [pn-b2b-client](https://github.com/pagopa/pn-b2b-client) pubblico sviluppato da PagoPA ed utilizzare le classi Java in esso contenute per sviluppare la propria soluzione

#### Importare le definizioni delle API su Postman <a href="#importare-le-definizioni-delle-api-su-postman" id="importare-le-definizioni-delle-api-su-postman"></a>

Per importare le definizioni su Postman bisogna cliccare su "import", poi selezionare "Link" ed inserire il seguente url: [https://raw.githubusercontent.com/pagopa/pn-delivery/v2.1.0/docs/openapi/api-external-b2b-pa-bundle.yaml](https://raw.githubusercontent.com/pagopa/pn-delivery/v2.1.0/docs/openapi/api-external-b2b-pa-bundle.yaml)​Poi modificare i seguenti parametri delle collections ottenute:

{% content-ref url="integrazione-send-pdnd-interoperabilita/creazione-richiesta-di-fruizione-generazione-voucher-per-send-uat-piattaforma-notifiche.md" %}
[creazione-richiesta-di-fruizione-generazione-voucher-per-send-uat-piattaforma-notifiche.md](integrazione-send-pdnd-interoperabilita/creazione-richiesta-di-fruizione-generazione-voucher-per-send-uat-piattaforma-notifiche.md)
{% endcontent-ref %}
