'''Aufgabe Umrechnung Grad Celsius in 1) Grad Fahrenheit 2) Kelvin    '''
#Eingabe:


umrechnung = float(input('Bitte geben Sie einen Wert ein: '))
#umrechnung_kelvin = float(input('Bitte geben Sie einen Wert ein: '))

# Verarbeitung
fahrenheit = umrechnung * 9 / 5 + 32
kelvin = umrechnung + 273.15


# Ausgabe
print('Temperatur in Fahrenheit ist:', fahrenheit)
print('Temperatur in Kelvin ist:', kelvin)

'''Aufgabe Entwickle ein Programm, mit dem der Flächeninhalt eines Dreiecks berechnen lässt'''



#Eingabe
g = float (input('Dreieck Seitenlänge Grundseite:'))
h = float (input('Dreieck Seitenlänge Höhe:'))




#Verarbeitung
A= (g*h) /2

#Ausgabe
print('Der Flächeninhalt lautet:', A)



'''Aufgabe Dreieckflächeninhalt über 3 Seiten'''
a = float (input('Dreieck Seitenlänge A:'))
b = float (input('Dreieck Seitenlänge B:'))
c = float (input('Dreieck Seitenlänge C:'))


s = (a + b + c) /2 
A = (s * (s-a)*(s-b)*(s-c)) ** 0.5    # ** Quadratwurzel

print('Der Flächeninhalt lautet:', A, 'Kubikcm')


'''Aufgabe    Fitnesstracker             '''
geh_zeit = int(input('Gehzeit in Minuten: '))
jogging_zeit = int(input('Joggingzeit in Minuten: '))
schwimm_zeit = int(input('Schwimmzeit in Minuten: '))

kalorien_geh = geh_zeit * 5
kalorien_jog = jogging_zeit * 10
kalorien_schw = schwimm_zeit * 8
kalorien_gesamt = kalorien_geh + kalorien_jog + kalorien_schw

dauer_stunde = round ((geh_zeit + jogging_zeit + schwimm_zeit )/60, 2)             # gerundet

print('Ihre Kalorienwerte für Gehen: ', kalorien_geh)
print('Kalorienwerte für Joggen: ', kalorien_jog)
print('Kalorienwerte fürs Schwimmen: ' ,kalorien_schw) 
print('Gesamt Verbrauchte Kalorien: ',kalorien_gesamt)
print('Gesamttrainingsdauer in Stunden: ' ,dauer_stunde) 


'''Aufgabe Einkaufszettlel'''
'''Anzahl Äpfel (0,89 €/Stück)
- Anzahl Bananen (0,49 €/Stück)
- Anzahl Orangen (0,69 €/Stück)
- Berechne Gesamtpreis für jede Obstsorte
- Berechne Gesamtsumme
- Berechne Anzahl der verschiedenen Obstsorten (immer 3, da 3 Sorten)

- Ausgabe:

- Gesamtsumme in Euro
- Durchschnittspreis pro Frucht
'''
#Eingabe
apfel = int(input('Anzahl Äpfel: '))
bananen = int(input('Anzahl Bananen: '))
orangen = int(input('Anzahl Orangen: '))

#Berechnung
apfel_preis = apfel * 0.89
bananen_preis = bananen * 0.49
orangen_preis = orangen * 0.69

gesamt_summe = apfel_preis + bananen_preis + orangen_preis

# Anzahl der Obstsorten
obstsorten = ['Apfel', 'Banane', 'Orange']
anzahl_sorten = len(obstsorten)

durchschnitt_frucht = gesamt_summe / anzahl_sorten 

print('Anzahl der Obstsorten: ', anzahl_sorten)
print('Gesamtsumme: ', gesamt_summe, ' Euro.' )
print('Durchschnitts Preis pro Frucht: ', durchschnitt_frucht, ' Euro.')





'''Aufgabe Reisebüro Eingabe:
• Anzahl Erwachsene (320 €/Person)
• Anzahl Kinder (180 €/Person)
• Anzahl Babys (0 €/Person, aber 25 € Gebühr pro Baby)

Verarbeitung:
• Berechne Gesamtpreis für Erwachsene, Kinder, Babys
• Berechne Gesamtzahl der Passagiere
• Berechne Gesamtkosten

Ausgabe:
• Gesamtzahl Passagiere
• Gesamtkosten in Euro                 '''

#Eingabe
erwachsene = int(input('Anzahl Erwachsener : '))
kinder = int(input('Anzahl Kinder : '))
babys = int(input('Anzahl Babys : '))

#Berechnungen
gesamt_preis_erwachsene = erwachsene *320
gesamt_preis_kinder = kinder *180
gesamt_preis_babys = babys * 25

gesamt_zahl_passagiere = erwachsene + kinder + babys

gesamt_kosten = gesamt_preis_erwachsene + gesamt_preis_kinder + gesamt_preis_babys


print('Die Gesamte Anzahl der Passagiere: ', gesamt_zahl_passagiere)
print('Die Gesamtkosten belaufen sich auf: ', gesamt_kosten)









'''Aufgabe Aufgabe 5: Handwerker - Farbbedarf
Szenario: Ein Maler berechnet, wie viel Farbe für eine Wand benötigt wird.
Eingabe:
• Wandhöhe in Metern (z.B. 2.5)
• Wandbreite in Metern (z.B. 4.0)
• Anzahl der Wände (gleiche Größe)
Verarbeitung:
• Berechne Fläche einer Wand (Höhe × Breite)
• Berechne Gesamtfläche aller Wände
• Pro Quadratmeter werden 0.15 Liter Farbe benötigt
• Berechne Farbbedarf in Litern (auf 1 Nachkommastelle gerundet)
Ausgabe:
• Gesamtfläche in Quadratmetern
• Benötigte Farbe in Litern                '''

