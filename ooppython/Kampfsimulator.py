# identität gibt Python selbst random.randint(5, 5)
import random

class Krieger:

    def __init__(self, name: str = "Unbekannt", lebenspunkte: int = 100, staerke: int = 10, ruestung: int = 5):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.staerke = staerke
        self.ruestung = ruestung

    def status(self):
        print("Krieger:", self.name, "- Lebenspunkte:", self.lebenspunkte)

    def angreifen(self, gegner):
        schaden = self.staerke - gegner.ruestung + random.randint(0, 20)
        if schaden < 1:
            schaden = 1
        gegner.lebenspunkte = gegner.lebenspunkte - schaden

    def heilen(self):
        self.lebenspunkte = self.lebenspunkte + random.randint(10, 20)
        if self.lebenspunkte > 100:
            self.lebenspunkte = 100

    def ist_am_leben(self):
        if self.lebenspunkte > 0:
            return True
        else:
            return False

#########################################################

krieger_1 = Krieger("Aragorn", staerke=15, ruestung=3)
krieger_2 = Krieger("Legolas", staerke=15, ruestung=3)
print("Status:")
krieger_1.status()
krieger_2.status()


while krieger_1.ist_am_leben() and krieger_2.ist_am_leben():

    krieger_1.angreifen(krieger_2)
    krieger_2.angreifen(krieger_1)

    if not krieger_1.ist_am_leben() and not krieger_2.ist_am_leben():
        print("Beide wurden besiegt!")
        break
    elif not krieger_1.ist_am_leben():
        print(krieger_1.name, "wurde besiegt!")
        break
    elif not krieger_2.ist_am_leben():
        print(krieger_2.name, "wurde besiegt!")
        break

    krieger_1.heilen()
    krieger_2.heilen()

    print("Status:")
    krieger_1.status()
    krieger_2.status()

    
   #Lösung2 Übung 1: Charakter-Kampf-System
import random
class Krieger:
    def __init__(self, name="Unbekannt", lebenspunkte=100, staerke=10,ruestung=5):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.staerke = staerke
        self.ruestung = ruestung
    
    def angreifen(self, gegner):
            schaden = self.staerke - gegner.ruestung
            if schaden < 1:
                schaden = 1
            gegner.lebenspunkte -= schaden
            if gegner.lebenspunkte < 0:
                gegner.lebenspunkte = 0
            print(f"{self.name} greift {gegner.name} an und verursacht {schaden}Schaden!")
    def heilen(self):
            self.lebenspunkte += 20
            if self.lebenspunkte > 100:
                self.lebenspunkte = 100
            print(f"{self.name} heilt sich auf {self.lebenspunkte} Lebenspunkte.")
    def ist_am_leben(self):
            return self.lebenspunkte > 0
    def status_anzeigen(self):
            print(f"{self.name}: {self.lebenspunkte} LP, Stärke: {self.staerke}, Rüstung: {self.ruestung}")
# Testcode
krieger1 = Krieger("Aragorn", 100, 15, 3)
krieger2 = Krieger("Legolas", 100, 12, 2)
print("=== Beginn des Kampfes ===")
krieger1.status_anzeigen()
krieger2.status_anzeigen()
print()
for runde in range(1, 6):
    print(f"--- Runde {runde} ---")
# Krieger1 greift an
    if krieger1.ist_am_leben() and krieger2.ist_am_leben():
        krieger1.angreifen(krieger2)
        if not krieger2.ist_am_leben():
            print(f"{krieger2.name} wurde besiegt!")
        break

# Krieger2 greift an
    if krieger1.ist_am_leben() and krieger2.ist_am_leben():
        krieger2.angreifen(krieger1)
        if not krieger1.ist_am_leben():
            print(f"{krieger1.name} wurde besiegt!")
        break
# Nach der Runde heilen sich beide
    if krieger1.ist_am_leben():
        krieger1.heilen()   
    if krieger2.ist_am_leben():
        krieger2.heilen()
    print()
    krieger1.status_anzeigen()
    krieger2.status_anzeigen()
    print()
# Ergebnis
    print("=== Kampfende ===")
    if krieger1.ist_am_leben() and krieger2.ist_am_leben():
        print("Unentschieden - beide Krieger leben noch!")
    elif krieger1.ist_am_leben():
        print(f"{krieger1.name} hat gewonnen!")
    elif krieger2.ist_am_leben():
        print(f"{krieger2.name} hat gewonnen!")
    else:
        print("Beide Krieger sind gefallen - Unentschieden!")

