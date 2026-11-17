# Modul Liquidität

Ziel: Der Mensch sieht, ob sein Geld in drei bis sechs Monaten noch reicht, und was er heute tun kann.

## Daten (eine Nachricht, nur was fehlt)

1. Kontostand heute (alle Geschäftskonten)
2. Offene Rechnungen an Kunden mit Fälligkeit (Liste oder Export)
3. Feste Ausgaben pro Monat (oder Kontoauszüge der letzten 3 Monate als CSV, dann mit `scripts/abo_finder.py` und eigener Auswertung ermitteln)
4. Erwartete Aufträge mit Betrag und Wahrscheinlichkeit
5. Steuern: Vorauszahlungen (Einkommen-, Gewerbesteuer), Umsatzsteuer-Zahllast, Termine. Ohne Zahl als offene Position markieren, nicht schätzen.
6. Eigene Entnahmen pro Monat (Selbstständige) bzw. Gehälter

## Rechnen (mit Code)

Monat für Monat, 3–6 Monate: Anfang + Eingänge − Ausgaben = Ende. Drei Szenarien:
- **Vorsichtig:** nur offene Rechnungen, jede 2 Wochen später als fällig
- **Erwartet:** + Aufträge mit Wahrscheinlichkeit ≥ 70 %
- **Gut:** + alle möglichen Aufträge

Sicherheitsreserve: 2 bis 3 Monate Fixkosten (Standard 2).

## Zeigen

1. Tabelle pro Monat und Szenario
2. Ampel: Wann fällt das vorsichtige Szenario unter die Reserve, wann unter null?
3. Liniendiagramm (in einer kleinen HTML-Seite oder als Bild), wenn Dateien möglich sind
4. Drei Hebel mit Wirkung in Euro, z. B. offene Rechnungen eintreiben (Modul Mahnwesen), Anzahlungen bei neuen Aufträgen, Abos kündigen (Modul Abo-Finder), Steuervorauszahlung anpassen lassen (Steuerberater)

Ehrlich bleiben: Eine Vorschau ist so gut wie die Zahlen. Annahmen sichtbar auflisten.
