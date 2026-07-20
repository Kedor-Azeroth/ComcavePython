'''Aufgabe 1'''
'''Starte den Python-Interpreter und gib folgendes ein:
• Deinen Vornamen als Zeichenkette
• Das Jahr 2026
• Eine Addition aus 15 und 27
Beende den Interpreter anschließend wieder.'''

print('Rene')
print(15 + 27)
print(2026)

'''Aufgabe 2 Berechne im interaktiven Modus:
• 1234 × 567
• 100 geteilt durch 3 (als Gleitkommazahl)
• Den Rest von 17 geteilt durch 5
• 2 hoch 10'''

print(1234 * 567)
print(100 / 3)
print(17 % 5)
print(2 ** 10)

'''Aufgabe 3 Finde mit der passenden Funktion heraus, welchen Typ folgende Werte haben:
• 3.14159
• "True" (mit Anführungszeichen)
• True (ohne Anführungszeichen)
• 42'''

print (type(3.14159))    #type(3.14159) float
print (type("True"))      #type("True") str
print (type(True))        #type(True)  bool
print (type(42))          #type(42)   int

'''Aufgabe 4 Lege diese Variablen an:
• stadt = "Berlin"
• einwohner = 3600000
• flaeche = 891.7
Gib dann nacheinander jede Variable ein, um ihren Wert anzuzeigen.
Berechne die Einwohnerdichte: einwohner / flaeche'''

stadt = "Berlin"
einwohner = 3600000
flaeche = 891.7
print(stadt)
print(einwohner)
print(flaeche)
print(einwohner / flaeche)

'''Aufgabe 5 Erzeuge mit Variablen diesen Satz:
„Mein Name ist Max und ich wohne in Hamburg.“
Verwende dafür:
• name = "Max"
• ort = "Hamburg"
• Und die print()-Funktion mit mehreren Argumenten oder +
'''

name = "Max"
ort = "Hamburg"
print("Mein Name ist " + name + " und ich wohne in " + ort + ".")


'''Aufgabe 6 Nutze input(), um nach deinem Lieblingsessen zu fragen.
Speichere die Antwort in einer Variable und gib dann aus:
„Lecker, [Essen] mag ich auch!“'''

essen = input ('Lieblingsfutter')
'''Lieblingsfutter fisch'''
print ('Lecker ' + essen + 'mag ich auch!')


'''Aufgabe 7 Speichere "Python-Kurs" in einer Variable.
• Gib die Länge des Strings mit len() aus.
• Wandle den String mit .upper() in Großbuchstaben um.
• Wandle ihn mit .lower() in Kleinbuchstaben um.
'''

py = 'Python-Kurs'
print(len(py))
print(py.upper())
print(py.lower())    




'''Aufgabe 8 Öffne die Hilfe für die Funktion print().
Lies die Beschreibung und beende die Hilfe wieder mit q.
Finde mit dir() alle Methoden eines Strings (z. B. von "test") und probiere zwei davon aus,
die du noch nicht kennst (z. B. .swapcase() oder .count()).'''

'''Nur q beenden und quit, exit verlassen'''

print(dir('Test'))
A = 'Hallo Ihr mein Name ist Rene'
B = A.swapcase()
print (B)


fruits = ['apple', 'banana', 'cherry', 'date', 'cherry']
x = fruits.count("cherry")
print(x)

'Apple' .count ('p')  #Zählt die Anzahl der Buchstaben p in dem Wort Apple



fruits = ["apple", "banana", "cherry"] 
x = len(fruits) 
print(x)

'''Aufgabe 9 • print("Hallo) (fehlendes Anführungszeichen)
• print(alter) (Variable existiert nicht)
• "5" + 3 (unterschiedliche Typen)
• 10 / 0 (Division durch Null)
Korrigiere danach jeden Befehl, sodass er funktioniert'''
#Semikolon fehlt
#String und Integer können nicht addiert werden, daher muss die 3 in einen String umgewandelt werden
#division durch Null ist nicht möglich, daher muss die 0 durch eine andere Zahl ersetzt werden

print('Hallo')   
alter = 25
print(alter)  
print('5' + '3')  #'5' + str(3) 
print(10/1) 



