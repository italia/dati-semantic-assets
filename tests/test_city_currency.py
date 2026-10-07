"""Currency check for the cities controlled vocabulary (issue #225).

Checks that every city concept marked current in
VocabolariControllati/territorial-classifications/cities/cities.csv
(DATA_FINE_VALIDITA equal to the sentinel 31-12-9999) carries an ISTAT
code that is current in the ISTAT register, and that every current ISTAT
code is represented.

The reference register is a vendored snapshot of the ISTAT
Elenco-comuni-italiani.xlsx
(https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.xlsx),
kept in tests/data/istat_current_city_codes.txt so the test stays
hermetic. The snapshot must be refreshed at every ISTAT variation
bulletin, together with currency.shacl (see
VocabolariControllati/territorial-classifications/generate_currency_shape.py).
Note that the CSV flavour of the same ISTAT endpoint lags the XLSX
flavour: as of August 2026 the CSV still predates the Sardinian recoding
in force since 1 January 2026, so the XLSX is authoritative.

The two currency assertions are marked xfail until the vocabulary is
refreshed for the 2026 ISTAT variations (Sardinian recoding, Lirio,
Castegnero Nanto): as of August 2026 the vocabulary carries 380 dead
codes as current and lacks 378 current codes. Drop the markers once the
vocabulary is updated.
"""

import csv
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CITIES_CSV = (
    ROOT / "VocabolariControllati/territorial-classifications/cities/cities.csv"
)
ISTAT_SNAPSHOT = ROOT / "tests/data/istat_current_city_codes.txt"

OPEN_SENTINELS = ("", "31-12-9999")


def load_vocab_current_codes():
    codes = set()
    with open(CITIES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row["DATA_FINE_VALIDITA"] or "").strip() in OPEN_SENTINELS:
                codes.add(row["CODICE_COMUNE"].strip())
    return codes


def load_istat_current_codes():
    codes = set()
    with open(ISTAT_SNAPSHOT, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                codes.add(line)
    return codes


@pytest.fixture(scope="module")
def vocab_codes():
    return load_vocab_current_codes()


@pytest.fixture(scope="module")
def istat_codes():
    return load_istat_current_codes()


def test_known_answer_roma(vocab_codes, istat_codes):
    assert "058091" in vocab_codes
    assert "058091" in istat_codes


@pytest.mark.xfail(
    reason="cities vocabulary predates the 2026 ISTAT variations (issue #225)",
    strict=False,
)
def test_no_stale_codes_marked_current(vocab_codes, istat_codes):
    stale = sorted(vocab_codes - istat_codes)
    assert not stale, f"{len(stale)} stale codes marked current: {stale[:10]}..."


@pytest.mark.xfail(
    reason="cities vocabulary predates the 2026 ISTAT variations (issue #225)",
    strict=False,
)
def test_all_current_codes_present(vocab_codes, istat_codes):
    missing = sorted(istat_codes - vocab_codes)
    assert not missing, f"{len(missing)} current ISTAT codes missing: {missing[:10]}..."
