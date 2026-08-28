# Drop Filter Glue – Skript für Vorbereitung der Daten für DFG-Monitoring (FZ Jülich)

Erstellen einer Datei aus mehreren Excel-Tabellen/Arbeitsblättern mit unterschiedlichem Spalten-Mapping

Webseite zum Monitoring: https://go.fzj.de/DFG-OAPK

Input: eine oder mehrere Exceldatei(en) mit jeweils einem oder mehreren Tabellenblättern, die jeweils Artikel und sämtliche für das Monitoring benötigte zugehörige Artikeldaten inkl. Kosten enthalten.

Output: eine Exceldatei, deren Daten mit einmal Kopieren des entsprechenden Bereichs in die Vorgabedatei des Monitorings eingefügt werden können.

## Vorbereitung

- Artikel ohne DOI manuell prüfen, ob schon veröffentlicht; wenn ja, aber ohne DOI, erfolgt Meldung in Tabellenblatt „ohne DOI“ (manuell ausfüllen); wenn nein, erfolgt die Meldung im nächsten Jahr (ggf. Filter für das jeweilige Tabellenblatt einstellen, dass nur Artikel mit DOI berücksichtigt werden) 
- In Datei `col_mappings.py` alle zu verwendenden Dateien und Tabellenblätter und die jeweiligen Details angeben (siehe unten)
- Prüfen (aktuell mit PHAME), ob alle DOIs in Crossref abrufbar sind -> Tippfehler etc. korrigieren
- Alle verwendeten Dateien in Kopie in den Ordner input_files einfügen. (Letzter Schritt, wenn keine Korrekturen mehr in den Dateien erfolgen!)

## Das Skript

1.	Importiert Daten aus verschiedenen xlsx-Dateien und Tabellenblättern
2.	Wendet je Input gegebene Filter auf die Daten an, z.B. Kostenstelle, Rechnungsnummer
3.	Bringt die Spalten in die vorgegebene Reihenfolge
4.	Übernimmt von Datumsangaben für die Spalten „Förderjahr“ und „Rechnungsjahr“ nur das Jahr

## Datei col_mappings.py

In `col_mappings.py` werden vor der Ausführung von `drop_filter_glue.py` folgende Angaben zu den Dateien gemacht, je Datensatz/Input:
- Dateiname (Excel-Datei)
- Tabellenblattname
- Zu überspringende Zeilen im Tabellenblatt (bei Angabe von ‚0‘ wird in der ersten Zeile des Blattes die Überschriftenzeile erwartet)
- Filter, die auf die eingelesenen Daten angewendet werden. Bsp.: Nur Zeilen mit Kostenstelle 54321
Hier müssen die Spaltennamen aus der Inputdatei verwendet werden!
- Mapping: Spaltennamen im Output in der entsprechenden Reihenfolge und jeweils die zu verwendende Spalte aus dem Input. Soll für eine Output-Spalte kein Input übernommen werden, wird der Output-Spalte ein leerer String zugewiesen.
- Standardwerte, z.B. Förderjahr immer 2021

#Lizenz
Das Projekt ist unter der MIT-Lizenz lizenziert. Details siehe LICENSE-Datei.

# Autorinnen
Elena Gandert, 2023-2025 (Code und Mappings)
Anja Siebert, 2023-2025 (Mappings)

