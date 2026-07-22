#Anforderungen: Copyright René Drees
# jegliche vervielfälltigung meines Geistigeneigentums wird zur Anzeigen gebracht.
# Aus DSGVO alle Daten wurden Anonymisiert 
# Variablen & Datentypen,(int,float,str,bool)
# Listen (Speicherung der Punkte)
# for und while -Schleifen
# if / elif / else / Fallunterscheidung
# try/ except / (Error Handling)
# VallueError, KeyboardError, ZeroDivisionsError
# Lehrer erfasst Punkte von Schülern um diese zuverwalten.
# Lehrer insert,delete,auswerten & Statistiken wieder geben.
# Menü l
#



title = str;
title('Notenverwaltung')
#Was muss ich deklarieren: import || Feste werte Schüler id &  Name sowie die entsprechenden Listen []
namen_schueler = (0 = Leon[], 1 = Mia, 2 = Finn, 3 = Emma, 4 = Noah, 5 = Lena, 6 = Elias, 7 = Ida, 8 = Ben, 9 = Paula)
name_schueler = str
schueler_id = int



#Menü
'''Notenverwaltung'''
1 - ('Punkte eingeben')
#       'Exit = Menü'
2 - ('Alle Punkte anzeigen')
#        'Exit = Menü'
3 - ('Durchsnitt berechnen')
#        'Exit = Menü'
4 - ('Note aus Punktezahl ermitteln (Einzelabfrage)')
#         'Exit = Menü'
5 - ('Programm beenden')
#      'Exit = Menü'
6 - ('Min Max Auswertung')
#      'Exit = Menü'
7 - ('Notenspiegel')
#      'Exit = Menü'
8 - ('Punkte löschen')
#      'Exit = Menü'

#Nummer 1:
schueler_id = int(input('Bitte geben Sie die Schüler id ein 1 -10'))
          if 0 < or > 100: count(x)
                      else  print('keine Zahl oder außerhalb von 0 -100')
punkte_zahl = float(input('Wie viele Punkte möchten Sie eingeben?'))
          if 0 < or > 100:
            else  print('keine Zahl oder außerhalb von 0 -100')
            loop 
    schüler1 eintragen in Liste / index
    schüler2
    schüler3
    schüler4   -> 10 schleife for schleife
# Error Handling , valaue keyboard  print('Bitte nur Dezimalzahlen 1-100 im Fomrat 10.1 Eingeben  )
# Bei überschreitung von gesamt Punkten von 100 print('ERROR: Wert wird nicht übernommern, er liegt nicht im Wertebereich von 0 - 100')
# print ('Back to Menü')


# Nummer 2:
# Alle Schüler mit Ihren Punkten anzeigen lassen 

#Eingegebene Punkte für Sven:[45.5, 78.0, 92.5, 33.0 ] 
  



# print ('Back to Menü')
# Nummer 3:
#mittelwet errechnen summer aller listen index / (listen addition)
#noten_durchschnitt = float(input('Der arithmetische Mittelwert: ', mittelwert),2) 
# print ('"Keine Punkte vorhanden – Durchschnitt nicht berechenbar."')


# print ('Back to Menü')

# Nummer 4:
try:
    punkte_zahl_note = float(input('Bitte geben Sie eine Zahl zwischen 0 -100 ein.:'))
        if 0 < or > 100:
        else  print('keine Zahl oder außerhalb von 0 -100')
    
except ValueError:
        print("Bitte eine Ganzzahl eingeben!")
except KeyboardInterrupt:
        print("Abbruch durch User")

else:
    if punkte_zahl_note < 0:
        print("Wert zu klein!")
    elif punkte_zahl_note < 35:
        print("Note 6")
    elif punkte_zahl_note < 50:
        print("Note 5")
    elif punkte_zahl_note < 60:
        print("Note 4")
    elif punkte_zahl_note < 75:
        print("Note 3")
    elif punkte_zahl_note < 85:
        print("Note 2")
    elif punkte_zahl_note <= 100:
        print("Note 1")
    else:
        print("Wert zu groß!")

                          
# print ('Back to Menü')

# Nummer 5:
#Press E for Programm-'Exit' 
# except ValueError:
#        print('Bitte "e" DRÜCKEN! e nicht a b oder c einfach "e"')
#except KeyboardInterrupt:
#        print("Abbruch durch User")
# print ("Programm beendet. Auf Wiedersehen!")
#    break
# print ('Back to Menü')


# Nummer 6:
# Anzeige der Min & Max Punkte ggf. mitnamen an.
# Liste leer von schüler id = print('Für diesen Schüler sind noch keine Punkte hinterlegt')
#except KeyboardInterrupt:
#        print("Abbruch durch User")
# print ('Back to Menü')



# Nummer 7: //Liste noten_zaehler = [0,0,0,0,0,0] für die Noten 1–6
# print('Notenspiegel')
# Note 1: 3 Schüler
# Note 2: ..
# Note 6: ....
#except KeyboardInterrupt:
#        print("Abbruch durch User")
# print ('Back to Menü')

# Nummer 8:
Schüler_id = int(input('Bitte geben Sie die Schüler id ein 1 -10'))
punkte_zahl = float(input('Wie viele Punkte möchten Sie eingeben?'))
# Punkte löschen:
# input Schüler_id 
# input Schülername:
# Ausgabe werte 
# 0: 45 Punkte
# 1: 10 Punkte ....
# print ()
 # Print('Daten wirklich dauerhaft löschen',  ) 
 # // j / n  abfrage  j delete durchführen : my_list.remove(120)
#fehleingabe Errorhandling and Keyboard ...  nicht j oder N 
# print ('Der gewünschte zulöschende Wert ist nicht vorhanden')
#except KeyboardInterrupt:
#        print("Abbruch durch User")
# print ('Back to Menü')








#Muster
import os

kontostand = 100

while True:
    # HAUPTMENÜ
    os.system("clear") # in Windows: "cls"
    print("Du bist im Hauptmenü")
    print("Du hast folgende Optionen:")
    print("[1] Kontostand einsehen")
    print("[2] Kontostand verändern")
    print("[x] Programm beenden")
    auswahl = input(">>> ")

    if auswahl == "1":
        while True:
            os.system("clear") # in Windows: "cls"
            print("Du möchtest deinen Kontostand einsehen")
            print("Du hast folgende Optionen:")
            print("[1] Kontostand einsehen")
            print("[x] Zum Hauptmenü")
            auswahl = input(">>> ")

            if auswahl == "1":
                print("Kontostand:", kontostand, "€")
                os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"
            elif auswahl == "x":
                print("Du kehrst jetzt zum Hauptmenü zurück.")
                os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"
                break
            else:
                print("Das verstehe ich nicht.")
                os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"

    elif auswahl == "2":
        while True:
            os.system("clear") # in Windows: "cls"
            print("Du möchtest deinen Kontostand verändern")
            print("Du hast folgende Optionen:")
            print("[1] Kontostand erhöhen")
            print("[2] Kontostand verringern")
            print("[x] Zum Hauptmenü")
            auswahl = input(">>> ")

            if auswahl == "1":
                print("Bitte Betrag als Ganzzahl eingeben")
                try:
                    betrag = int(input("Betrag: "))
                except ValueError:
                    print("Das ist keine valide Eingabe!")
                    os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"
                else:
                    kontostand = kontostand + betrag
                    print("Vielen Dank!")
                    os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"

            elif auswahl == "2":
                print("Bitte Betrag als Ganzzahl eingeben")
                try:
                    betrag = int(input("Betrag: "))
                except ValueError:
                    print("Das ist keine valide Eingabe!")
                    os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"
                else:
                    kontostand = kontostand - betrag
                    print("Vielen Dank!")
                    os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"

            elif auswahl == "x":
                print("Du kehrst jetzt zum Hauptmenü zurück.")
                os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"
                break
            else:
                print("Das verstehe ich nicht.")
                os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"

    elif auswahl == "x":
        print("Auf Wiedersehen!")
        break
    else:
        print("Das verstehe ich nicht.")
        os.system("read -p 'Weiter mit Enter...'") # in Windows: "pause"
