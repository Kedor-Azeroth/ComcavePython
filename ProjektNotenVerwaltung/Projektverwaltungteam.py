punkte = []

while True:
    print()
    print("--- Notenverwaltung ---")
    print("1 - Punkte eingeben")
    print("2 - Alle Punkte anzeigen")
    print("3 - Durchschnitt berechnen")
    print("4 - Note aus Punktzahl ermitteln")
    print("5 - Programm beenden")
    print("6 - Höchste und niedrigste Punktzahl")
    print("7 - Notenspiegel")
    print("8 - Punkte löschen")
    print("9 - Bestehensquote")

    auswahl = input("Ihre Wahl: ")

    # ------------------ Menüpunkt 1

    if auswahl == "1":
        print()
        print("--- Punkte eingeben ---")
        print("Hinweis: Sie befinden sich jetzt in der Eingabe.")
        print("Zum Menü kommen Sie mit x zurück.")

        anzahl = 0
        abbruch = False
        while True:
            eingabe = input("Für wie viele Schüler möchten Sie Punkte eingeben? "
                            "(x = Zurück zum Menü)")
            if eingabe.lower() == "x":
                abbruch = True
                break
            try:
                anzahl = int(eingabe)
            except ValueError:
                print("Das ist keine gültige Zahl. Bitte eine ganze Zahl eingeben.")
            else:
                if anzahl < 1:
                    print("Bitte eine Zahl größer 0 eingeben.")
                elif anzahl > 100:
                    print("Das sind zu viele Punkte, bitte höchstens 100 Schüler eingeben.")
                else:
                    break

        if not abbruch:
            for i in range(anzahl):
                while True:
                    eingabe = input("Punkte für Schüler " + str(i + 1) +
                                    " von " + str(anzahl) +
                                    " (0-100, x = abbrechen): ")
                    if eingabe.lower() == "x":
                        abbruch = True
                        break

                    try:
                        wert = float(eingabe.replace(",", "."))
                    except ValueError:
                        print("Das ist keine gültige Zahl, bitte erneut eingeben.")
                        continue

                    if wert < 0 or wert > 100:
                        print("Warnung: Der Wert muss zwischen 0 und 100 Punkten liegen.",
                              "Der Wert  wird nicht übernommen.")
                        continue

                    punkte.append(wert)
                    break

            if abbruch:
                print("Eingabe abgebrochen.")
                break

        print("Es sind jetzt", len(punkte), "Werte gespeichert.")

    # ------------------ Menüpunkt 2
    
    elif auswahl == "2":
        if len(punkte) == 0:
            print("Keine Punkte vorhanden.")
        else:
            print("Aktuelle Punkte: ", punkte)
            print("Anzahl der Schüler: ", len(punkte))

    # ------------------ Menüpunkt 3
    
    elif auswahl == "3":
            if len(punkte) == 0:
                print("Keine Punkte vorhanden - Durchschnitt nicht berechenbar.")
            else:
                summe = 0
                for p in punkte:
                    summe = summe + p
                durchschnitt = summe / len(punkte)
                print("Durchschnitt: ", format(durchschnitt, ".2f"), "Punkte")

    # ------------------ Menüpunkt 4
    
    elif auswahl == "4":
        eingabe = input("Punktzahl: ")
        try:
            wert = float(eingabe.replace(",", "."))
        except ValueError:
            print("Das ist keine gültige Zahl.")
        else:
            if wert < 0 or wert > 100:
                print("Der Wert muss zwischen 0 und 100 Punkten liegen.")
            elif wert >= 92:
                print(wert, "Punkte ergeben Note 1")
            elif wert >= 81:
                print(wert, "Punkte ergeben Note 2")
            elif wert >= 67:
                print(wert, "Punkte ergeben Note 3")
            elif wert >= 50:
                print(wert, "Punkte ergeben Note 4")
            elif wert >= 30:
                print(wert, "Punkte ergeben Note 5")
            else:
                print(wert, "Punkte ergeben Note 6")
  
    # ------------------ Menüpunkt 5
    
    elif auswahl == "5":
        print("Programm beendet. Auf Wiedersehen.")
        break
  
    # ------------------ Menüpunkt 6
         
    elif auswahl == "6":
        if len(punkte) == 0:
            print("Bisher wurden keine Punkte eingetragen.")
        else:
            hoechste = punkte[0]
            niedrigste = punkte[0]
            for p in punkte:
                if p > hoechste:
                    hoechste = p
                if p < niedrigste:
                    niedrigste = p
            print("Höchste Punktzahl: ", hoechste)
            print("Niedrigste Punktzahl: ", niedrigste)

    # ------------------ Menüpunkt 7
    
    elif auswahl == "7":
        if len(punkte) == 0:
                    print("Bisher wurden keine Punkte eingetragen.")
        else:
            noten_zaehler = [0, 0, 0, 0, 0, 0]
            for p in punkte:
                if p >= 92:
                    noten_zaehler[0] = noten_zaehler[0] + 1
                elif p >= 81:
                    noten_zaehler[1] = noten_zaehler[1] + 1
                elif p >= 67:
                    noten_zaehler[2] = noten_zaehler[2] + 1
                elif p >= 50:
                    noten_zaehler[3] = noten_zaehler[3] + 1
                elif p >= 30:
                    noten_zaehler[4] = noten_zaehler[4] + 1
                else:
                    noten_zaehler[5] = noten_zaehler[5] + 1

            print("Notenspiegel: ")
            for i in range(6):
                print("Note", str(i + 1) + ":", noten_zaehler[i], "Schüler")    


    # ------------------ Menüpunkt 8
    
    elif auswahl == "8":
        if len(punkte) == 0:
            print("Bisher wurden keine Punkte eingetragen.")
        else:
            for i, p in enumerate(punkte):
                print(str(i) + ":", p)

            eingabe = input("Welchen Index möchten Sie löschen? ")
            try:
                index = int(eingabe)
            except ValueError:
                print("Das ist keine gültige Zahl.")
            else:
                if index < 0 or index >= len(punkte):
                    print("Diesen Index gibt es nicht. Erlaubt ist 0 bis",
                          len(punkte) - 1)
                else:
                    sicher = input("Wirklich löschen? (j/n) ")
                    if sicher.lower() == "j":
                        geloescht = punkte[index]
                        del punkte[index]
                        print("Der Wert ", geloescht, "wurde gelöscht.")
                    else:
                        print("Abgebrochen. Es wurde nichts gelöscht.")    
    
    # ------------------ Menüpunkt 9

    elif auswahl == "9":
        if len(punkte) == 0:
            print("Bisher wurden keine Punkte eingetragen.")
        else:
            bestanden = 0
            for p in punkte:
                if p >= 50:
                    bestanden = bestanden + 1
            quote = bestanden / len(punkte) * 100
            print("Bestehensquote: " + format(quote, ".1f") + "%", 
                  "(" + str(bestanden), "von", str(len(punkte)) + " Schülern)")        

    # ------------------ Falscheingabe

    else:
        print("Falsche Eingabe, bitte eine Zahl von 1 - 9 eingeben.")
        