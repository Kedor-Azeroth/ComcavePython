
# Notenverwaltung für Lehrer

punkte_liste = []  # Liste zur Speicherung aller Punktzahlen


def punkte_eingeben():
    while True:
        try:
            anzahl = int(input("Wie viele Punkte möchten Sie eingeben? "))
            if anzahl <= 0:
                print("Fehler: Bitte eine positive ganze Zahl eingeben.")
                continue
            break
        except ValueError:
            print("Fehler: Bitte eine ganze Zahl eingeben.")

    for i in range(anzahl):
        while True:
            try:
                wert = float(input(f"Punktzahl für Schüler {i + 1}: "))
                if 0 <= wert <= 100:
                    punkte_liste.append(wert)
                    break
                else:
                    print("Warnung: Wert muss zwischen 0 und 100 liegen. Wert wird nicht übernommen.")
            except ValueError:
                print("Fehler: Bitte eine Zahl eingeben.")


def alle_punkte_anzeigen():
    if not punkte_liste:
        print("Bisher wurden keine Punkte eingetragen.")
    else:
        print(f"Aktuelle Punkte: {punkte_liste}")
        print(f"Anzahl der Schüler: {len(punkte_liste)}")


def durchschnitt_berechnen():
    if not punkte_liste:
        print("Keine Punkte vorhanden – Durchschnitt nicht berechenbar.")
    else:
        durchschnitt = sum(punkte_liste) / len(punkte_liste)
        print(f"Durchschnitt: {durchschnitt:.2f} Punkte")


def note_aus_punktzahl(punkte):
    if 92 <= punkte <= 100:
        return 1
    elif 81 <= punkte < 92:
        return 2
    elif 67 <= punkte < 81:
        return 3
    elif 50 <= punkte < 67:
        return 4
    elif 30 <= punkte < 50:
        return 5
    elif 0 <= punkte < 30:
        return 6
    else:
        return None


def note_einzelabfrage():
    while True:
        try:
            wert = float(input("Bitte eine Punktzahl eingeben (0–100): "))
            if 0 <= wert <= 100:
                note = note_aus_punktzahl(wert)
                print(f"Punktzahl: {wert} → Note: {note}")
                break
            else:
                print("Fehler: Punktzahl muss zwischen 0 und 100 liegen.")
        except ValueError:
            print("Fehler: Bitte eine Zahl eingeben.")


def max_min_punkte():
    if not punkte_liste:
        print("Keine Punkte vorhanden – Maximum/Minimum nicht berechenbar.")
    else:
        print(f"Höchste Punktzahl: {max(punkte_liste)}")
        print(f"Niedrigste Punktzahl: {min(punkte_liste)}")


def notenspiegel():
    if not punkte_liste:
        print("Keine Punkte vorhanden – Notenspiegel nicht berechenbar.")
        return

    noten_zaehler = [0, 0, 0, 0, 0, 0]

    for p in punkte_liste:
        note = note_aus_punktzahl(p)
        if note is not None:
            noten_zaehler[note - 1] += 1

    print("Notenspiegel:")
    for note, anzahl in enumerate(noten_zaehler, start=1):
        print(f"Note {note}: {anzahl} Schüler")


def punkte_loeschen():
    if not punkte_liste:
        print("Keine Punkte vorhanden – nichts zu löschen.")
        return

    print("Aktuelle Punkte mit Indizes:")
    for index, wert in enumerate(punkte_liste):
        print(f"{index}: {wert}")

    try:
        index = int(input("Index des zu löschenden Punktes eingeben: "))
        if 0 <= index < len(punkte_liste):
            bestaetigung = input("Wirklich löschen? (j/n): ").lower()
            if bestaetigung == "j":
                geloeschter_wert = punkte_liste.pop(index)
                print(f"Punkt {geloeschter_wert} an Index {index} wurde gelöscht.")
            else:
                print("Löschvorgang abgebrochen.")
        else:
            print("Fehler: Index existiert nicht.")
    except ValueError:
        print("Fehler: Bitte eine ganze Zahl für den Index eingeben.")


def bestehensquote():
    if not punkte_liste:
        print("Keine Punkte vorhanden – Bestehensquote nicht berechenbar.")
        return

    gesamt = len(punkte_liste)
    bestanden = sum(1 for punkt in punkte_liste if punkt >= 50)
    quote = (bestanden / gesamt) * 100

    print(f"Bestehensquote: {quote:.1f}% ({bestanden} von {gesamt} Schülern)")


def menue():
    while True:
        print("\n--- Notenverwaltung ---")
        print("1 – Punkte eingeben")
        print("2 – Alle Punkte anzeigen")
        print("3 – Durchschnitt berechnen")
        print("4 – Note aus Punktzahl ermitteln (Einzelabfrage)")
        print("5 – Programm beenden")
        print("6 – Höchste & niedrigste Punktzahl")
        print("7 – Notenspiegel")
        print("8 – Punkte löschen")
        print("9 – Bestehensquote")

        auswahl = input("Bitte wählen Sie eine Option (1–9): ")

        if auswahl == "1":
            punkte_eingeben()
        elif auswahl == "2":
            alle_punkte_anzeigen()
        elif auswahl == "3":
            durchschnitt_berechnen()
        elif auswahl == "4":
            note_einzelabfrage()
        elif auswahl == "5":
            print("Programm beendet. Auf Wiedersehen!")
            break
        elif auswahl == "6":
            max_min_punkte()
        elif auswahl == "7":
            notenspiegel()
        elif auswahl == "8":
            punkte_loeschen()
        elif auswahl == "9":
            bestehensquote()
        else:
            print("Ungültige Auswahl. Bitte 1–9 eingeben.")


if __name__ == "__main__":
    menue()

