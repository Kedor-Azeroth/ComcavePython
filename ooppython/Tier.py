
class Tier:

    def __init__(self, name, gewicht):
        self.name = name
        self.gewicht = gewicht
    
    def get_gewicht(self):
        return str(self.gewicht) + " kg"

class Saeugetier(Tier):

    def __init__(self, name, gewicht, anzahl_beine):
        super().__init__(name, gewicht)
        self.anzahl_beine = anzahl_beine

class Hund(Saeugetier):

    def __init__(self, name, gewicht, anzahl_beine, fellfarbe):
        super().__init__(name, gewicht, anzahl_beine)
        self.fellfarbe = fellfarbe

    def get_gewicht(self):
        return str(self.gewicht + 10) + " kg" 

tier_1 = Tier("Albert", 30)
saeugetier_1 = Saeugetier("Berta", 20, 3)
hund_1 = Hund("Charlie", 60, 4, "braun")

print(saeugetier_1.name, saeugetier_1.gewicht, saeugetier_1.anzahl_beine)
print(saeugetier_1.get_gewicht())

print(hund_1.name, hund_1.fellfarbe)

print(hund_1.get_gewicht())

###############################################################

class A:
    def f(self):
        return "A"

class B:
    def f(self):
        return "B"

class C:
    def f(self):
        return "C"

class D:
    pass

def g(obj):
    print(obj.f())

a = A()
b = B()
c = C()
d = D()

g(a)
g(b)
g(c)
g(d)