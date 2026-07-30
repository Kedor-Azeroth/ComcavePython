class Kunde:

    def __init__(self, name, guthaben):
        self.name = name
        self.guthaben = guthaben
        self.warenkorb = Warenkorb([])

    def abheben(self, betrag):
        if betrag <= self.guthaben:
            self.guthaben = self.guthaben - betrag
            return True
        else:
            return False

    def guthabenAnzeigen(self):
        return self.guthaben

class Produkt:

    def __init__(self, name, preis):
        self.name = name
        self.preis = preis

class Warenkorb:

    def __init__(self, produkte):
        self.produkte = produkte

    def produkteAnzeigen(self):
        produkt_namen = []
        for elem in self.produkte:
            produkt_namen.append(elem.name)
        return produkt_namen

    def produktHinzufuegen(self, produkt):
        for elem in self.produkte:
            if produkt.name == elem.name:
                return

        self.produkte.append(produkt)

    def produktEntfernen(self, produkt):
        for i, elem in enumerate(self.produkte):
            if produkt.name == elem.name:
               self.produkte.pop(i)

    def gesamtpreisBerechnen(self):
        gesamtpreis = 0.0
        for elem in self.produkte:
            gesamtpreis = gesamtpreis + elem.preis
        return gesamtpreis

    def bezahlen(self, kunde: Kunde):
        if len(self.produkte) == 0:
            return
        gesamtpreis = self.gesamtpreisBerechnen()
        abheben_erfolgreich = kunde.abheben(gesamtpreis)
        if abheben_erfolgreich:
            self.warenkorbLeeren()
            return True
        else:
            return False

    def warenkorbLeeren(self):
        self.produkte.clear()


#######################################################################

kunde_1 = Kunde("Max", 150.0)
produkt_1 = Produkt("Buch", 25.0)
produkt_2 = Produkt("Stift", 5.0)
produkt_3 = Produkt("Tasche", 120.0)

print("1. max ruft auf seinem Warenkorb produktHinzufuegen(buch) auf")
kunde_1.warenkorb.produktHinzufuegen(produkt_1)
print(kunde_1.warenkorb.produkteAnzeigen())
print()

print("2. max ruft auf seinem Warenkorb produktHinzufuegen(stift) auf")
kunde_1.warenkorb.produktHinzufuegen(produkt_2)
print(kunde_1.warenkorb.produkteAnzeigen())
print()

print("3. max ruft auf seinem Warenkorb produktHinzufuegen(tasche) auf")
kunde_1.warenkorb.produktHinzufuegen(produkt_3)
print(kunde_1.warenkorb.produkteAnzeigen())
print()

print("4. max ruft auf seinem Warenkorb produktHinzufuegen(stift) auf (nochmal)")
kunde_1.warenkorb.produktHinzufuegen(produkt_2)
print(kunde_1.warenkorb.produkteAnzeigen())
print()

print("5. max ruft auf seinem Warenkorb produktEntfernen(stift) auf")
kunde_1.warenkorb.produktEntfernen(produkt_2)
print(kunde_1.warenkorb.produkteAnzeigen())
print()

print("6. max ruft auf seinem Warenkorb gesamtpreisBerechnen() auf")
print(kunde_1.warenkorb.gesamtpreisBerechnen())
print()

print("7. max ruft auf seinem Warenkorb bezahlen(max) auf")
kunde_1.warenkorb.bezahlen(kunde_1)
print(kunde_1.warenkorb.produkteAnzeigen())
print()

print("8. max ruft guthabenAnzeigen() auf")
print(kunde_1.guthabenAnzeigen(), "€")
