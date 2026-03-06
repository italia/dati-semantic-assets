Indicator-AP_IT Profilo Italiano dell'ontologia sugli indicatori
================================================================

L’ontologia **è da riternersi PRELIMINARE e quindi INSTABILE**; essa consente di modellare il mondo degli indicatori (esempi di indicatori possono essere Key Performace Indicator, indicatori smart city, indicatori COVID-19, indicatori del mondo HER -Higher Education & Research, ecc.).

L'ontologia nasce nel contesto del lavoro della task force data-driven per l'emergenza COVID-19 al fine di fornire un modello comune nazionale per la rappresentazione degli indicatori COVID-19. Tuttavia il modello è stato pensato, fin dalla sua prima definizione, per essere sufficientemente generale e applicarsi quindi anche a dati relativi a indicatori di altri domini.

Il modello è rappresentato nello schema grafico ontologico che segue.

![modello ontologia indicatori](Indicator.png)

Nel modello si possono distinguere tre moduli principali:

+ **Indicatori**: modulo non disponibile a livello di ontologie nazionali. Il modulo è stato pensato per essere il più generale possibile. Il modulo si caratterizza per la distinzione tra indicatore e il suo calcolo. Questo consente anche di poter definire vocabolari controllati di specifici indicatori mantenendo separata la parte di calcolo vero e proprio basato un metodo e su metriche specifiche. Alcuni concetti rappresentati in questa parte del modello quali per esempio Purpose derivano dal modello Measure dello standard in ambito sanitario HL7/FHIR;

+ **Valori e Misure** già modellato attraverso l'ontologia MU. Questo modulo rappresenta valori (di qualunque tipo) e unità di misura.

+ **Modulo delle Osservazioni** già modellato attraverso l’ontologia della sensoristica IoT di cui qui si considera solo il pattern Observation-FeatureOfInterest-ObservationParameter-ObservationValue. Quest’ultimo modello segue due standard disponibili a livello internazionale ed europeo: lo standard INSPIRE Observation & Measurements e lo standard Web della Semantic Sensor Network Ontology.  

Il modulo sugli indicatori è stato pensato tenendo conto del decreto del ministero della salute del 30 aprile 2020 sugli indicatori COVID-19 della fase 2A e visionando una serie di ontologie analoghe già presenti allo stato dell’arte, anche scientifico [1, 2, 3, 4, 5, 6, 7].

Il razionale che sta dietro al modello può essere così riassunto: gli indicatori sono calcolati in base a un metodo di calcolo, a diverse metriche elementari. Il calcolo fornisce un valore dell'indicatore. Il processo che sottende il calcolo presuppone la raccolta di una serie di osservazioni su determinate caratteristiche di interesse e proprietà che complessivamente alimentano una sorgente dati usata per il calcolo degli indicatori. Nel caso specifico degli indicatori COVID-19, dalle tabelle degli indicatori del decreto del Ministero della Salute del 30 aprile 2020 emerge come gli indicatori siano calcolati sulla base di una certa fonte dati (nel modello questo concetto è chiamato DatumSource), che può essere il sistema di sorveglianza integrata COVID-19 dell’ISS oppure rilevazioni dirette delle regioni.  


Il modello proposto consente di rispondere a domande di competenza (competency question) come le seguenti; si noti che non è una lista esaustiva ma è un primo elenco a titolo d’esempio:

CQ1: Quali sono gli indicatori di tipo processo?

CQ2: Quali sono gli indicatori del Comune XXX?

CQ3: Qual è la fonte dati per un certo indicatore?

CQ4: Qual è la frequenza di aggiornamento ci un certo indicatore?

CQ5: Qual è il valore di un certo indicatore?

CQ6: Qual è la metrica usate per calcolare un certo indicatore?

CQ9: Quali sono le proprietà che forniscono i dati per un certo indicatore?


Riferimenti bibliografici
=========================

[1] https://arxiv.org/pdf/1909.01602.pdf

[2] http://energy.linkeddata.es/em-kpi/ontology/index-en.html

[3] https://save-sd.github.io/2018/accepted/nuzzolese/index.html#endnote_15

[4] http://ontology.eil.utoronto.ca/ISO37120.html#d4e78

[5] https://www.researchgate.net/publication/262675058_A_Foundation_Ontology_for_Global_City_Indicators

[6] https://www.semanticscholar.org/paper/A-Knowledge-Based-Search-Tool-for-Performance-in-Beyan-Bayka/3a972ecf7835770f47937ee84d949935e2c56b79

[7] https://www.researchgate.net/publication/220538113_Ontology_for_Software_Metrics_and_Indicators


Autori
======

Agenzia per l'Italia Digitale - Giorgia Lodi

Dipartimento per la Trasformazione Digitale - Ministro per l'innovazione tecnologica e la digitalizzazione - Maria Claudia Bodino, Roberto Polli
