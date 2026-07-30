class Krieger:
    def __init__(self, name="Unbekannt", lebenspunkte=100, staerke=10, ruestung=5):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.staerke = staerke
        self.ruestung = ruestung

    def ist_am_leben(self):
        return self.lebenspunkte > 0

    def angreifen(self, gegner):
        schaden = Krieger.schaden_berechnen(self.staerke, self.ruestung)
        gegner.lebenspunkte = gegner.lebenspunkte - schaden

    @classmethod
    def from_name(cls, name): # cls wichtig
        return cls(name)

    @staticmethod
    def schaden_berechnen(staerke, ruestung):
        schaden = staerke - ruestung
        if schaden < 1:
            schaden = 1
        return schaden

krieger_1 = Krieger()
krieger_2 = Krieger.from_name("Max")
print(krieger_1.ist_am_leben())
print(krieger_2.ist_am_leben())