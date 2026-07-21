'W3Schools.com'
# Case Sensitivity¡!!!!!!!!!
# Duck-Typing erkennt selbst Datentypen und wandelt sie automatisch um, wenn nötig.
print(9+2)
#print(type("\"Hallo\""))
#print("Drucken"," Hier") #   >Ausgabe Konsole  Drucken hier
#Print("Drucken") #> Drucken
#Print()          #> es wird eine Zeile eingeschoben ohne ausgabe  
#Print("Hier")    #> Hier untereinadner        "" >String  ""< int ohne
#name = " Rene "  # Variable name mit dem Wert Rene
#name = input("Wie heißt du? ") #Zahl = 4        # Variable Zahl mit dem Wert 4
#Zahl = 4        # Variable Zahl mit dem Wert 4
#print(name + " will Python lernen " + str(Zahl) + " in Wochen")  # Nun mit variablen  str als int in String umwandeln
#print(name + " will Python lernen " + str(Zahl) + " in Wochen")  # Nun mit variablen  str als int in String umwandeln
#print("ich will Python lernen in",4,"Wochen")
#item = "Bike" """Bike steht hier als Varible für Item
#                 Variable Box: Item Variablenwert "Bike" mit Informationen 
#                 Variablen speichern Informationen die sich ändern können (Fortschritt eines Spiels)"""
#print("Ich habe ein", item)  ###> Ich habe ein Bike
#print(9+2)  ist mit /*  -  +  möglich
#Modulo %  Rest einer Division Beispiel 7/3 = 2 Rest 1
#print(9%2) #> 1  Rest der Division von 9 durch 2 ist Ergebniss 1 
#2 ** 3 = 2*2*2 = 8 Potenzierung
#del  y löscht die Variable y und gibt den Speicherplatz frei
#type() gibt den Datentyp der Variable aus
# x = True  # Boolean True oder False
""" Comment 1 Zeile oder mehrzeilig mit drei Anführungszeichen
Dieses beeinflusst auch nicht den Code, es ist nur eine Anmerkung für den Programmierer, damit er sich besser zurechtfindet. 
Es könnte auch eine To-Do Liste
"""
#Variablen definieren 
#X=3
#Y=4
#print(X+Y) #> 7
#print(type("Hallo")) 
#print(type(""Hallo"")) Ausgabe >"Hallo"
#print(type("\"Hallo\""))
#print("i am "+"25"+" years old") #> i am 25 years old
#print("5"+"5") #> 55
#print("This is a"
#"very long"
# "string") #> This is a very long string
#print("""This is a
# very long 
# string""") 
#alternativ auch ohne Print() möglich
#x = 5
#y = 10
#z = x + y
#print(z)
#a1 = 5 #Varibale dürfen nicht mit Zahlen beginnen, daher ist a1 korrekt
#1 = 5 #Fehlerhafte Variable, Variablen dürfen nicht mit Zahlen beginnen'''
#fruits = ['apple', 'banana', 'cherry', 'date', 'cherry']
#x = fruits.count("cherry")
#print(x)
#'Apple' .count ('p')  #Zählt die Anzahl der Buchstaben p in dem Wort Apple
# string * 3 bedeutet, dass der String 3 mal wiederholt wird
# print("Hello" * 3)
# a = int('3') *3 string wird in int umgewandelt und mit 3 multipliziert
# dauer_stunde = round ((geh_zeit + jogging_zeit + schwimm_zeit )/60, 2)             # gerundet 
#round(wandflaeche_gesamt * 0.15, 1)  # 0.15 Liter pro m²
#print(round('Temperatur in Kelvin ist:', kelvin,2))
#print(round(kelvin, 3), 'K')
#\n zeitlen umbruch ('\n Das Program')
'''Error Handling in Python   #Nach if, elif, else, try und except steht immer ein Doppelpunkt:
try:                        # bei fehler try block sonst else Block es kommt aufjeden Finallyblock
    # Code, der einen Fehler verursachen kann
    zahl = int(input("Zahl eingeben: "))

except ValueError:
    # Fehler: Es wurde keine ganze Zahl eingegeben
    print("Es wurde keine gültige Zahl eingegeben.")

except KeyboardInterrupt:
    # Fehler: Benutzer hat das Programm mit Strg + C beendet
    print()
    print("Das Programm wurde vom Benutzer abgebrochen.")
    
    try:weitere Handlings möglich
    except
    else
    finally

else:
    # Wird nur ausgeführt, wenn kein Fehler aufgetreten ist
    print("Vielen Dank.")

finally:                                 #wird immer ausgeführt
    # Wird immer ausgeführt
    print("Auf Wiedersehen.")'''
#try: → Hier steht der Code, der einen Fehler verursachen könnte.
#except: → Fängt einen bestimmten Fehler ab und behandelt ihn.
#else: → Wird nur ausgeführt, wenn im try-Block kein Fehler aufgetreten ist.
#finally: → Wird immer ausgeführt, unabhängig davon, ob ein Fehler aufgetreten ist oder nicht
#try
# │
# ├── Fehler? ── Ja ──► except
# │
# └── Nein ───────────► else
#                      │
#                      ▼
#                   finally
#try = ausprobieren → except = Fehler behandeln → else = kein Fehler → finally = immer ausführen.
#Beispiel zum Anfangen
'''Getraenkemarkt'''
try:
#Eingabe
    bierkisten = int(input('Anzahlkisten:'))
    wasserkisten = int(input('Anzahl Wasser-Kisten:'))
    einzelflaschen = int(input('Anzahl einzelne Flaschen'))
except ValueError:
    print('nein')
except KeyboardInterrupt:
    print('Programm wurde beendet')    
else:
   print( 'Schön')

#Verarbeitung

#Ausgabe

#Beispiel zum Anfangen von Fehlern
'''Getraenkemarkt
try:
#Eingabe
    bierkisten = int(input('Anzahlkisten:'))
    wasserkisten = int(input('Anzahl Wasser-Kisten:'))
    einzelflaschen = int(input('Anzahl einzelne Flaschen'))
except ValueError:
    print('nein')
else:
   #wenn eine der 3 Variablen negativ ist Hinweise an Nutzer, ansonsten alles ganz normal 
   
   if bierkisten <= 0 or wasserkisten <= 0 or einzelflaschen  <= 0:
       print('positive Zahlen')
   else:
#Verarbeitung
    gesamt_flaschen = bierkisten *  + wasserkisten *  + einzelflaschen
    gesamt_pfand = gesamt_flaschen * 0.25

#Ausgabe
    print('Gesamtzahl Flaschen:', gesamt_flaschen)
    print('Gesamtpfand:' ,gesamt_pfand, 'Euro')'''
#Alternative
'''Getraenkemarkt
try:
#Eingabe Eingabe wird bei Falsch abgebrochen.
    bierkisten = int(input('Anzahlkisten:'))
    if bierkisten <= 0:
        raise ValueError
        
    wasserkisten = int(input('Anzahl Wasser-Kisten:'))
    if wasserkisten <= 0:
        raise ValueError
    einzelflaschen = int(input('Anzahl einzelne Flaschen'))
    if einzelflaschen <= 0:
        raise ValueError
except ValueError:
    print('nein')
except KeyboardInterrupt:
       print('')    
else:
   #Verarbeitung
    gesamt_flaschen = bierkisten *  + wasserkisten *  + einzelflaschen
    gesamt_pfand = gesamt_flaschen * 0.25

#Ausgabe
    print('Gesamtzahl Flaschen:', gesamt_flaschen)
    print('Gesamtpfand:' ,gesamt_pfand, 'Euro')'''


'''
If, elif, else   # Verzeigung von Bedingungen

[Start]
   |
   v
[ if Bedingung 1 ? ] --(Wahr)--> [Block 1 ausführen] --> [Ende]
   | (Falsch)
   v
[ elif Bedingung 2 ? ] --(Wahr)--> [Block 2 ausführen] --> [Ende]
   | (Falsch)
   v
[ ... ]
   | (Falsch)
   v
[ else ] --> [Standard-Block ausführen] --> [Ende]

Einfache IF Vergleiche

if 2 == 3:
    print("Die Zahlen sind gleich")

    '''