# Vocabolario Controllato Titolo della Persona

**Stato**: instabile, incompleto

**Creator**:
[Agid](http://spcdata.digitpa.gov.it/browse/page/Amministrazione/agid),
[STLab](https://w3id.org/italia/data/organization/support-unit/cnr-Z6HZEH/stlab)

**Thread di discussione**: [Issue #58](https://github.com/italia/dati-semantic-assets/issues/58)

### Scopo del Vocabolario
Il vocabolario controllato *Titolo della Persona* ha lo scopo
di creare un vocabolario condiviso che permetta di specificare
i titoli di una persona (e.g. 'Sig', 'Dott', 'Prof' etc.).

#### Competency Questions

Di seguito una lista delle competency questions a cui il vocabolario offre una soluzione:

1. Quali titoli possono essere associati al nome di una persona?
2. Qual è la verbalizzazione di un certo titolo in una certa lingua?
3. Qual è il significato di un certo titolo?

### Contesto
Il vocabolario nasce nel contesto del progetto [EcoDigit](http://ecodigit.dtclazio.it) per
far fronte all'esigenza di rappresentazione dei titoli di una persona.

### Fonti
Non sono state trovate delle fonti autorevoli che forniscono una lista esaustiva di titoli di una persona.
Pertanto i termini specificati in questo vocabolario sono stati ricavati da enciclopedie e dizionari.

### Struttura del Vocabolario
Il vocabolario è strutturato seguendo il modello [skos](http://www.w3.org/2004/02/skos/core#).

Per ogni titolo della persona (e.g. 'Sig.ra') viene creata una nuova entità (e.g. https://w3id.org/italia/controlled-vocabulary/classifications-for-people/person-title/1) di tipo *skos:Concept* e *cpvapit:PersonTitle*.
Questa entità rappresenta un possibile titolo di una persona.
Al titolo sono associate delle label (specificate usando il predicato *skos:prefLabel) che
rappresentano la verbalizzazione del titolo in diverse lingue (le lingue sono specificate attraverso il language tag
del valore associato a *skos:prefLabel*).

Ad ogni titolo viene associato un identificativo (numero intero maggiore di 1).

Viene inoltre fornita una breve descrizione del significato di ogni titolo.

```
<https://w3id.org/italia/controlled-vocabulary/classifications-for-people/person-title/1>
 	    a  	skos:Concept , cpvapit:PersonTitle ;
 	  skos:inScheme <https://w3id.org/italia/controlled-vocabulary/classifications-for-people/person-title> ;
    clvapit:hasRankOrder "1" ;
    skos:notation "1" ;
    dct:identifier "1" ;
    skos:prefLabel "Sig.ra"@it ;
    skos:prefLabel "Mrs"@en ;
    skos:definition "English honorific used for women, usually for those who are married and who do not instead use another title."@en ;
    skos:definition "Abbreviazione di 'Signora'."@it .
```

### Contatti
Per maggiori informazioni riguardo questo vocabolario contattare

Luigi Asprino (STLab, ISTC-CNR) luigi.asprino@istc.cnr.it

Giorgia Lodi (Agid) giorgia.lodi@agid.gov.it
