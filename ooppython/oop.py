# Kommentieren # oder '''    '''
# False und True immer Anfang Groß

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
class SmartPhone:                                         #CamelCase
  
    akkuStand = 15
    eingeschaltet = False
    offeneApps = 0
    flugmodus = False         

#print(SmartPhone)
mein_handy = SmartPhone()
print('Akkustand',mein_handy.akkuStand)
print('ist eingeschaltet',mein_handy.eingeschaltet)
print('offene App"s',mein_handy.offeneApps)
print('Flugmodus eingeschaltet',mein_handy.flugmodus)
mein_handy.akkuStand = 30                                 # änderung im Objekt
print('Akkustand',mein_handy.akkuStand)
#######################################################################################
class SmartPhone1:
      #Konstruktor
        def __init__(self, akkuStand, eingeschaltet ):  # muss nicht alles kann ist es nie eingeschaltet brauch man diese hier auch nicht../*offeneApps, flugmodus*/..                                
                                                             
                                                            #init initialisiert das Objekt mit Werten.
                                                            # 'self' = this. ist ein Platzhalter für das zukünftige Objekt.' 
                                                            #self' ist eine Referenz auf aktuelle Instanz (das aktuelle Objekt)
            self.akkuStand = akkuStand                      # links = objekt eigene AkkuStand ,rechts = Was beim Instanzieren mit gegeben wird. (15, False)
            self.eingeschaltet = eingeschaltet              # von unten nach oben und dan verteilt.!! Wie immer.
            self.offeneApps = 0
            self.flugmodus = False 



#print(SmartPhone)
mein_handy1 = SmartPhone1(15, False)

print('Akkustand',mein_handy1.akkuStand)
print('ist eingeschaltet',mein_handy1.eingeschaltet)
print('offene App"s',mein_handy1.offeneApps)
print('Flugmodus eingeschaltet',mein_handy1.flugmodus)
