# Copyright René Drees
# Jegliche Vervielfältigung meines geistigen Eigentums wird zur Anzeige gebracht.
# Aus DSGVO-Gründen wurden alle Daten anonymisiert.

import os

ANZAHL_SCHUELER = 10
BESTANDEN_AB = 50.0
punkte_liste = [[] for _ in range(ANZAHL_SCHUELER)]


def bildschirm_leeren():
    """Leert die Konsole unter Windows, Linux und macOS."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Wartet auf Enter, bevor das Hauptmenü erneut angezeigt wird."""
    try:
        input("\nWeiter mit Enter...")
    except KeyboardInterrupt:
        print("\nEingabe durch Benutzer abgebrochen.")


def note_ermitteln(punkte):
    """Ermittelt aus einer Punktezahl zwischen 0 und 100 die Note 1 bis 6."""
    if punkte < 0 or punkte > 100:
        raise ValueError("Die Punkte müssen zwischen 0 und 100 liegen.")
    if punkte < 35:
        return 6
    elif punkte < 50:
        return 5
    elif punkte < 60:
        return 4
    elif punkte < 75:
        return 3
    elif punkte < 85:
        return 2
    else:
        return 1


def schueler_id_einlesen(text="Schüler-ID (1-10): "):
    """Liest eine gültige Schüler-ID ein. 'x' bricht die Eingabe ab."""
    while True:
        try:
            eingabe = input(text).strip().lower()
            if eingabe == "x":
                return None

            schueler_id = int(eingabe)
            if schueler_id < 1 or schueler_id > ANZAHL_SCHUELER:
                raise ValueError
            return schueler_id
        except ValueError:
            print(f"Bitte eine ganze Zahl zwischen 1 und {ANZAHL_SCHUELER} eingeben.")
        except KeyboardInterrupt:
            print("\nEingabe durch Benutzer abgebrochen.")
            return None


def punkte_einlesen(text="Punkte (0-100): "):
    """Liest eine gültige Punktezahl ein. 'x' bricht die Eingabe ab."""
    while True:
        try:
            eingabe = input(text).strip().lower()
            if eingabe == "x":
                return None

            punkte = float(eingabe.replace(",", "."))
            if punkte < 0 or punkte > 100:
                raise ValueError
            return punkte
        except ValueError:
            print("Bitte eine Zahl zwischen 0 und 100 eingeben.")
        except KeyboardInterrupt:
            print("\nEingabe durch Benutzer abgebrochen.")
            return None


def alle_punkte():
    """Gibt alle gespeicherten Einzelpunkte als flache Liste zurück."""
    return [punkte for schueler in punkte_liste for punkte in schueler]


def schueler_durchschnitt(index):
    """Berechnet den Durchschnitt eines Schülers."""
    try:
        return sum(punkte_liste[index]) / len(punkte_liste[index])
    except ZeroDivisionError:
        return None


def punkte_eingeben():
    print("\n--- Punkte eingeben ---")
    print("Mit 'x' kann die Eingabe abgebrochen werden.\n")

    while True:
        try:
            eingabe = input("Für wie viele Schüler sollen Punkte eingegeben werden? (1-10): ").strip().lower()
            if eingabe == "x":
                return
            anzahl = int(eingabe)
            if anzahl < 1 or anzahl > ANZAHL_SCHUELER:
                raise ValueError
            break
        except ValueError:
            print(f"Bitte eine ganze Zahl zwischen 1 und {ANZAHL_SCHUELER} eingeben.")
        except KeyboardInterrupt:
            print("\nVorgang durch Benutzer abgebrochen.")
            return

    for nummer in range(1, anzahl + 1):
        print(f"\nEingabe {nummer} von {anzahl}")
        schueler_id = schueler_id_einlesen()
        if schueler_id is None:
            print("Punkteingabe beendet.")
            break

        punkte = punkte_einlesen()
        if punkte is None:
            print("Punkteingabe beendet.")
            break

        punkte_liste[schueler_id - 1].append(punkte)
        print(f"{punkte:.1f} Punkte wurden für Schüler {schueler_id} gespeichert.")


def punkte_anzeigen():
    print("\n--- Alle Punkte anzeigen ---")
    vorhandene_schueler = 0

    for index, punkte in enumerate(punkte_liste, start=1):
        if punkte:
            vorhandene_schueler += 1
            durchschnitt = sum(punkte) / len(punkte)
            formatierte_punkte = ", ".join(f"{wert:.1f}" for wert in punkte)
            print(f"Schüler {index}: [{formatierte_punkte}] | Durchschnitt: {durchschnitt:.2f}")
        else:
            print(f"Schüler {index}: keine Punkte vorhanden")

    print(f"\nSchüler mit Einträgen: {vorhandene_schueler} von {ANZAHL_SCHUELER}")
    print(f"Gespeicherte Einzelwerte: {len(alle_punkte())}")


def durchschnitt_berechnen():
    print("\n--- Durchschnitt berechnen ---")
    print("[1] Durchschnitt eines Schülers")
    print("[2] Gesamtdurchschnitt aller Punkte")
    print("[x] Zum Hauptmenü")

    try:
        auswahl = input(">>> ").strip().lower()
    except KeyboardInterrupt:
        print("\nVorgang durch Benutzer abgebrochen.")
        return

    if auswahl == "1":
        schueler_id = schueler_id_einlesen()
        if schueler_id is None:
            return

        durchschnitt = schueler_durchschnitt(schueler_id - 1)
        if durchschnitt is None:
            print(f"Für Schüler {schueler_id} sind keine Punkte vorhanden.")
        else:
            print(f"Durchschnitt von Schüler {schueler_id}: {durchschnitt:.2f} Punkte")
            print(f"Entspricht Note: {note_ermitteln(durchschnitt)}")

    elif auswahl == "2":
        werte = alle_punkte()
        try:
            durchschnitt = sum(werte) / len(werte)
            print(f"Gesamtdurchschnitt: {durchschnitt:.2f} Punkte")
            print(f"Entspricht Note: {note_ermitteln(durchschnitt)}")
        except ZeroDivisionError:
            print("Keine Punkte vorhanden – Durchschnitt nicht berechenbar.")

    elif auswahl == "x":
        return
    else:
        print("Ungültige Eingabe.")


def einzel_note_ermitteln():
    print("\n--- Note aus Punktezahl ermitteln ---")
    print("Mit 'x' gelangst du zurück zum Hauptmenü.")

    punkte = punkte_einlesen()
    if punkte is None:
        return

    print(f"{punkte:.1f} Punkte entsprechen der Note {note_ermitteln(punkte)}.")


def min_max_auswertung():
    print("\n--- Min-/Max-Auswertung ---")
    werte = alle_punkte()

    if not werte:
        print("Es sind noch keine Punkte vorhanden.")
        return

    minimum = min(werte)
    maximum = max(werte)
    print(f"Niedrigste Punktezahl: {minimum:.1f}")
    print(f"Höchste Punktezahl:   {maximum:.1f}")

    print("\nSchüler mit der niedrigsten Punktezahl:")
    for index, punkte in enumerate(punkte_liste, start=1):
        if minimum in punkte:
            print(f"- Schüler {index}")

    print("Schüler mit der höchsten Punktezahl:")
    for index, punkte in enumerate(punkte_liste, start=1):
        if maximum in punkte:
            print(f"- Schüler {index}")


def notenspiegel_anzeigen():
    print("\n--- Notenspiegel ---")
    noten_zaehler = [0, 0, 0, 0, 0, 0]
    ausgewertete_schueler = 0

    for index in range(ANZAHL_SCHUELER):
        durchschnitt = schueler_durchschnitt(index)
        if durchschnitt is not None:
            note = note_ermitteln(durchschnitt)
            noten_zaehler[note - 1] += 1
            ausgewertete_schueler += 1

    if ausgewertete_schueler == 0:
        print("Keine Schüler mit Punkten vorhanden.")
        return

    for note, anzahl in enumerate(noten_zaehler, start=1):
        print(f"Note {note}: {anzahl} Schüler")

    print(f"\nAusgewertete Schüler: {ausgewertete_schueler}")
    print("Grundlage ist jeweils der Durchschnitt des Schülers.")


def punkte_loeschen():
    print("\n--- Punkte löschen ---")
    print("Mit 'x' kann der Vorgang abgebrochen werden.\n")

    schueler_id = schueler_id_einlesen()
    if schueler_id is None:
        return

    schueler_punkte = punkte_liste[schueler_id - 1]
    if not schueler_punkte:
        print(f"Für Schüler {schueler_id} sind keine Punkte hinterlegt.")
        return

    print(f"\nPunkte von Schüler {schueler_id}:")
    for index, punkte in enumerate(schueler_punkte):
        print(f"[{index}] {punkte:.1f} Punkte")

    while True:
        try:
            eingabe = input("Index des zu löschenden Eintrags: ").strip().lower()
            if eingabe == "x":
                return
            listen_index = int(eingabe)
            if listen_index < 0 or listen_index >= len(schueler_punkte):
                raise ValueError
            break
        except ValueError:
            print("Der angegebene Index ist nicht vorhanden.")
        except KeyboardInterrupt:
            print("\nVorgang durch Benutzer abgebrochen.")
            return

    zu_loeschender_wert = schueler_punkte[listen_index]
    bestaetigung = input(
        f"{zu_loeschender_wert:.1f} Punkte wirklich dauerhaft löschen? (j/n): "
    ).strip().lower()

    if bestaetigung == "j":
        geloeschter_wert = schueler_punkte.pop(listen_index)
        print(f"{geloeschter_wert:.1f} Punkte wurden gelöscht.")
    elif bestaetigung == "n":
        print("Löschvorgang abgebrochen.")
    else:
        print("Ungültige Eingabe. Es wurde nichts gelöscht.")


def bestehensquote_berechnen():
    print("\n--- Bestehensquote ---")
    ausgewertete_schueler = 0
    bestandene_schueler = 0

    for index in range(ANZAHL_SCHUELER):
        durchschnitt = schueler_durchschnitt(index)
        if durchschnitt is not None:
            ausgewertete_schueler += 1
            if durchschnitt >= BESTANDEN_AB:
                bestandene_schueler += 1

    try:
        quote = bestandene_schueler / ausgewertete_schueler * 100
        print(
            f"Bestehensquote: {quote:.1f}% "
            f"({bestandene_schueler} von {ausgewertete_schueler} Schülern)"
        )
        print(f"Bestanden ist ab {BESTANDEN_AB:.0f} Punkten im Durchschnitt.")
    except ZeroDivisionError:
        print("Keine Schüler mit Punkten vorhanden – Quote nicht berechenbar.")


def hauptmenue_anzeigen():
    print("\n--- Notenverwaltung ---\n")
    print("[1] Punkte eingeben")
    print("[2] Alle Punkte anzeigen")
    print("[3] Durchschnitt berechnen")
    print("[4] Note aus Punktezahl ermitteln (Einzelabfrage)")
    print("[5] Min-/Max-Auswertung")
    print("[6] Notenspiegel")
    print("[7] Punkte löschen")
    print("[8] Bestehensquote")
    print("[9] Programm beenden")


def main():
    while True:
        bildschirm_leeren()
        hauptmenue_anzeigen()

        try:
            auswahl = input("\n>>> Ihre Eingabe: ").strip()
        except KeyboardInterrupt:
            print("\nProgramm durch Benutzer beendet.")
            break

        bildschirm_leeren()

        if auswahl == "1":
            punkte_eingeben()
        elif auswahl == "2":
            punkte_anzeigen()
        elif auswahl == "3":
            durchschnitt_berechnen()
        elif auswahl == "4":
            einzel_note_ermitteln()
        elif auswahl == "5":
            min_max_auswertung()
        elif auswahl == "6":
            notenspiegel_anzeigen()
        elif auswahl == "7":
            punkte_loeschen()
        elif auswahl == "8":
            bestehensquote_berechnen()
        elif auswahl == "9":
            print("\nProgramm beendet. Auf Wiedersehen!\n")
            break
        else:
            print("\nEingabe nicht verstanden.")

        pause()


if __name__ == "__main__":
    main()