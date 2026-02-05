# Vocabolario Controllato Archivio Storico dei Comuni d'Italia

### Contesto
Il vocabolario è stato creato nella sua prima versione all'interno della Piattaforma Digitale Nazionale dei Dati (o altrimenti nota come DAF) - PDND - grazie a due fonti dati principali conferite da Istat e da team di ANPR.
Attualmente è stato estratto direttamente dai dati del Territorio ISTAT.

**Stato**: stabile

### Fonti
[elenco dei comuni di ISTAT 2022-2023](https://www.istat.it/storage/codici-unita-amministrative/Archivio-elenco-comuni-codici-e-denominazioni_Anni_2022-2023.zip) (dato aperto in formato CSV con licenza CC-BY 3.0 IT)

### Processo di generazione del vocabolario controllato
Il vocabolario è stato generato utilizzando un processo che nella PDND è chiamato [triplificatore](https://github.com/italia/daf-semantic-triplifier).
Il triplificatore si interfaccia, mediante query SQL, a dati conferiti alla PDND e memorizzati su [Impala](https://impala.apache.org/) nel dataset estratto direttamente dai database di Istat che gestiscono lo storico dei comuni.

Gli script eseguono tipicamente una query SQL sulla Base dati di Istat e i dati ottenuti vengono poi utilizzati per la costruizione delle triple soggetto - predicato - oggetto del vocabolario

### Struttura del Vocabolario
Il vocabolario è strutturato seguendo il modello CLV - Core Location Vocabulary di OntoPiA e il modello [skos](http://www.w3.org/2004/02/skos/core#), quest'ultimo utilizzato per tutti gli altri vocabolari controllati della rete.

Un esempio di definizione di un Comune attualmente attivo è il seguente:

```
<https://w3id.org/italia/controlled-vocabulary/territorial-classifications/cities/025001-(1866-11-19)> a <https://w3id.org/italia/onto/CLV/City> , <https://w3id.org/italia/onto/CLV/Feature> , <https://w3id.org/italia/onto/CLV/AdminUnitComponent> , <http://www.w3.org/2004/02/skos/core#Concept> ;
	<http://www.w3.org/2002/07/owl#sameAs> <http://pt.dbpedia.org/resource/Agordo> , <http://fr.dbpedia.org/resource/Agordo> , <http://dbpedia.org/resource/Agordo> , <http://dati.isprambiente.it/id/place/25001> ;
	<http://www.w3.org/2004/02/skos/core#broader> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/provinces/025> ;
	<http://www.w3.org/2004/02/skos/core#broaderTransitive> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/regions/05> ;
	<http://www.w3.org/2004/02/skos/core#inScheme> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/cities> ;
	<http://www.w3.org/2004/02/skos/core#notation> "025001" ;
	<http://www.w3.org/2004/02/skos/core#preflabel> "AGORDO"@it ;
	<https://w3id.org/italia/onto/CLV/:hasGeographicalDistribution> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/geographical-distribution/2> ;
	<https://w3id.org/italia/onto/CLV/:hasHigherRank> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/regions/05> ;
	<https://w3id.org/italia/onto/CLV/hasDirectHigherRank> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/provinces/025> ;
	<https://w3id.org/italia/onto/CLV/hasIdentifier> <https://w3id.org/italia/data/identifiers/cities-identifiers/progressive-code/001> , <https://w3id.org/italia/data/identifiers/cities-identifiers/alphanumeric-istat-code/025001> , <https://w3id.org/italia/data/identifiers/cities-identifiers/numeric-istat-code/25001> , <https://w3id.org/italia/data/identifiers/cities-identifiers/cadastral-code/A083> ;
	<https://w3id.org/italia/onto/CLV/hasRankOrder> "4" ;
	<https://w3id.org/italia/onto/CLV/hasSOValidity> <https://w3id.org/italia/data/time-intervals/(1866-11-19)-(9999-12-31)> ;
	<https://w3id.org/italia/onto/CLV/situatedWithin> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/provinces/025> , <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/regions/05> ;
	<https://w3id.org/italia/onto/TI/modified> "2016-06-17"^^<http://www.w3.org/2001/XMLSchema#date> ;
	<https://w3id.org/italia/onto/l0/name> "AGORDO"@it .
```

### URI
Essendo un vocabolario controllato è stata usata la stessa convenzione utilizzata in generale per i vocabolari controllati: https://w3id.org/italia/controlled-vocabulary seguito da tutti i concetti specifici del vocabolario.
Ogni URI del comune termina con la "concatenazione" del codice ISTAT e della data di istituzione, due elementi stabili nel tempo (ad eccezione di casi molto particolari in cui questi due elementi cambiano per via di errori di trascrizione alle fonti; questi eventi sono comunque rari).

### Interlinking
Il vocabolario controllato è collegato al vocabolario controllato delle regioni e delle province. Inoltre sono stati materializzati collegamenti ai seguenti due dataset esterni:

1. [DBpedia](https://wiki.dbpedia.org/) (inglese, francese e portoghese)
2. [Linked Open Data di ISPRA](http://dati.isprambiente.it/dataset/i-luoghi/).


