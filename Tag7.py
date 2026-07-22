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