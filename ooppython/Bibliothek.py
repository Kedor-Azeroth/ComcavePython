class Bibliothek:

    def __init__(self, name, anzahlBuecher = 0, oeffnungszeiten = None, hatLesesaal = False, gruendungsjahr = 2026):
        self.name = name
        self.anzahlBuecher = anzahlBuecher
        self.oeffnungszeiten = oeffnungszeiten
        self.hatLesesaal = hatLesesaal
        if self.oeffnungszeiten:
            self.hatLesesaal = True
        self.gruendungsjahr = gruendungsjahr

    def zeigeAlleAttribute(self):
        print("Name:", self.name)
        print("Anzahl Bücher:", self.anzahlBuecher)
        print("Öffnungszeiten:", self.oeffnungszeiten)
        print("Hat Lesesaal?", self.hatLesesaal)
        print("Gründungsjahr:", self.gruendungsjahr)
      

meine_Bib = Bibliothek("Stadtbibliothek")
meine_Bib.zeigeAlleAttribute()
print()

meine_Bib = Bibliothek("Uni-Bibliothek", oeffnungszeiten = "Mo-Fr 8-20")
meine_Bib.zeigeAlleAttribute()
print()

meine_Bib = Bibliothek("Schulbibliothek", oeffnungszeiten = "Mo-Do 8-16", gruendungsjahr = 1975)
meine_Bib.zeigeAlleAttribute()
print()

meine_Bib = Bibliothek("Fahrbibliothek")
meine_Bib.zeigeAlleAttribute()
print()

