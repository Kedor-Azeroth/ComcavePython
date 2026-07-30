# test.py
#

class Rezept:
    def __init__(self, titel, zubereitungszeit, schwierigkeitsgrad, zutaten = None):
        self.titel = titel
        self.zubereitungszeit = zubereitungszeit
        self.schwierigkeitsgrad = schwierigkeitsgrad
        if zutaten is None:
            self.zutaten = []
        else:
            self.zutaten = zutaten.copy()

    def __str__(self):
        return "Das Rezept heisst " + self.titel + " und ist in " + str(self.zubereitungszeit) + " min. zubereitet!"

    def zutatHinzufuegen(self, zutat):
        for elem in self.zutaten:
            if zutat == elem:
                return False
        self.zutaten.append(zutat)
        return True

    def zutatEntfernen(self, zutat):
        for i,elem in enumerate(self.zutaten):
            if zutat == elem:
                self.zutaten.pop(i)

    def zeigeRezept(self):
        if len(self.zutaten) == 0:
            print("Es wurden noch keine Zutaten eingetragen")
        else:
            print("Zutatenliste für "+self.titel)
            for elem in self.zutaten:
                print(elem)
            print()


    def benoetigtZutat(self, zutat):
        for elem in self.zutaten:
            if zutat == elem.name:
                return True

        return False

pizza = Rezept("Pizza",25,"einfach")
print(pizza)
pizza.zutatHinzufuegen("Käse")
pizza.zeigeRezept()
pizza.zutatHinzufuegen("Tomatensauce")
pizza.zeigeRezept()

pizza.zutatEntfernen("Käse")
pizza.zeigeRezept()
pizza.zutatHinzufuegen("Käse")
pizza.zeigeRezept()

pflaumenkuchen = Rezept("Pflaumenkuchen",60,"mittel")
pflaumenkuchen.zutatHinzufuegen("Pflaumen")
pflaumenkuchen.zutatHinzufuegen("Hefe")
pflaumenkuchen.zutatHinzufuegen("Mehl")
pflaumenkuchen.zeigeRezept()

pommes = Rezept("Pommes",10,"einfach",["Kartoffeln","Öl","Salz"])
pommes.zeigeRezept()

rezeptliste=[]
rezeptliste.append(pizza)
rezeptliste.append(pflaumenkuchen)
rezeptliste.append(pommes)

print("Rezepte kürzer als 30 min.:")
for elem in rezeptliste:
    if elem.zubereitungszeit < 30:
        print(elem.titel)

print()
print("Alle Rezepte in Liste:")
for elem in rezeptliste:
    print(elem.titel)
    
    
#Lösung Übung 2: Rezept-Manager

class Rezept:
    def __init__(self, titel, zubereitungszeit, schwierigkeitsgrad,zutaten=None):
        self.titel = titel
        self.zubereitungszeit = zubereitungszeit
        self.schwierigkeitsgrad = schwierigkeitsgrad
        if zutaten is None:
            self.zutaten = []
        else:
            self.zutaten = zutaten.copy()
    def zutat_hinzufuegen(self, zutat):
        if zutat not in self.zutaten:
            self.zutaten.append(zutat)
            print(f"Zutat '{zutat}' wurde hinzugefügt.")
        else:
            print(f"Zutat '{zutat}' ist bereits im Rezept.")
    def zutat_entfernen(self, zutat):
        if zutat in self.zutaten:
            self.zutaten.remove(zutat)

            print(f"Zutat '{zutat}' wurde entfernt.")
        else:
            print(f"Zutat '{zutat}' nicht im Rezept gefunden.")
    def zeige_rezept(self):
        print("=" * 50)
        print(f"Titel: {self.titel}")
        print(f"Zubereitungszeit: {self.zubereitungszeit} Minuten")
        print(f"Schwierigkeitsgrad: {self.schwierigkeitsgrad}")
        print("Zutaten:")
        if self.zutaten:
            for i, zutat in enumerate(self.zutaten, 1):
                print(f" {i}. {zutat}")
        else:
            print(" (Keine Zutaten eingetragen)")
        print("=" * 50)
    def benoetigt_zutat(self, zutat):
        return zutat in self.zutaten
    def __str__(self):
        return f"{self.titel} ({self.zubereitungszeit} min)"
# Testcode
rezept1 = Rezept("Spaghetti Carbonara", 25, "mittel", ["Spaghetti", "Eier",
"Pancetta", "Parmesan", "Pfeffer"])
rezept2 = Rezept("Salat", 10, "einfach", ["Salat", "Tomaten", "Gurken",
"Dressing"])
rezept3 = Rezept("Rinderbraten", 120, "schwer", ["Rindfleisch", "Zwiebeln",
"Karotten", "Rotwein"])
# Methoden testen
print("=== Rezept 1 testen ===")
rezept1.zeige_rezept()
rezept1.zutat_hinzufuegen("Petersilie")
rezept1.zutat_hinzufuegen("Parmesan") # Doppelt
rezept1.zutat_entfernen("Pfeffer")
rezept1.zeige_rezept()
print("\n=== Rezept 2 testen ===")
print(f"Benötigt Salat? {rezept2.benoetigt_zutat('Salat')}")
print(f"Benötigt Käse? {rezept2.benoetigt_zutat('Käse')}")
print(rezept2) # __str__ testen
print("\n=== Alle Rezepte ===")
rezepte = [rezept1, rezept2, rezept3]
for rezept in rezepte:
    print(rezept)
print("\n=== Schnelle Rezepte (< 30 Minuten) ===")
schnelle_rezepte = [r for r in rezepte if r.zubereitungszeit < 30]
for rezept in schnelle_rezepte:
    print(f" {rezept}")
