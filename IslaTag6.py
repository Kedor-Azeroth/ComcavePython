'APFEL' .count ('P')  #Zählt die Anzahl der Buchstaben p in dem Wort APFEL
print('APFEL' .count ('P'))  # Ausgabe: 1


Mexiko = ['Mexiko', 'Deutschland', 'Brasilien', 'Argentinien', 'Frankreich']
print(Mexiko.count('Mexiko'))  # Ausgabe: 1
# Einzeilig Kommentare
''' Mehrzeilige Kommentare'''


''' Fussball Beispiel'''
# Pkt -> erreichte Punkte (S*3 + U*1 + N*0)
# AB -> Anzahl der absolvierten Spiele (S+U+N)
# S -> Anzahl der Siege (S = 3 Punkte)
# U -> Anzahl der Unentschieden (U = 1 Punkt)
# N -> Anzahl der Niederlagen (N = 0 Punkte)
#
''' EVA-Prinzip:
   Eingabe:

1) Anzahl der Siege (S)
2) Anzahl der Unentschieden (U)
3) Anzahl der Niederlagen (N)
4) Mannschaftsname (M) optional
 
   Verarbeitung:
1) Berechnung der Punktezahl  (Pkt = S*3 + U*1 + N*0)
2) Berechnung der absolvierten Begegnungen (AB = S+U+N)  

   Ausgabe:
1) Informative Darstellung der ermittleten Werte 



''' 
#Eingabe der Werte

mannschaftsname = input('Mannschaftsname : ')
anz_siege = int(input('Anzahl der Siege : '))
anz_unentschieden = int(input('Anzahl der Unentschieden : '))
anz_niederlagen = int(input('Anzahl der Niederlagen : '))

#Verarbeitung der Werte
#|| Umwandlung in eine Funktion
#anz_siege = int(anz_siege)
#anz_unentschieden = int(anz_unentschieden)
#anz_niederlagen = int(anz_niederlagen)
#

gesamt_punkte = anz_siege * 3 + anz_unentschieden * 1 + anz_niederlagen * 0
absolvierte_begegnungen = anz_siege +anz_unentschieden + anz_niederlagen    

#Ausgabe der Werte
print('Die ' ,mannschaftsname, ' hat',gesamt_punkte,'Punkte erreicht.')
# oder print('Deine Mannschaft ', mannschaft ,'hat folgedes erreicht:' )
print('Die ' , mannschaftsname,  ' hat',absolvierte_begegnungen,'Begegnungen absolviert.')
# || print('- Erreichte Puhkte :' gesamt_punkte)
# || print(' - Absolvierte Begegnungen:', ab )





