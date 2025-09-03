# Specifiche tecniche dei PDF allegati alla notifica

I documenti pdf allegati alla notifica devono presentare una serie di caratteristiche tecniche, volti a permetterne la corretta elaborazione digitale e la successiva stampa fisica tramite processi industriali. E' responsabilità della PA mittente garantire che i documenti siano aderenti a queste note tecniche. Nel caso si rendesse impossibile l'invio cartaceo di un atto a fronte di un file pdf non conforme, la PA mittente si assume ogni responsabilità in merito all'interruzione del processo di notificazione.

I documenti inviati devono essere file pdf con le seguenti caratteristiche:

* Adobe PDF/A
* Le dimensioni “fisiche” della pagina devono essere conformi al formato A4 (210 x 297 mm)
* Al fine di regolare gli opportuni trattamenti di eventuali stampe fisiche viene imposta una “area di sicurezza” che regola lo spazio effettivamente utilizzabile per la stampa dei documenti da inoltrare. Tale area di sicurezza è definita in 1 (uno) centimetro per lato su un foglio di dimensioni standard A4, e dovrà essere lasciata libera a cura del cliente

Come insieme minimo di regole di partenza si faccia riferimento allo standard PDF/A definito nelle raccomandazioni ISO 19005-1:2005, a cui nel prosieguo verranno aggiunti ulteriori vincoli volti a garantire la produzione di stampe di qualità adeguata (a titolo di esempio, lo standard ISO 19005-1:2005 considera adeguata una risoluzione delle immagini a 50dpi, ma questa porta a stampe industriali di pessima qualità, per questa ragione, verrà richiesta una risoluzione maggiore).

Le dimensioni della pagina (e dimensioni della CROPBOX, TRIMBOX, ARTBOX e MEDIABOX) devono essere in formato A4 portrait (210 mm x 297 mm).

Non sono consentiti oggetti, anche se non contenenti grafica stampabile, fuori dalla media box.

Al fine di consentire gli opportuni trattamenti della stampa viene imposta una “area di sicurezza” che regola lo spazio effettivamente utilizzabile per la stampa dei documenti da inoltrare. Tale area di sicurezza è definita in 1 (uno) centimetro di area libera da grafica per ciascun margine su ciascun lato su un foglio di dimensioni di cui al punto precedente e, in questa area non devono essere presenti grafiche di alcun tipo.

I file PDF che possono essere accettati devono possedere le seguenti caratteristiche:

* PDF standard Adobe raccomandati PDF/X-3:2003 compliant
* Risoluzione delle immagini pari a 300 dpi (si sconsiglia di eccedere tale valore per non appesantire i flussi o di scendere sotto tale soglia per non degradare l’immagine)
* Nessuna protezione applicata, nessuna encryption
* Non sono ammessi elementi non strettamente testuali o grafici, come ad esempio note, commenti, file audio, multimediali, evidenziazioni, annotazioni, macro, script e così via
* Proibita la trasparenza
* Evitare Clipping Path
* Non usare per quanto possibile elementi grafici che si sovrappongono (totalmente o parzialmente)
* Fare in modo che il testo sia sempre renderizzato per ultimo (sopra tutto il resto)
* Il testo nero cosi’ come elementi grafici come barcode e datamatrix qualora definiti con informazione di colore devono essere definiti come 100% black (CMYK(0,0,0,100) e quindi 0% delle altre componenti cromatiche)
* Non sono ammesse pagine contenenti più di 1000 elementi
* Ridurre in generale la complessità delle pagine, ridurre al minimo gli anchor points, I layer non sono consentiti
* Total Area Coverage massimo 220% per carta standard
* Evitare di creare linee sottili  o testo sottile con colori composti in quanto potrebbero verificarsi fenomeni di sfocatura, meglio utilizzare in questi casi un colore base e.g.  CMYK(0,100,0,0)
* Non inserire profili (e.g. profili ICC) all’interno delle risorse grafiche e immagini in genere
* Non utilizzare scaling
* Non usare drop shadow style nel testo
* Non utilizzare Alternate Image, Embedded Page Thumbnails  e JavaScript
* Proibiti pdf monodocumento, creare invece un PDF unico multidocumento che sia autoconsistente cioè contenga tutte le risorse necessarie e mettendo a fattor comune le risorse stesse evitando proliferare di risorse ripetute o spezzettate e sparse nel file&#x20;
* Raggruppare il testo in entità ampie, righe o paragrafi, per favorire le performance.

Le immagini e gli oggetti grafici contenuti nei file PDF devono:

* Rispettare le dimensioni massime della pagina
* Rispettare i margini della pagina senza fuoriuscire dalla cropbox e dalla media box per nessuna componente anche priva di grafica
* Avere una risoluzione di 300 dpi&#x20;
* Essere sempre nel numero minimo indispensabile (ad es., evitare di disegnare una tabella utilizzando tante piccole righe a comporre le celle ognuna delle quali è un oggetto grafico distinto e separato)
* Ridurre la complessità, ridurre eccessivo uso di anchor points, evitare vector patterns complessi (eventualmente convertirli), ridurre al minimo il numero di layer e di risorse grafiche
* Per le stampe in b/n, si consiglia di evitare sfondi grigi ed in generale sfumature di grigio poiché sulle stampanti industriali in b/n non possono essere resi in modo soddisfacente
* Evitare l’uso di righe troppo sottili (inferiori o superiori di poco al punto tipografico) che potrebbero non essere rese alla risoluzione di stampa standard
* Evitare la rotazione o lo scaling delle immagini ed in genere di oggetti rasterizzati&#x20;
* Evitare di inserire oggetti grafici a tutta pagina, per esempio evitare di inserire una risorsa a tutta pagina A4 che contenga la grafica di solo logo e footer e tutti il resto bianco; in questi casi si richiede al cliente di spezzare le due risorse in grafiche piu’ piccole e che contengano solo quanto necessario

Gli algoritmi di compressione degli stream (es. immagini) supportati sono:

* LZW
* ZIP da verificare
* NON usare JPEG2000 e JBig2
* Raccomandati TIFF con LZW (non usare per TIFF la compressione 8)
* L’utilizzo di immagini JPEG a seconda della qualità rende necessario ridurre a 100 il numero massimo di immagini per file

L’uso di font outline (vettoriali) è preferibile in quanto la quantità di dati trasmessa con il documento è inferiore rispetto alla trasmissione di font bitmap. Si richiede:

* Utilizzare solo Font totalmente incorporati di tipo Type1 (outline) con encoding WinISOEncoding Latin1 (MS Windows1252 Latin1)
* Evitare i font Type3, Outline Bitmap e All And None
* Minima font size 6pt
* Non è ammesso l’uso della funzione di scaling (sia horizontal che vertical scaling) né sulle stringhe di testo né sull’intera pagina; non sono altresì ammesse altre funzioni di trasformazione dei font (skew, ecc.)
* I font utilizzati, anche quelli standard, devono essere totalmente incorporati all’interno del PDF (senza subsetting), font non presenti anche se standard potrebbero dare luogo ad una stampa non corretta
* I font utilizzati devono essere inclusi nel PDF una volta sola (no ripetizioni, no frammentazioni)
* Font uguali devono avere nomi uguali
* Limitare comunque il numero di font utilizzati nel PDF, il numero di font concesso verrà valutato sulla base degli esiti dei test preliminari a seconda delle caratteristiche del flusso
* Definire il testo colorato sempre come font senza convertirlo in immagine
* Font CID con grande numero di caratteri sono da valutare caso per caso per garantire le performance di velocità di stampa

Nel caso di utilizzo all’origine di font con codifica diversa da WinISOEncoding (MS Windows1252 Latin1), non viene garantita la conformità del prodotto finale stampato rispetto alla presentazione su video del documento stesso operata tramite Adobe Reader o altri visualizzatori PDF.
