# Modul Belege

Ziel: Aus einem Stapel Quittungsfotos wird eine saubere Tabelle, mit der der Steuerberater sofort arbeiten kann.

## Ablauf

1. **Jede Datei ansehen** (Fotos, PDFs, Mails mit Rechnungen). Bei PDFs mit mehreren Seiten: jede Rechnung einzeln erfassen.
2. **Erfassen** je Beleg: Datum · Lieferant · Rechnungsnummer · Beschreibung · Netto · USt-Satz · USt-Betrag · Brutto · Zahlungsart (bar, Karte, Überweisung, PayPal) · Kategorie · Dateiname · Hinweis.
   Kategorien (üblich in der EÜR): Wareneinkauf, Fremdleistungen, Miete/Raumkosten, Telefon/Internet, Software/Abos, Bürobedarf, Fortbildung, Reisekosten, Fahrzeugkosten, Bewirtung, Werbung, Versicherungen/Beiträge, Porto, Bankgebühren, Geringwertige Wirtschaftsgüter (bis 800 € netto), Sonstiges. Der Steuerberater entscheidet final.
3. **Prüfen** und in „Hinweis“ markieren:
   - USt fehlt oder ist falsch gerechnet (mit Code prüfen)
   - Rechnung über 250 € brutto ohne vollständige Anschrift des Empfängers (siehe Rechnungs-Check)
   - Bewirtung ohne Anlass und Teilnehmer
   - unleserlich, doppelt, privat?
   - ausländischer Anbieter ohne USt (mögliches Reverse Charge, Steuerberater fragen)
4. **Dateien umbenennen:** `JJJJ-MM-TT_Lieferant_Betrag.ext`.
5. **Ausgeben:**
   - Tabelle als Excel/CSV (Summe pro Kategorie und Gesamtsumme als zweites Blatt bzw. darunter)
   - ZIP mit umbenannten Dateien, wenn Dateien möglich sind
   - Liste „Bitte noch klären“ mit den markierten Belegen

Fehlt ein Beleg für eine Abbuchung, das Modul Liquidität bzw. einen Abgleich mit dem Kontoauszug anbieten.
