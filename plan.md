# Piano di implementazione — DIGI HOUSE

## Obiettivo e approccio
Realizzare una landing page aziendale **single-page**, interamente contenuta in `index.html`, pronta da caricare in una repository GitHub Pages senza build, backend o dipendenze locali. Tailwind CSS verrà caricato tramite CDN; il codice CSS aggiuntivo, le illustrazioni architettoniche CSS e il JavaScript essenziale resteranno nello stesso file. Il modulo contatti sarà un'interazione front-end: controlla i campi obbligatori e mostra una conferma, mentre i recapiti diretti restano disponibili per il contatto reale. Nessun messaggio verrà salvato, in linea con la scelta di non attivare il power-up database.

## Architettura dei file
| Percorso | Responsabilità |
| --- | --- |
| `index.html` | Pagina completa: struttura semantica, stile Tailwind/CDN, CSS personalizzato, illustrazioni CSS, interazioni mobile e modulo. |
| `manus-routes.json` | Manifest della sola route pubblica `/`, utile alla preview di sviluppo. |
| `TODO.md` | Esiti richiesti e criteri di completamento del progetto. |

## Direzione creativa

### Movimento di design
**Industrial editorial retail**: l'eleganza ordinata dell'architettura italiana incontra l'immediatezza di un catalogo per professionisti. Le sezioni di serramentistica assumono un tono raffinato e materico, mentre il reparto tecnico usa moduli compatti e leggibili.

### Principi guida
1. **Contrasto controllato** — ampie superfici bianche e blu notte per un'identità affidabile, con una sola tinta accent per i dettagli operativi.
2. **Materia prima, gerarchia prima** — immagini grandi ma con testo nitido, griglie leggibili e micro-dati utili.
3. **Percorso a capitoli** — il visitatore attraversa casa, comfort e cantiere con passaggi visivi distinti.
4. **Mobile senza compromessi** — CTA grandi, colonne che si ricompongono e navigazione semplice anche su schermi stretti.

### Filosofia cromatica
Il **blu istituzionale #003366** è la firma di competenza, protezione e continuità del marchio. Bianco, azzurro nebbia e grigi caldi mantengono la pagina ariosa; il rame/arancio tenue viene impiegato solo per i segnali d'azione e le etichette funzionali. Il contrasto resta sempre netto per sostenere fiducia e leggibilità.

### Paradigma di layout
La pagina non è una sequenza di card identiche: parte da una **fascia hero architettonica asimmetrica**, passa a un capitolo editoriale sui serramenti, entra in una fascia tecnica ad alto contrasto e termina in un **mosaico-catalogo** per edilizia e ferramenta. I blocchi sono collegati da etichette numerate, linee sottili e bordi “da scheda tecnica”.

### Elementi firma
- Una **casa geometrica** dentro un quadrato aperto nel marchio e nelle texture lineari.
- Etichette numerate “01 / 02 / 03” come indici dei reparti.
- Un piccolo **punto rame** e riquadri con angoli netti per CTA, dati e categorie.

### Interazioni e animazioni
Le ancore del menu scorrono morbidamente alle sezioni. Il menu compatto mobile si apre con un pulsante accessibile. Card e pulsanti hanno un sollevamento leggero all'hover, mentre le immagini mantengono una lenta transizione di scala; le animazioni rispettano `prefers-reduced-motion`. Il form restituisce una conferma inline senza simulare un invio backend.

### Tipografia
**Manrope** per titoli, navigazione e CTA: geometrica e contemporanea. **DM Sans** per paragrafi, dati e moduli: neutra e ad alta leggibilità. Titoli grandi e serrati, testo funzionale arioso, maiuscole calibrate per le etichette dei reparti.

### Brand
> **DIGI HOUSE è il partner unico per trasformare casa e cantiere, dalla finitura che si vede al materiale che fa la differenza.**

Personalità: **solida, competente, contemporanea**.

### Voce
Chiara, concreta e orientata alla scelta. Non promette genericamente: nomina materiali, sistemi e risultati.

- “La porta giusta non chiude una stanza: completa un progetto.”
- “Dal cantiere alla finitura, trovi quello che serve. Subito.”

### Wordmark e colore firma
Il wordmark è composto da un simbolo monolineare di casa/porta aperta e dalla scritta **DIGI / HOUSE** su due livelli. Il blu firma è **#003366**; il rame di servizio è **#D47A36**.

## Contenuti e sezioni
1. **Header fisso** — wordmark, navigazione ad ancore e CTA “Parla con noi”.
2. **Hero** — messaggio sul partner per casa, edilizia e serramenti; CTA verso reparti e contatti; metriche di assortimento; immagine di villa con serramenti.
3. **Porte interne e finestre** — introduzione editoriale, immagine dedicata, tre card per porte, finestre e finiture con dettagli di prodotto.
4. **Avvolgibili e zanzariere** — fascia tecnica in blu, immagine dedicata, elenco dei sistemi su misura e quattro vantaggi funzionali.
5. **Ferramenta, materiali edili e pittura** — griglia compatta a otto categorie con icone; nastro informativo sull'assortimento professionale e fai-da-te.
6. **Punti di forza** — tre promesse operative sulla consulenza, disponibilità e consegna.
7. **Contatti** — recapiti dimostrativi, orari, mappa illustrativa, modulo con nome, email, telefono, argomento e messaggio.
8. **Footer** — richiamo al brand, collegamenti di sezione e dati essenziali.

## Compatibilità e pubblicazione
- HTML semantico, meta viewport, title e description descrittivi; nessun contenuto dipende da JavaScript per essere letto.
- Visuali architettoniche realizzate in CSS e integrate nel file, senza asset locali o URL di storage da copiare su GitHub Pages.
- Il form è gestito lato client; prima della pubblicazione reale, email, telefono e indirizzo dimostrativi dovranno essere sostituiti con i dati aziendali.
