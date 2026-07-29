# Klassen in Python definieren
x = 3
print(type(x))
# x ist ein Objekt, instanziiert von der Klasse int
# Ausgabe: <class 'int'>
######################################################################################################
def f():
    pass
print(type(f))
# f ist ein Objekt, instanziiert von der Klasse function
# Ausgabe: <class 'function'>

print(type(int))
print(type(type))
#########################################################################################################
class SmartPhone:                                           #CamelCase
    akkustand = 15
    eingeschaltet = False
    offeneApps = 0
    flugmodus = False         

#print(SmartPhone)
mein_handy = SmartPhone()
print('Akkustand',mein_handy.akkustand)
print('ist eingeschaltet',mein_handy.eingeschaltet)
print('offene App"s',mein_handy.offeneApps)
print('Flugmodus eingeschaltet',mein_handy.flugmodus)
mein_handy.akkustand = 30                                 # änderung im Objekt
print('Akkustand',mein_handy.akkustand)