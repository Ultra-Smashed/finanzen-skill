# Finanzen-Skill

Ein Skill für Claude. Der Finanzen-Skill funktioniert mit jedem Buchhaltungsprogramm, weil er mit Fotos, PDFs und CSV-Exporten arbeitet. Er macht aus Quittungsfotos eine Tabelle für den Steuerberater, prüft Rechnungen auf Pflichtangaben, rechnet eine Liquiditätsvorschau, schreibt Mahnungen und sucht Fördermittel. Der Abo-Finder findet jedes Abo auf deinem Konto, auch die vergessenen, und rechnet aus, was du im Jahr sparst. Kostenlos, MIT-Lizenz.

| Modul | Was es macht |
| --- | --- |
| **Belege** | Quittungsfotos werden zu einer Tabelle mit Datum, Lieferant, Netto, Steuer, Brutto und Kategorie, dazu umbenannte Dateien und eine Liste offener Fragen. |
| **Rechnungs-Check** | Jede Rechnung gegen die Pflichtangaben nach § 14 UStG, inklusive Kleinbetragsrechnung, Kleinunternehmer und E-Rechnung. |
| **Liquidität** | Kontostand, offene Rechnungen und feste Ausgaben ergeben eine Vorschau in drei Szenarien und den Monat, in dem es eng wird. |
| **Mahnwesen** | Von der freundlichen Erinnerung bis zur zweiten Mahnung, mit konkreten Fristen und dem Recht in Kürze. |
| **Abo-Finder** | Ein Skript liest deine Kontoauszüge und findet alles, was wöchentlich, monatlich oder jährlich abgebucht wird. Mit Summe pro Jahr und Kündigungstexten. |
| **Fördermittel** | Passende Programme von Bund, Land und KfW mit Voraussetzungen in Klartext und Quelle, sortiert nach Passung. |

## Installation

### Claude-App (Web, Desktop)

Am schnellsten: den Link in einen neuen Chat einfügen und Claude bitten, den Skill zu installieren:

```
https://github.com/Ultra-Smashed/finanzen-skill

Installier diesen Skill für mich.
```

Oder von Hand:

1. [`finanzen.zip`](https://github.com/Ultra-Smashed/finanzen-skill/raw/main/finanzen.zip) herunterladen (nicht entpacken).
2. In Claude unter **Settings → Capabilities** den Schalter **Code execution and file creation** einschalten. In der neueren Ansicht heißt er **Create and edit files**.
3. **Customize → Skills** öffnen, auf **+** klicken, dann **Create skill → Upload a skill** und die ZIP-Datei wählen.

Als Plugin: **Customize → Plugins**, bei den persönlichen Plugins auf **+**, dann **Add from a repository** und `Ultra-Smashed/finanzen-skill` eintragen.

Die Menünamen stehen hier so, wie Anthropic sie in der Hilfe nennt. In der deutschen Oberfläche können sie übersetzt sein.

### Claude Code

Als Plugin:

```
/plugin marketplace add Ultra-Smashed/finanzen-skill
/plugin install finanzen@finanzen
```

Oder den Ordner kopieren:

```bash
git clone https://github.com/Ultra-Smashed/finanzen-skill.git
cp -r finanzen-skill/skills/finanzen ~/.claude/skills/
```

## Benutzen

Einfach schreiben, was du brauchst, zum Beispiel:

> Hier sind meine Kontoauszüge der letzten sechs Monate. Finde alle Abos und sag mir, was ich sparen kann.

> Hier sind 30 Quittungsfotos vom Oktober. Mach daraus eine Tabelle für meinen Steuerberater.

> Prüf diese Rechnung, bevor ich sie rausschicke.

Der Skill ist keine Steuerberatung. Er ordnet, prüft auf Vollständigkeit und rechnet. Ob etwas absetzbar ist, klärst du mit deinem Steuerberater.

## Dateien

```
skills/finanzen/SKILL.md            Ablauf, Module, Regeln
skills/finanzen/modes/               eine Anleitung pro Modul
skills/finanzen/scripts/             Hilfsskripte (Python 3, ohne Zusatzpakete)
finanzen.zip                       derselbe Skill-Ordner als ZIP für die Claude-App
.claude-plugin/                     plugin.json, marketplace.json
```

Nach einer Änderung im Skill-Ordner die ZIP neu bauen: `cd skills && zip -r ../finanzen.zip finanzen`.

**Keine Steuerberatung.** Der Skill ordnet, prüft und rechnet. Steuerliche Fragen klärst du mit deinem Steuerberater.

Anleitung: [thanisch.co/wissen/guides/finanzen-skill-claude](https://thanisch.co/wissen/guides/finanzen-skill-claude)

MIT-Lizenz, siehe [LICENSE](LICENSE). Von [Christopher Thanisch](https://thanisch.co).
