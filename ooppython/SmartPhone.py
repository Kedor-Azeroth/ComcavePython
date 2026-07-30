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
            
            
        def einschalten (self):
            if self.akkuStand > 0:                    # Kann nur eingeschaltet werden bei Akku größer  0
                self.eingeschaltet = True
               
        def ausschalten(self):
            self.eingeschaltet = False                # SmartPhone kann immer ausgeschaltet werden
        
        def appOeffnen(self, appName):
            if self.eingeschaltet:
                self.offeneApps = self.offeneApps +1
                if not self.flugmodus:
                    self.akkuStand = self.akkuStand -2
                
        def appSchliessen(self, appName):
            if self.eingeschaltet:   
                self.offeneApps = self.offeneApps -1
                self.akkuStand = self.akkuStand +2
                
        def laden(self, minuten):
            if self.akkuStand + minuten > 100:
                self.akkuStand = 100
            else:    
                self.akkuStand = self.akkuStand + minuten
                
        def flugmodusUmschalten(self):
            if self.flugmodus:
                self.flugmodus = False
            else:
                self.flugmodus = True
                
            #|| self.flugmodus = not self.flugmodus        
            
        def akkuAnzeigen(self):  # Mehr Kontrolle über den Zugriff sowie über Private erreichbar.
            return str(self.akkuStand) + '%' 
        
        def alleAppsSchliessen(self):
            if self.appSchliessen:
                self.offeneApps = 0
            
        
        def getAkkustand(self) -> int:    # was holen int 
            return self.akkuStand
        
        def setAkkustand(self, akkuStand: int) -> None:     # setter kein Rückgabewerte nur Nebeneffekt None: nicht vorhanden.
            if type(akkuStand) == int:
                self.akkuStand = akkuStand
            else:
                raise TypeError('Akkustand muß int sein')    
        #for Zeile 69    #self,akkuStand = akkuStand                      # besser mit get und set Arbeien
        #Getter und Setter sind neben dem Konstruktor Standardmethoden einer Klasse.
        #Der Konstruktor konstruiert neue Objekte und wird zur Instanziierung einer Klasse verwendet.  
        #Der Getter (get)wird zum lesen bestehender Werte von Attributen gwtutzt
        #Der Setter (set) wird zum setzen oder verändern von Werten der Attribute genutzt.
        # Ich könnte pro Atribut(akkustand) getter und setter nutzen bei 4 Attribute kann ich 4 Getter und 4 Setter habe Also 8 Methoden.
  


#print(SmartPhone)
mein_handy1 = SmartPhone1(15, False)
#print('Akkustand',mein_handy1.akkuStand)
#print('Smartphone eingeschaltet ? = ',mein_handy1.eingeschaltet)
#mein_handy1.einschalten()     # Methode ausführen
#print('Smartphone eingeschaltet ? =',mein_handy1.eingeschaltet) # Abfrage 
#print('offene App"s',mein_handy1.offeneApps)
#print('Flugmodus eingeschaltet',mein_handy1.flugmodus)
#mein_handy1.ausschalten()
#print('Smartphone eingeschaltet ? =',mein_handy1.eingeschaltet)
#mein_handy1.einschalten() 
#mein_handy1.appOeffnen('Maps')
#print('Akkustand',mein_handy1.akkuStand)
#print('offene App"s',mein_handy1.offeneApps)
#mein_handy1.appSchliessen('Maps')
#print('Akkustand',mein_handy1.akkuStand)
#print('offene App"s',mein_handy1.offeneApps)
#mein_handy1.laden(12)
#print('Akkustand',mein_handy1.akkuStand)
#mein_handy1.flugmodusUmschalten()
#print('Flugmodus?',mein_handy1.flugmodus)
#mein_handy1.flugmodusUmschalten()
#print('Flugmodus?',mein_handy1.flugmodus)
#print()
print("mein_handy.einschalten()")
mein_handy1.einschalten() 
print('Akkustand',mein_handy1.akkuStand)
print('Smartphone eingeschaltet ? =',mein_handy1.eingeschaltet)
print('offene App"s',mein_handy1.offeneApps)
print('Flugmodus?',mein_handy1.flugmodus)

print("mein_handy.appOeffnen('Maps')")
mein_handy1.appOeffnen('Maps')
print('Akkustand',mein_handy1.akkuStand)
print('Smartphone eingeschaltet ? =',mein_handy1.eingeschaltet)
print('offene App"s',mein_handy1.offeneApps)
print('Flugmodus?',mein_handy1.flugmodus)

print("mein_handy.appOeffnen('Spotify')")
mein_handy1.appOeffnen('Spoti')
print('Akkustand',mein_handy1.akkuStand)
print('Smartphone eingeschaltet ? =',mein_handy1.eingeschaltet)
print('offene App"s',mein_handy1.offeneApps)
print('Flugmodus?',mein_handy1.flugmodus)

print("mein_handy.flugmodusUmschalten()")
mein_handy1.flugmodusUmschalten()
print('Akkustand',mein_handy1.akkuStand)
print('Smartphone eingeschaltet ? =',mein_handy1.eingeschaltet)
print('offene App"s',mein_handy1.offeneApps)
print('Flugmodus?',mein_handy1.flugmodus)

print("mein_handy.appOeffnen('WhatsApp')")
mein_handy1.appOeffnen("Whatsapp")
print('Akkustand',mein_handy1.akkuStand)
print('Smartphone eingeschaltet ? =',mein_handy1.eingeschaltet)
print('offene App"s',mein_handy1.offeneApps)
print('Flugmodus?',mein_handy1.flugmodus)


print("mein_handy.appSchliessen('Spotify')")
mein_handy1.appSchliessen("Spoti")
print('Akkustand',mein_handy1.akkuStand)
print('Smartphone eingeschaltet ? =',mein_handy1.eingeschaltet)
print('offene App"s',mein_handy1.offeneApps)
print('Flugmodus?',mein_handy1.flugmodus)


print("mein_handy.laden(30)")
mein_handy1.laden(30)
print('Akkustand',mein_handy1.akkuStand)
print('Smartphone eingeschaltet ? =',mein_handy1.eingeschaltet)
print('offene App"s',mein_handy1.offeneApps)
print('Flugmodus?',mein_handy1.flugmodus)

print("mein_handy.akkuAnzeigen()")
mein_handy1.akkuAnzeigen()
print('Akkustand',mein_handy1.akkuStand)
print('Smartphone eingeschaltet ? =',mein_handy1.eingeschaltet)
print('offene App"s',mein_handy1.offeneApps)
print('Flugmodus?',mein_handy1.flugmodus)

#print(mein_handy1.akkuAnzeigen())

#mein_handy1.setAkkustand(100)
#mein_handy1.setAkkustand('a')

print('Akkustand',mein_handy1.akkuStand)
print('Meine Handy.alleAppsSchliessen()')
mein_handy1.alleAppsSchliessen()