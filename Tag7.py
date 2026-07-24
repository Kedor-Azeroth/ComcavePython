'Zusammenfassung'
import random

bot_nr = random.randint(1,10) # zufälliger int zw. 1 & 10
usr_nr = int(input('Zahl'))

if usr_nr == bot_nr:
    print('Win')
else:
    print('Nochmal')
    usr_nr = int(input('Zahl'))
    if usr_nr == bot_nr:
        print('you Win')
    else:
        print('verloren')
        print('botnr=',bot_nr)

import random

bot_nr = random.randint(1,10) # zufälliger int zw. 1 & 10
usr_nr = int(input('Zahl'))

if usr_nr == bot_nr:
    print('Win')
else:
    print('Nochmal')
    usr_nr = int(input('Zahl'))
    if usr_nr == bot_nr:
        print('you Win')
    else:
        print('Nochmal')
        usr_nr = int(input('Zahl'))
        if usr_nr == bot_nr:
            print('you Win')

        
        else:
            print('Nochmal')
            usr_nr = int(input('Zahl'))
            if usr_nr == bot_nr:
                print('you Win')
            else:
                print('verloren')
                print('botnr=',bot_nr)
#Python nur kopf & Zählschleifen
#nicht wahr schleife verlassen#
versuche = 3
print (bot_nr)

while versuche > 0:
    usr_nr = int(input('Zahl'))

    if usr_nr == bot_nr:
        print('Win')
        versuche = 0

    else:
            print('Leider falsch')
            versuche = versuche -1

#alternative
import random
print('Bitte nur ganz Zahlen:')
bot_nr = random.randint(1,10) # zufälliger int zw. 1 & 10
print (bot_nr)
versuche = 3


while versuche > 0:
    try:
        usr_nr = int(input('Zahl'))
        if usr_nr <1 or usr_nr > 10:
            raise ValueError
    except ValueError:
        print('Fehler')
        versuche = versuche -1

    if usr_nr == bot_nr:
        print('Win')
        break

    else:
        print('Leider falsch')
        versuche = versuche -1      

#Erweiterung     
import random

print("Bitte nur Ganzzahlen zwischen 1 und 10 eingeben")
bot_nr = random.randint(1, 10) # zufälliger int zw. 1 und 10
print(bot_nr)

versuche = 3
while versuche > 0:
    print("Du hast noch", versuche, "Versuche.")
    try:
        usr_nr = int(input("Zahl: "))
        if usr_nr < 1 or usr_nr > 10:
            raise ValueError
    except ValueError:
        print("Das ist keine valide Eingabe!")
        versuche = versuche - 1
    else:
        if usr_nr == bot_nr:
            print("Du hast gewonnen!")
            break
        else:
            print("Leider falsch!")
            versuche = versuche - 1

print("Der Computer hatte gewählt:", bot_nr)        

# index:     0    1    2
my_list = [100, 120, 140]

print(my_list[0]) # erstes Element
print(my_list[1]) # zweites Element
print(my_list[2]) # drittes Element
#print(my_list[3]) IndexError -> Index 3 existiert nicht!
print(my_list[-1]) # letztes Element
print(my_list[-2]) # vorletztes Element
print(my_list[-3]) # vorvorletztes Element
#print(my_list[-4]) IndexError -> Index -4 existiert nicht!

x = my_list[0]

# Elemente hinzufügen:
my_list.append(160) # ein Element ans Ende
my_list.extend([180, 200]) # mehrere Elemente ans Ende
#my_list = my_list + [180, 200] # selber Effekt wie in der Zeile davor
my_list.insert(0, 80) # ein Element in beliebiger Position

print(my_list)

# Elemente entfernen:
#my_list.clear() # entfernt alle Elemente
#print(my_list)
my_list.pop() # letztes Element entfernen
my_list.pop(0) # beliebiges Element über den Index entfernen (hier: das erste Element)
my_list.remove(120) # beliebiges Element über den Wert entfernen
print(my_list)
if 2000 in my_list: # prüfe, ob 2000 in der Liste vorkommt
    my_list.remove(2000) # entferne den Wert 2000

# Elemente verändern:
my_list[0] = 120
print(my_list)

# Weitere Möglichkeiten:
print(my_list.count(140)) # Zählen, wie oft die 140 vorkommt
print(my_list.index(120)) # Position (=Index), in der sich das Element 120 befindet
#print(my_list.index(2000)) # ValueError, da Element 2000 nicht existiert
my_list.reverse() # Liste umdrehen: [100, 140, 160, 180] -> [180, 160, 140, 120]
print(my_list)
my_list.sort()
print(my_list)
#iterieren: im Satz wiederholen,  iteration: eine Iteration vornehmen; wiederholen, um sich einer schrittweisen Lösung zu nähern
#wir iterieren my_list
# index     0    1    2    3    4    5    6
my_list = [80, 100, 120, 140, 160, 180, 200]

for elem in my_list:
    print(elem)

for i, elem in enumerate(my_list):
    print("Index:", i)
    print("Element:", elem)
    print()

for i in range(100):
    x = 1
    #print(i)
