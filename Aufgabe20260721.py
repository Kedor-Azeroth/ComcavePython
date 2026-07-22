'''
Entwickle ein Programm zur Berechnung des Durchschnittwerts
Eingabe:
- Summe  (Zahl!)
- Anzahl (Ganzzahl!)
Beispiel -> summe = 3.7 anzahl = 4

try:
       summe = float(input('Geben Sie einen Zahl an:'))
       if summe <=0:
              raise ValueError
       anzahl = int(input('Geben Sie einen Ganzzahl an:'))
       if anzahl <=0:
              raise ValueError
except ValueError:
       print('Dieses ist keine gültiger Eingabewert!')   
except ZeroDivisionError:
       print('Die Division durch 0 ist nicht möglich!')           
except KeyboardInterrupt:
       print('Das Programm wurde durch Sie abgebrochen!')
else:       
       #Verarbeitung:
       durchschnitts_wert = summe / anzahl
       #Ausgabe
       #3.7 / 4
       print('Ihr Durchschnittswert lautet',durchschnitts_wert)

Arbeitet mit try-except-else!
BONUS) Was passiert wenn Anzahl = 0?
'''
"""

Übung 1:
Eine Schule möchte die Ermittlung der Noten ihrer Schüler 
digital durchführen.

Dabei soll der Lehrer (=Nutzer) eine Punktzahl eingeben 
und eine Note ausgegeben bekommen.

Die Note wird anhand folgender Formel berechnet:

weniger als 35 Punkte -> 6
mind. 35 Punkte -> 5
mind. 50 Punkte -> 4
mind. 60 Punkte -> 3
mind. 75 Punkte -> 2
mind. 85 Punkte -> 1

Anmerkung: Die Maximalpunktzahl beträgt 100 Punkte!
Anmerkung: Die Minimalpunktzahl beträgt 0 Punkte!
"""
'''
try:
       nutzer = int(input('Bitte Punkteanzahl eingeben:'))
       if nutzer < 0 or nutzer > 100:
               raise ValueError
except ValueError:
       print('Ihr Eingegebener Wert liegt ausserhalb des Notenschlüssels!')               
except KeyboardInterrupt:
       print('Das Programm wurde durch Sie abgebrochen!')
else:
#Verarbeitung
       if nutzer < 35:                  alternative if nutzer < 0 (print) elif nutzer < 35:
              note = 6
       elif nutzer < 50:
              note = 5
       elif nutzer < 60:
              note = 4
       elif nutzer < 75:
              note = 3
       elif nutzer < 85:
              note = 2                      elif nutzer <=100:print(1)
       else:                               #else(wet zu groß)

print('Die eingegebenen Punkte entsprechen einer:', note)              
'''
#Alternative
try:
    punktzahl = int(input("Punktzahl: "))
except ValueError:
    print("Bitte eine Ganzzahl eingeben!")
else:
    if punktzahl < 0:
        print("Wert zu klein!")
    elif punktzahl < 35:
        print("Note 6")
    elif punktzahl < 50:
        print("Note 5")
    elif punktzahl < 60:
        print("Note 4")
    elif punktzahl < 75:
        print("Note 3")
    elif punktzahl < 85:
        print("Note 2")
    elif punktzahl <= 100:
        print("Note 1")
    else:
        print("Wert zu groß!")

'''
Entwickle ein Kopf-oder-Zahl Spiel

Zuerst gibt der Nutzer "Kopf" oder "Zahl" ein.
Anschließend wird die Eingabe mit dem
Wert, welchen der Computer "sich denkt" verglichen

Sollte der Nutzer richtig geraten haben,
gebe eine positive Rückmeldung aus

Sollte der Nutzer falsch geraten haben,
gebe eine negative Rückmeldung aus

Wandle die Eingabe des Nutzers in Kleinbuchstaben
um. Das geht mit der str.lower() Methode.

Beispiel:
x = "ABC"
x = x.lower()
print(x) # "abc"

BONUS) Finde heraus, wie du den Zufall über

       den Wert des Computers entscheiden lässt

'''
try:
       import random
       user = (input('Bitte eingeben Kopf oder Zahl ein:'))
       user = user.lower()
       m_computer = ['zahl','kopf']
       if user not in m_computer:
              raise ValueError
except ValueError:
       print('Dieses ist keine gültiger Eingabewert!')   
except KeyboardInterrupt:
       print('Das Programm wurde durch Sie abgebrochen!')
#Verarbeitung
else:       
       computer = random.choice(m_computer)    #computer = random.choice('Kopf','Zahl')
       if user == computer:
              print('Gewonnen!')
       else:
              print('Das war leider nix vielleicht hast du bei nächstenmal mehr Glück.')

#Alternative
import random

m_computer = random.choice(["kopf", "zahl"])
m_user = input("Kopf oder Zahl? ")
m_user = m_user.lower()

try:
    if m_user != "kopf" and m_user != "zahl":
        raise ValueError
except ValueError:
    print("Das ist keine valide Eingabe!")
else:
    print("Der Computer hat gewählt:", m_computer)
    if m_user == m_computer:
        print("Sehr gut! Du hast gewonnen.")
    else:
        print("Schade! Du hast verloren.")



