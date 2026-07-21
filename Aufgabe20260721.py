"""

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
"""



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
"""

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

"""

m_computer = "zahl"