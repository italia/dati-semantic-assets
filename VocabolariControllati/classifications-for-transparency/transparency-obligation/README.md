Vocabolario controllato degli obblighi di trasparenza
=======================

## Descrizione

Il presente vocabolario controllato codifica gli obblighi di trasparenza della PA a supporto dell'ontologia della Trasparenza [Transparency-AP_IT](https://w3id.org/italia/onto/Transparency/). L'informazione relativa al vocabolario è stata ottenuta analizzando i [riferimenti](#rifnorm) sotto riportati. In particolare gli obblighi di trasparenza enunciati dalle normative sono stati definiti come istanze delle classi [skos:Concept](http://www.w3.org/2004/02/skos/core#Concept) e [Transparency Obligation](https://w3id.org/italia/onto/Transparency/TransparencyObligation), eventualmente collegati tra loro tramite la relazione di sotto-obbligo. Agli obblighi sono stati collegati le relative voci delle sezioni di "Amministrazione Trasparente" istanziate nel vocabolario [transparency-titulus](https://w3id.org/italia/controlled-vocabulary/classifications-for-trasparency/transparency-titulus) e i contenuti informativi da pubblicare istanziati nel vocabolario [transparency-subject](https://github.com/italia/dati-semantic-assets/blob/master/VocabolariControllati/classifications-for-transparency/transparency-subject/transparency-subject.ttl). Inoltre sono state specificate informazioni come riferimenti normativi, frequenza di aggiornamento di pubblicazione, data di validità.

## Corrispondenze di applicazione tra obblighi di trasparenza e organizzazioni

Il vocabolario è stato impostato per esplicitare quali obblighi di trasparenza si applicano alle diverse organizzazioni o tipologie di amministrazioni. Tali corrispondenze sono state materializzate in un file separato [transparency-obligation-organization](https://github.com/italia/dati-semantic-assets/blob/master/VocabolariControllati/classifications-for-transparency/transparency-obligation/transparency-obligation-organization.ttl) per motivi di organizzazione e manutenzione in previsione di futuri aggiornamenti.
Allo stato attuale, l'insieme delle corrispondenze riguarda le seguenti pubbliche amministrazioni e tipologie (rif.  [Elenco analitico delle amministrazioni pubbliche](https://www.istat.it/it/archivio/190748)):

* Presidenza del Consiglio dei Ministri e Ministeri (corrispondenze sulle singole amministrazioni)

    * Presidenza del Consiglio dei Ministri
    * Ministero degli Affari Esteri e della Cooperazione Internazionale
    * Ministero del Lavoro e delle Politiche Sociali
    * Ministero dell’Ambiente e della Tutela del Territorio e del Mare
    * Ministero dell’Economia e delle Finanze
    * Ministero dell’Interno
    * Ministero dell’Istruzione, dell’Università e della Ricerca
    * Ministero della Difesa
    * Ministero della Giustizia
    * Ministero della Salute
    * Ministero delle Infrastrutture e dei Trasporti
    * Ministero delle Politiche Agricole Alimentari e Forestali
    * Ministero dello Sviluppo Economico
    * Ministero per i Beni e le Attività Culturali e per il Turismo

* Regioni e Province autonome (corrispondenze sulle singole amministrazioni)
* Comuni (corrispondenze sulla tipologia di amministrazione)

A supporto di questa parte è pubblicato un file di mapping R2RML (transparency-obligation-organization.rml.ttl) che si basa su due tabelle, transparency-obligation-administration.csv e transparency-obligation-administration-category.csv, ottenute dalla trasposizione del file csv transparency-obligation-organization.csv. In questo modo vengono specificati ulteriori elementi di dettaglio per gestire l'integrazione successiva delle corrispondenze di applicazione per le organizzazioni e le categorie di amministrazione mancanti.

## Sviluppi futuri

* Consolidare le corrispondenze riguardanti le amministrazioni considerate, anche attraverso un rapporto più stretto con ANAC
* Estensione ad altre amministrazioni e tipologie di amministrazioni

## Riferimenti <a name="rifnorm"></a>

* [Decreto Legislativo 14 marzo 2013, n. 33](http://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2013-03-14;33) aggiornato dal [Decreto Legislativo 25 maggio 2016, n. 97](http://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2016-05-25;97) e descritto nel dettaglio dalla delibera ANAC 1310/2016
* [Delibera numero 50 del 04 luglio 2013](https://www.anticorruzione.it/-/delibera%C2%A0numero-50-del-04/07/2013-1?inheritRedirect=true&redirect=%2Frisultati-ricerca%3Fq%3DDelibera%2520numero%252050%2520del%252004%2520luglio%25202013%26sort%3DpublishDate_sortable-)
* [FAQ in materia di trasparenza (ANAC)](https://www.anticorruzione.it/chiedilo-ad-anac/-/categories/119067?p_r_p_resetCur=true&p_r_p_categoryId=119067#nav-filtercategoryNavigation45586)
* Siti istituzionali delle pubbliche amministrazioni in oggetto
