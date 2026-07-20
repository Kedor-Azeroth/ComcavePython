
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



