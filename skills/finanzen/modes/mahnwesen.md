# Modul Mahnwesen

Ziel: Offenes Geld kommt rein, ohne die Kundenbeziehung zu ruinieren.

## Ablauf

1. **Offene Rechnungen** erfassen (Liste, Export, Screenshot): Kunde, Rechnungsnummer, Datum, Betrag, Fälligkeit, schon gemahnt? Mit Code die Tage über Fälligkeit berechnen und sortieren.
2. **Stufe je Rechnung:**
   | Stufe | Wann | Ton | Inhalt |
   |---|---|---|---|
   | Zahlungserinnerung | 1–14 Tage über Fälligkeit | freundlich | „Vielleicht untergegangen?“, neue Frist 7 Tage |
   | 1. Mahnung | nach Ablauf der Erinnerung | sachlich | Rechnung, Betrag, Frist 7–10 Tage, Verzug erwähnen |
   | 2. Mahnung | nach Ablauf der 1. Mahnung | bestimmt | letzte Frist, Verzugszinsen/Pauschale, nächster Schritt |
   | Danach | | | gerichtliches Mahnverfahren (online-mahnantrag.de) oder Inkasso. Dafür Anwalt oder Inkassobüro, nicht Claude |
3. **Texte schreiben** mit konkreten Daten (Frist als Datum, nicht „in 7 Tagen“), Rechnungsnummer, Betrag, Zahlungsweg. Ohne Vorwurf, ohne Drohung, die der Mensch nicht umsetzen will.
4. **Verzugszinsen** nur auf Wunsch berechnen, mit Code, und den aktuellen Basiszinssatz der Bundesbank nachschlagen (Websuche), nicht aus dem Gedächtnis.

## Recht in Kürze (Stand November 2026, keine Rechtsberatung)

- Verzug: durch Mahnung nach Fälligkeit, oder automatisch 30 Tage nach Fälligkeit und Zugang der Rechnung; bei Privatkunden nur mit Hinweis darauf in der Rechnung (§ 286 BGB).
- Verzugszinsen: Firmen 9, Privat 5 Prozentpunkte über dem Basiszinssatz (§ 288 BGB).
- Firmenkunden: 40 € Verzugspauschale (§ 288 Abs. 5 BGB).
- Mahngebühren nur in angemessener Höhe für tatsächliche Kosten (Porto, Material), keine Fantasiebeträge.

## Vorbeugen

Am Ende drei Tipps passend zur Lage: kürzere Zahlungsziele, Anzahlungen, Rechnung am Tag der Abnahme, Verzugshinweis auf der Rechnung, Lastschrift für wiederkehrende Leistungen.
