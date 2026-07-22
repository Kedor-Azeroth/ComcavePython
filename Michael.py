import os

punkte = []

while True:
    # HAUPTMENÜ
    os.system("cls")  # unter Linux: os.system("clear")
    print("Notenverwaltung")
    print("Du hast folgende Optionen:")
    print("[1] Punktevergabe")
    print("[2] Punkte anzeigen")
    print("[3] Durchschnitt berechnen")
    print("[4] Punkte zu Noten")
    print("[x] Programm beenden")
    auswahl = input(">>> ")

    if auswahl == "1":
        i = 1
        while True:
            os.system("cls")
            print("Punktevergabe")
            print("Wie viele Punkte möchten Sie eingeben?")
            print("[x] Zum Hauptmenü")

            eingabe = input("Punkte " + str(i) + ": ")

            if eingabe == "x":
                print("Du kehrst jetzt zum Hauptmenü zurück.")
                input("Weiter mit Enter...")
                break

            try:
                wert = int(eingabe)

                if wert < 0 or wert > 100:
                    print("Ungültiger Wert - nur 0 bis 100 Punkte erlaubt.")
                    input("Weiter mit Enter...")
                    continue

                punkte.append(wert)
                i = i + 1

            except ValueError:
                print("Das ist keine gültige Zahl - bitte erneut eingeben.")
                input("Weiter mit Enter...")

        print(punkte)
        input("Weiter mit Enter...")

    elif auswahl == "x":
        print("Programm beendet. Auf Wiedersehen!")
        break
    else: auswahl != 'x'
    print ('flasche Eingabe')
    ''' 
    
 
''' 
 
'''
    elif auswahl == "2":
        while True:
            os.system("cls")
            print("Punkte anzeigen")
            print("Du hast folgende Optionen:")
            print("[x] Zum Hauptmenü")
            auswahl = input(">>> ")
 
            if auswahl == "x":
                print("Du kehrst jetzt zum Hauptmenü zurück.")
                os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"
                break
            else:
                print("Das verstehe ich nicht.")
                os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"
 
    elif auswahl == "3":
        while True:
            os.system("cls") # in Windows: "cls"
            print("Durschnitt berechnen")
            print("Du hast folgende Optionen:")
            print("[x] Zum Hauptmenü")
            auswahl = input(">>> ")
 
            if auswahl == "x":
                print("Du kehrst jetzt zum Hauptmenü zurück.")
                os.system("pause 'Weiter mit Enter...'")
                break
            else:
                print("Das verstehe ich nicht.")
                os.system("pause 'Weiter mit Enter...'")
 
    elif auswahl == "4":
            while True:
                os.system("cls") # in Windows: "cls"
                print("Durschnitt berechnen")
                print("Du hast folgende Optionen:")
                print("[x] Zum Hauptmenü")
                auswahl = input(">>> ")
 
                if auswahl == "x":
                    print("Du kehrst jetzt zum Hauptmenü zurück.")
                    os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"
                    break
                else:
                    print("Das verstehe ich nicht.")
                    os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"
 
 
    elif auswahl == "x":
        print("Beendet!")
        break
    else:
        print("Bissu Banane?.")
        os.system("pause 'Weiter mit Enter...'")
'''
 