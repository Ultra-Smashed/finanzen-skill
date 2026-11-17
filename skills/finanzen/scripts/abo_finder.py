#!/usr/bin/env python3
"""Findet wiederkehrende Abbuchungen (Abos, Verträge) in Kontoauszügen.

Eingabe: eine oder mehrere CSV-Dateien aus dem Online-Banking (Sparkasse, Volksbank,
DKB, ING, N26, Commerzbank, Qonto, Kontist, Lexware-/sevDesk-Export …). Spalten werden
automatisch erkannt. Alternativ eine CSV mit den Spalten datum;betrag;empfaenger;zweck.

  python3 abo_finder.py umsaetze.csv [weitere.csv] [--json]

Ausgabe: Liste wiederkehrender Abbuchungen mit Rhythmus, letztem Betrag und Kosten pro Jahr.
"""
import csv
import io
import json
import re
import statistics
import sys
from collections import defaultdict
from datetime import datetime

DATUM = ["buchungstag", "buchungsdatum", "datum", "valuta", "wertstellung", "date", "booking date", "valuedate"]
BETRAG = ["betrag", "betrag (eur)", "umsatz", "amount", "betrag in eur", "soll/haben"]
NAME = ["beguenstigter/zahlungspflichtiger", "begünstigter/zahlungspflichtiger", "empfänger", "empfaenger",
        "zahlungsempfänger", "name zahlungsbeteiligter", "auftraggeber/empfänger", "auftraggeber / begünstigter",
        "payee", "counterparty", "name", "partner name", "gegenkonto name"]
ZWECK = ["verwendungszweck", "buchungstext", "purpose", "description", "reference", "zweck", "beschreibung"]


def finde(spalten, kandidaten):
    low = {s.lower().strip(): s for s in spalten}
    for k in kandidaten:
        if k in low:
            return low[k]
    for k in kandidaten:
        for l, s in low.items():
            if k in l:
                return s
    return None


def zahl(s):
    s = str(s).strip().replace("€", "").replace("EUR", "").replace(" ", "")
    if not s:
        return None
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def datum(s):
    s = str(s).strip()
    for f in ("%d.%m.%Y", "%d.%m.%y", "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(s[:10], f).date()
        except ValueError:
            pass
    return None


def lies(pfad):
    raw = open(pfad, "rb").read()
    for enc in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    zeilen = text.splitlines()
    # Kopfzeilen von Banken überspringen: erste Zeile mit Datum- und Betrag-Spalte suchen
    start = 0
    for i, z in enumerate(zeilen[:40]):
        l = z.lower()
        if any(d in l for d in DATUM) and any(b in l for b in ("betrag", "amount", "umsatz")):
            start = i
            break
    rest = "\n".join(zeilen[start:])
    dialect = csv.Sniffer().sniff(rest[:5000], delimiters=";,\t")
    reader = csv.DictReader(io.StringIO(rest), dialect=dialect)
    sp = reader.fieldnames or []
    cd, cb, cn, cz = finde(sp, DATUM), finde(sp, BETRAG), finde(sp, NAME), finde(sp, ZWECK)
    if not cd or not cb:
        sys.exit(f"FEHLER: In {pfad} keine Datums- oder Betragsspalte erkannt. Spalten: {sp}")
    out = []
    for r in reader:
        d, b = datum(r.get(cd, "")), zahl(r.get(cb, ""))
        if d is None or b is None:
            continue
        out.append({"datum": d, "betrag": b, "name": (r.get(cn) or "").strip() if cn else "",
                    "zweck": (r.get(cz) or "").strip() if cz else ""})
    return out


def schluessel(u):
    basis = u["name"] or u["zweck"]
    basis = re.sub(r"\d{4,}", "", basis.lower())
    basis = re.sub(r"[^a-zäöüß ]", " ", basis)
    worte = [w for w in basis.split() if len(w) > 2 and w not in ("gmbh", "sepa", "lastschrift", "ihre", "kundennr", "mandat", "referenz", "europe", "sarl", "inc", "ltd", "und")]
    return " ".join(worte[:3]) or basis.strip()[:30]


def rhythmus(tage):
    m = statistics.median(tage)
    for name, ziel, tol, faktor in (("wöchentlich", 7, 2, 52), ("monatlich", 30, 5, 12), ("vierteljährlich", 91, 12, 4),
                                     ("halbjährlich", 182, 20, 2), ("jährlich", 365, 30, 1)):
        if abs(m - ziel) <= tol:
            return name, faktor
    return None, None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(1)
    umsaetze = [u for p in args for u in lies(p) if u["betrag"] < 0]
    gruppen = defaultdict(list)
    for u in umsaetze:
        gruppen[schluessel(u)].append(u)
    abos = []
    for k, us in gruppen.items():
        us.sort(key=lambda u: u["datum"])
        # gleiche Buchung doppelt aus zwei Dateien entfernen
        uniq = []
        for u in us:
            if not uniq or (u["datum"], u["betrag"]) != (uniq[-1]["datum"], uniq[-1]["betrag"]):
                uniq.append(u)
        if len(uniq) < 2:
            continue
        tage = [(b["datum"] - a["datum"]).days for a, b in zip(uniq, uniq[1:]) if (b["datum"] - a["datum"]).days > 0]
        if not tage:
            continue
        name, faktor = rhythmus(tage)
        betraege = [abs(u["betrag"]) for u in uniq]
        if not name or (max(betraege) - min(betraege)) > 0.35 * statistics.median(betraege):
            continue
        letzter = abs(uniq[-1]["betrag"])
        abos.append({"name": uniq[-1]["name"] or k, "rhythmus": name, "anzahl": len(uniq),
                     "letzter_betrag": round(letzter, 2), "pro_jahr": round(letzter * faktor, 2),
                     "zuletzt": str(uniq[-1]["datum"]), "zweck_beispiel": uniq[-1]["zweck"][:80]})
    abos.sort(key=lambda a: -a["pro_jahr"])
    if "--json" in sys.argv:
        print(json.dumps({"abos": abos, "summe_pro_jahr": round(sum(a["pro_jahr"] for a in abos), 2)}, ensure_ascii=False, indent=2))
        return
    print("Name\tRhythmus\tLetzter Betrag\tPro Jahr\tZuletzt\tAnzahl")
    for a in abos:
        print(f"{a['name']}\t{a['rhythmus']}\t{a['letzter_betrag']:.2f}\t{a['pro_jahr']:.2f}\t{a['zuletzt']}\t{a['anzahl']}")
    print(f"\nSumme wiederkehrend pro Jahr: {sum(a['pro_jahr'] for a in abos):.2f} € ({len(abos)} Posten)")


if __name__ == "__main__":
    main()
