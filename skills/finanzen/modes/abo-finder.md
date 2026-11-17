# Modul Abo-Finder

Ziel: Jedes Abo und jeder wiederkehrende Vertrag auf dem Konto wird sichtbar, auch die vergessenen, mit der Ersparnis pro Jahr.

## Eingabe

Kontoauszüge der letzten 6–12 Monate (mindestens 3), am besten als CSV-Export aus dem Online-Banking. Kreditkarten- und PayPal-Abrechnungen dazunehmen, viele Abos laufen darüber.
- PDF-Kontoauszüge: Umsätze mit Code (z. B. pdfplumber) in eine CSV mit `datum;betrag;empfaenger;zweck` übertragen.
- Screenshots: Umsätze ablesen und in dieselbe CSV schreiben.

## Ablauf

1. `python3 scripts/abo_finder.py auszug1.csv [auszug2.csv …] --json`
   Findet Abbuchungen an denselben Empfänger mit wöchentlichem, monatlichem, vierteljährlichem, halbjährlichem oder jährlichem Rhythmus und ähnlichem Betrag.
   Ohne Befehle: dieselbe Logik selbst mit Code.
2. **Nacharbeiten:**
   - Sammelempfänger (PayPal, Apple, Google, Amazon) aufschlüsseln: Verwendungszweck lesen, nachfragen
   - Jahresabos mit nur einer Abbuchung im Zeitraum: nach typischen Anbietern suchen (Domains, Versicherungen, Software) und als „vermutlich jährlich“ markieren
   - Preiserhöhungen erkennen (Betrag gestiegen) und markieren
3. **Einordnen** mit dem Menschen: jede Position als ✅ brauche ich · 🔍 prüfen · ❌ kündigen. Erst die Liste zeigen, dann fragen.
4. **Ergebnis:**
   - Tabelle: Anbieter, Rhythmus, Betrag, Kosten pro Jahr, zuletzt abgebucht, Einordnung
   - **Summe pro Jahr** gesamt und **Ersparnis pro Jahr** für alles mit ❌ (mit Code)
   - Doppelte Leistungen („3 Cloud-Speicher“, „2 Video-Tools“)
   - Kündigungstexte für jede ❌-Position (kurz, mit Kundennummer-Platzhalter, „zum nächstmöglichen Zeitpunkt“, Bitte um Bestätigung). In Deutschland müssen viele Online-Verträge über einen Kündigungsbutton kündbar sein; darauf hinweisen.

Private und geschäftliche Abos getrennt ausweisen, wenn das Konto gemischt ist.
