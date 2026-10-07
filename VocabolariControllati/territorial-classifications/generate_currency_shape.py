#!/usr/bin/env python3
"""Generate the data-driven SHACL currency shape for the cities vocabulary.

Reads the current ISTAT register (Elenco-comuni-italiani.xlsx, from
https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.xlsx)
and emits currency.shacl next to this script, containing an sh:in list of
every current ISTAT municipality code. The shape targets only city
concepts with an open validity interval, so historical concepts never
trigger it.

The generated file must be regenerated at every ISTAT variation bulletin
("Codici statistici delle unita' amministrative territoriali: novita'").
Note that the CSV flavour of the same ISTAT endpoint can lag the XLSX
flavour (as of August 2026 the CSV still predates the Sardinian recoding
in force since 1 January 2026), so the XLSX is the authoritative input.

The file is intentionally NOT named rules.shacl: pyshacl evaluates sh:in
in quadratic time, so the 7,894-item list is impractical under the
pre-commit toolchain, although the shape is valid SHACL and runs fine on
Jena-class engines. The equivalent check for this repository's CI is
tests/test_city_currency.py.

Usage: python generate_currency_shape.py /path/to/Elenco-comuni-italiani.xlsx

Requires openpyxl (not part of the tox environment; this is a maintainer
tool, not a CI step).
"""
import sys
from datetime import date
from pathlib import Path

OUT = Path(__file__).resolve().parent / "currency.shacl"

HEADER = """#
# GENERATED FILE, do not edit by hand.
#   Regenerate with generate_currency_shape.py from the current ISTAT
#   Elenco-comuni-italiani.xlsx.
#
# Source register state: {sheet} ({n} comuni), generated {today}.
#
# Proposed in answer to italia/dati-semantic-assets#225: a currency rule
#   that fails when a city concept with an open validity interval carries
#   an ISTAT code that is no longer current in the ISTAT register
#   (suppressed comune or recoded unit, e.g. the Sardinian recoding in
#   force since 1 January 2026).
#
# This shape is for Jena-class SHACL engines; the pre-commit pyshacl
#   toolchain evaluates sh:in in quadratic time, so the executable CI
#   equivalent is tests/test_city_currency.py.
#
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix owl:     <http://www.w3.org/2002/07/owl#> .
@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
@prefix clvapit: <https://w3id.org/italia/onto/CLV/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <https://localhost.example/TerritorialCurrencyShacl> .

ex:
 a owl:Ontology ;
  sh:declare [
    sh:prefix "skos" ;
    sh:namespace "http://www.w3.org/2004/02/skos/core#"^^xsd:anyURI ;
  ] ;

  sh:declare [
      sh:prefix "clvapit" ;
      sh:namespace "https://w3id.org/italia/onto/CLV/"^^xsd:anyURI ;
  ] ;
.

ex:CurrentCityCodeShape
  a sh:NodeShape ;

  sh:target [
    a sh:SPARQLTarget ;
    sh:prefixes ex: ;
    sh:select \"\"\"
      SELECT ?this
      WHERE {{
        ?this a clvapit:City .
        ?this a skos:Concept .
        ?this clvapit:hasSOValidity ?interval .
        FILTER(CONTAINS(STR(?interval), "(9999-12-31)"))
      }}
      \"\"\" ;
  ];

  sh:property [
    sh:path skos:notation ;
    sh:message "This concept has an open validity interval but its ISTAT code is not in the current ISTAT register ({sheet})." ;
    sh:in (
"""

FOOTER = """    ) ;
  ] ;
  .
"""


def main(xlsx_path):
    import openpyxl

    wb = openpyxl.load_workbook(xlsx_path, read_only=True)
    ws = wb.active
    rows = ws.iter_rows(values_only=True)
    next(rows)
    codes = []
    for r in rows:
        if r[4] is None:
            continue
        code = str(r[4]).strip()
        if len(code) == 6 and code.isdigit():
            codes.append(code)
    codes.sort()
    assert "058091" in codes, "Roma missing: refusing to generate"
    assert len(codes) > 7000, "implausibly small register: refusing to generate"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(
            HEADER.format(sheet=ws.title, n=len(codes), today=date.today().isoformat())
        )
        for i in range(0, len(codes), 10):
            chunk = codes[i:][:10]
            f.write("      " + " ".join('"%s"' % c for c in chunk) + "\n")
        f.write(FOOTER)
    print("wrote", OUT, "with", len(codes), "current codes, register state:", ws.title)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(
            "Usage: generate_currency_shape.py /path/to/Elenco-comuni-italiani.xlsx"
        )
    main(sys.argv[1])
