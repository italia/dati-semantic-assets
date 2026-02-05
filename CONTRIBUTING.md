# Contribuire a Ontopia

Questo repository contiene diversi tipi di asset semantici sviluppati nel tempo.
Per le Ontologie, le ultime versioni sono disponibili nella directory `latest/` di ogni ontologia,
e.g. `CPV/latest/`; il contenuto di queste directory corrisponde a quello delle directory con la versione più recente.

Ogni modifica deve passare da una specifica pull request, usando il git flow:
non è possibile effettuare commit direttamente su master.
I branch dovrebbero seguire la sintassi `$username-$issue` (e.g. `ioggstream-1`), ed essere creati
a valle di un apposito issue.

Le PR prima di essere integrate (merge) dovrebbero essere "spremute" (squash) in modo da
non introdurre modifiche inutili.

## Testare i contenuti

Il repository utilizza [pre-commit](https://pre-commit.com/) per controllare che le modifiche siano sempre valide:
prima di iniziare a sviluppare bisogna installare pre-commit, configurarlo e lanciare i test contenuti in
[.pre-commit-config.yaml](.pre-commit-config.yaml).

```bash
pip install pre-commit
pre-commit install
pre-commit run -a
```

I test di base includono la rimozione di spazi e l'uniformità sintattica in generale dei file.

Esistono anche test ulteriori, eseguibili tramite [tox](https://tox.readthedocs.io/en/latest/):

```bash
pip install tox
tox
```

Questi test controllano anche la correttezza dei link a github contenuti nei file .ttl.

## Test specifici per ogni tipo di asset

Il software per la validazione sintattica è pubblicato su https://github.com/teamdigitale/json-semantic-playground
ed i controlli sono configurabili in [.pre-commit-config.yaml](.pre-commit-config.yaml).
Ad esempio, il modulo `validate-csv` analizza solo i file .csv contenuti in `VocabolariControllati` e sottodirectory,
ad esclusione dei path che contengono scriptR2RML e vocs-deprecated.

```yaml
  -   id: validate-csv
      files: >-
        ^VocabolariControllati/.*\.csv
      exclude: >-
        ^.*(scriptR2RML|vocs-deprecated).*

```

I test verificano i file contenuti in [Ontologie](Ontologie) e [VocabolariControllati](VocabolariControllati),
e in particolare:

- la validità sintattica e la presenza di alcuni predicati obbligatori nei file .ttl come indicato nei file rules.shacl;
  presenti nelle varie directory;
- la coerenza dei contenuti dei .csv usando il framework [frictionlessdata](https://frictionlessdata.io),
  eventualmente utilizzando i metadati ulteriori contenuti nei file datapackage.json o datapackage.yaml;

## Continuous integration

Il repository è configurato con delle Github Actions in [.github/workflows/](.github/workflows/)
che verificano sia i test di pre-commit che quelli di tox.

