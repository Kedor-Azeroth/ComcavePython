# Copyright René Drees
# Jegliche Vervielfältigung meines geistigen Eigentums wird zur Anzeige gebracht.
# Aus DSGVO-Gründen wurden alle Daten anonymisiert.

# logischen Ablauf (Soll-Verhalten, Struktur, ggf. Pseudocode-Schnipsel
# Anforderungen: 
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
import os

punkte_liste = [[] for _ in range(10)]  # Index 0 = Schüler 1, ... Index 9 = Schüler 10

'''Notenverwaltung'''
while True:
    #Hauptmenü
    os.system('clear')             #os.system("cls")      # für Windows
    print()
    print('\n--- Notenverwaltung---')
    print()
    print('Du bist im Hauptmenü')
    print()
    print('Folgende Optionen stehen Ihnen zur verfügung:')
    print('[1] Punkte eingeben')
    print('[2] Alle Punkte anzeigen')
    print('[3] Durchschnitt berechnen')
    print('[4] Note aus Punktezahl ermitteln "Einzelabfrage"')
    print('[5] Min, Max Auswertung')
    print('[6] Notenspiegel')
    print('[7] Punkte löschen')
    print('[8] Bestehendesquote')
    print('[9] Programm beenden')
    auswahl = input('>>> Ihre Eingabe:  ')   #Eingabe erforderlich

    if auswahl == '1':
        while True:
            print()
            print('Du bist im Menü "Punkte eingeben"')
            print('[x] Zum Hauptmenü')
            eingabe = input('>>> Schüler-ID eingeben (1-10) oder x für Hauptmenü: ')

            if eingabe.lower() == 'x':
                break

            try:
                schueler_id = int(eingabe)
                if not (1 <= schueler_id <= 10):
                    print('Fehler: Schüler-ID muss zwischen 1 und 10 liegen.')
                    input('Weiter mit Enter...')
                    continue
            except ValueError:
                print('Fehler: Bitte eine ganze Zahl zwischen 1 und 10 eingeben.')

                input('Weiter mit Enter...')
                continue

            try:
                punkte_eingabe = float(input('Wie viele Punkte möchten Sie eingeben (0-100)? '))
                if not (0 <= punkte_eingabe <= 100):
                    print('ERROR: Wert wird nicht übernommen, er liegt nicht im Wertebereich von 0 - 100.')
                    input('Weiter mit Enter...')
                    continue
            except ValueError:
                print('Bitte nur Dezimalzahlen 1-100 im Format 10.1 eingeben.')
                input('Weiter mit Enter...')
                continue

            punkte_liste[schueler_id - 1].append(punkte_eingabe)
            print(f'{punkte_eingabe} Punkte wurden Schüler {schueler_id} zugeordnet.')
            input('Weiter mit Enter...')

    elif auswahl == '2':
        while True:
                    print()
                    print('"Du bist im Menü "Alle Punkte anzeigen"')
                    print('[x] Zum Hauptmenü')
                    print()
                    auswahl = input('>>> ' )

                    if auswahl == 'x':
                         print('Du kehrst zum Hauptmenü zurück.')

                    if os.name == 'nt':     # Windows 'nt' ist muss
                      os.system("pause")
                               
                    else:                     # Linux/macOS
                        input("Weiter mit Enter...")
        else:
                    break
                    print('Ungültige Eingabe')

                    

    elif auswahl == '3':
        while True:
                    print()
                    print('"Du bist im Menü "Durchschnitt berechen"')
                    print('[x] Zum Hauptmenü')
                    print()
                    auswahl = input('>>> ' )
                    
                    if auswahl == 'x':
                        print('Du kehrst zum Hauptmenü zurück.')
                    
                    if os.name == 'nt':     # Windows 'nt' ist muss
                       os.system("pause")
                                                   
                    else:                     # Linux/macOS
                        input("Weiter mit Enter...")
        else:
                    break
                    print('Ungültige Eingabe')
                    
    elif auswahl == '4':
        while True:
                    print()
                    print('"Du bist im Menü "Note aus Punktezahl ermitteln"')
                    print('[x] Zum Hauptmenü')
                    print()
                    auswahl = input('>>> ' )
                    
                    if auswahl == 'x':
                        print('Du kehrst zum Hauptmenü zurück.')
                    
                    if os.name == 'nt':     # Windows 'nt' ist muss
                       os.system("pause")
                                                   
                    else:                     # Linux/macOS
                        input("Weiter mit Enter...")
        else:
                    break
                    print('Ungültige Eingabe')                   
        
    elif auswahl == '5':
        while True:
                    print()
                    print('"Du bist im Menü "Min, Max Auswertung"')
                    print('[x] Zum Hauptmenü')
                    print()
                    auswahl = input('>>> ' )
                    
                    if auswahl == 'x':
                        print('Du kehrst zum Hauptmenü zurück.')
                    
                    if os.name == 'nt':     # Windows 'nt' ist muss
                       os.system("pause")
                                                   
                    else:                     # Linux/macOS
                        input("Weiter mit Enter...")
        else:
                    break
                    print('Ungültige Eingabe')                    

    elif auswahl == '6':
        while True:
                    print()
                    print('"Du bist im Menü "Notenspiegel"')
                    print('[x] Zum Hauptmenü')
                    print()
                    auswahl = input('>>> ' )
                    
                    if auswahl == 'x':
                        print('Du kehrst zum Hauptmenü zurück.')
                    
                    if os.name == 'nt':     # Windows 'nt' ist muss
                       os.system("pause")
                                                   
                    else:                     # Linux/macOS
                        input("Weiter mit Enter...")
        else:
                    break
                    print('Ungültige Eingabe') 

    elif auswahl == '7':
        while True:
                    print()
                    print('"Du bist im Menü "Punkte löschen"')
                    print('[x] Zum Hauptmenü')
                    print()
                    auswahl = input('>>> ' )
                    
                    if auswahl == 'x':
                        print('Du kehrst zum Hauptmenü zurück.')
                    
                    if os.name == 'nt':     # Windows 'nt' ist muss
                       os.system("pause")
                                                   
                    else:                     # Linux/macOS
                        input("Weiter mit Enter...")
        else:
                    break
                    print('Ungültige Eingabe')
                  
    elif auswahl == '8':
        while True:
                    print()
                    print('"Bestehendesquote"')
                    print('[x] Zum Hauptmenü')
                    print()
                    auswahl = input('>>> ' )
                    
                    if auswahl == 'x':
                        print('Du kehrst zum Hauptmenü zurück.')
                    
                    if os.name == 'nt':     # Windows 'nt' ist muss
                       os.system("pause")
                                                   
                    else:                     # Linux/macOS
                        input("Weiter mit Enter...")
        else:
                    break
                    print('Ungültige Eingabe')
                    
    elif auswahl == '9':
        print()
        print ("Programm beendet.Auf Wiedersehen!")
        print()
        break
    else:
         print()
         print('Eingabe nicht verstanden')
         print()
    if os.name == 'nt':     # Windows 'nt' ist muss
         os.system("pause")
    else:                     # Linux/macOS
        input("Weiter mit Enter...")




'''schueler_id = int(input('Bitte geben Sie die Schüler id ein 1 -10'))
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





#Was muss ich deklarieren:  Feste werte Schüler id &  Name sowie die entsprechenden Listen []
namen_schueler = (0 = Leon[], 1 = Mia, 2 = Finn, 3 = Emma, 4 = Noah, 5 = Lena, 6 = Elias, 7 = Ida, 8 = Ben, 9 = Paula)
name_schueler = str
schueler_id = int

punkte_liste = [[] for _ in range(10)]  # Index 0 = Schüler 1, ... Index 9 = Schüler 10
'''

'''
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

# Nummer 5:
# Anzeige der Min & Max Punkte ggf. mitnamen an.
# Liste leer von schüler id = print('Für diesen Schüler sind noch keine Punkte hinterlegt')
#except KeyboardInterrupt:
#        print("Abbruch durch User")

# Nummer 6: //Liste noten_zaehler = [0,0,0,0,0,0] für die Noten 1–6
# print('Notenspiegel')
# Note 1: 3 Schüler
# Note 2: ..
# Note 6: ....
#except KeyboardInterrupt:
#        print("Abbruch durch User")

# Nummer 7:
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

# Nummer 8:
# Bestehensquote ?  Schülerzählen wieviele schüler > 50 Punkte
# Gib aus: "Bestehensquote: 75.0% (6 von 8 Schülern)
'''