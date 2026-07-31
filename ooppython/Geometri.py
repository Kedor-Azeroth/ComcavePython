# Lösung Übung 3: Geometrie-Bibliothek
import math
from abc import ABC, abstractmethod
from typing import Dict, Any, Union, List, Optional
from collections.abc import Iterable

# Teil A: Abstrakte Basisklasse und konkrete Klassen

class Shape(ABC):
    """Abstrakte Basisklasse für geometrische Formen"""
    
    @abstractmethod
    def area(self) -> float:
        """Berechnet die Fläche der Form"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Berechnet den Umfang der Form"""
        pass
    
    def describe(self) -> str:
        """Gibt eine Beschreibung der Form zurück"""
        return f"This is a {type(self).__name__}"
   
    # Teil C: Klassenmethoden
    
    @classmethod
    def create_shape(cls, shape_type: str, *args) -> 'Shape':
        """
        Fabrikmethode zum Erstellen verschiedener Shapes
        Args:
        shape_type: "rectangle", "circle", oder "triangle"
        *args: Parameter für die jeweilige Form
        Returns:
        Shape-Objekt
        """
        shape_type = shape_type.lower()
        if shape_type == "rectangle":
            if len(args) != 2:
                raise ValueError("Rectangle needs width and height")
            return Rectangle(*args)
        elif shape_type == "circle":
            if len(args) != 1:
                raise ValueError("Circle needs radius")
            return Circle(*args)
        elif shape_type == "triangle":
            if len(args) != 3:
                raise ValueError("Triangle needs three sides")
            return Triangle(*args)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
    
    # Teil D: Statische Methoden
        
    @staticmethod
    def is_valid_shape(obj: Any) -> bool:
        """
        Prüft, ob ein Objekt alle Shape-Methoden implementiert
        Args:
        obj: Das zu prüfende Objekt
        Returns:
        True wenn alle Methoden vorhanden sind, sonst False
        """
        required_methods = ['area', 'perimeter', 'describe']
        return all(hasattr(obj, method) and callable(getattr(obj, method))
                   for method in required_methods)
    
    @staticmethod
    def calculate_pythagoras(a: float, b: float) -> float:
        """
        Berechnet die Hypotenuse mit dem Satz des Pythagoras
        Args:
        a, b: Katheten
        Returns:
        Hypotenuse
        """
        return math.sqrt(a**2 + b**2)
    
    @staticmethod
    def is_triangle_valid(side1: float, side2: float, side3: float) -> bool:
        """
        Prüft die Dreiecksungleichung
        Args:
        side1, side2, side3: Seitenlängen
        Returns:
        True wenn gültiges Dreieck, sonst False
        """
        return (side1 + side2 > side3 and
                side2 + side3 > side1 and
                side1 + side3 > side2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
   
    # Teil C: Klassenmethoden
       
    @classmethod
    def from_dict(cls, data: Dict[str, float]) -> 'Rectangle':
        """Erstellt Rectangle aus Dictionary"""
        return cls(data['width'], data['height'])
    
    @classmethod
    def from_string(cls, shape_string: str) -> 'Rectangle':
        """Erstellt Rectangle aus String 'Rectangle:width,height'"""
        parts = shape_string.split(':')[1].split(',')
        return cls(float(parts[0]), float(parts[1]))

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius**2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    # Teil C: Klassenmethoden
    
    @classmethod
    def from_dict(cls, data: Dict[str, float]) -> 'Circle':
        """Erstellt Circle aus Dictionary"""
        return cls(data['radius'])
    
    @classmethod
    def from_string(cls, shape_string: str) -> 'Circle':
        """Erstellt Circle aus String 'Circle:radius'"""
        radius = float(shape_string.split(':')[1])
        return cls(radius)
    
    @classmethod
    def from_diameter(cls, diameter: float) -> 'Circle':
        """Erstellt Circle aus Durchmesser"""
        return cls(diameter / 2)

    # Teil D: Statische Methoden
      
    @staticmethod
    def pi_approx(n: int) -> float:
        """
        Berechnet Pi mittels Leibniz-Formel
        π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
        Args:
        n: Anzahl der Iterationen
        Returns:
        Annäherung von Pi
        """
        if n <= 0:
            raise ValueError("n must be positive")
        pi_approx = 0
        for i in range(n):
            term = 1 / (2*i + 1)
            if i % 2 == 0:
                pi_approx += term
            else:
                pi_approx -= term
        return pi_approx * 4

class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float):
        # KORREKTUR: Shape.is_triangle_valid statt self.is_triangle_valid
        if not Shape.is_triangle_valid(side1, side2, side3):
            raise ValueError("Invalid triangle sides")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self) -> float:
        """Berechnet Fläche mittels Heron'scher Formel"""
        s = self.perimeter() / 2  # Semiperimeter
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3
   
    # Teil C: Klassenmethoden
    
    @classmethod
    def from_dict(cls, data: Dict[str, float]) -> 'Triangle':
        """Erstellt Triangle aus Dictionary"""
        return cls(data['side1'], data['side2'], data['side3'])
    
    @classmethod
    def from_string(cls, shape_string: str) -> 'Triangle':
        """Erstellt Triangle aus String 'Triangle:side1,side2,side3'"""
        parts = shape_string.split(':')[1].split(',')
        return cls(float(parts[0]), float(parts[1]), float(parts[2]))

# Teil B: Polymorphie ohne Vererbung (Duck Typing)

# KORREKTUR: Diese Funktionen müssen außerhalb der Klassen definiert werden
def print_shape_info(shape):
    """
    Gibt Informationen über eine Form aus.
    Funktioniert mit jedem Objekt, das area(), perimeter() und describe() hat.
    """
    print(f"\n{shape.describe()}")
    print(f" Area: {shape.area():.2f}")
    print(f" Perimeter: {shape.perimeter():.2f}")

def print_area_comparison(shape1, shape2):
    """
    Vergleicht die Flächen zweier Formen.
    Funktioniert mit jedem Objekt, das area() hat.
    """
    area1 = shape1.area()
    area2 = shape2.area()
    print(f"\nFlächenvergleich:")
    print(f" Shape 1: {area1:.2f}")
    print(f" Shape 2: {area2:.2f}")
    if area1 > area2:
        print(f" Shape 1 ist größer (Differenz: {area1 - area2:.2f})")
    elif area2 > area1:
        print(f" Shape 2 ist größer (Differenz: {area2 - area1:.2f})")
    else:
        print(" Beide Shapes haben die gleiche Fläche")

# Zusätzliche Herausforderung (optional): ShapeCollection

class ShapeCollection(Iterable):
    """Collection für Shape-Objekte"""
    
    def __init__(self, shapes: Optional[List[Shape]] = None):
        self._shapes = shapes if shapes is not None else []
    
    def add_shape(self, shape: Shape) -> None:
        self._shapes.append(shape)
    
    def remove_shape(self, index: int) -> Optional[Shape]:
        if 0 <= index < len(self._shapes):
            return self._shapes.pop(index)
        return None
    
    def total_area(self) -> float:
        return sum(shape.area() for shape in self._shapes)
    
    def average_area(self) -> float:
        if not self._shapes:
            return 0.0
        return self.total_area() / len(self._shapes)
    
    def get_shapes_by_type(self, shape_type: str) -> List[Shape]:
        """Filtert Shapes nach Typ (Klassenname)"""
        return [s for s in self._shapes
                if type(s).__name__.lower() == shape_type.lower()]
    
    def __iter__(self):
        return iter(self._shapes)
    
    def __len__(self) -> int:
        return len(self._shapes)
    
    def __repr__(self) -> str:
        return f"ShapeCollection({len(self._shapes)} shapes)"

# Teil E: Hauptprogramm
def main():
    print("="*60)
    print("GEOMETRIE-BIBLIOTHEK - DEMONSTRATION")
    print("="*60)
   
    # Teil A & B: Shapes erstellen und Polymorphie demonstrieren

    print("\n" + "="*60)
    print("TEIL A & B: Shapes und Polymorphie")
    print("="*60)
    
    # Shapes mit Konstruktor erstellen
    rect1 = Rectangle(10, 5)
    circle1 = Circle(7)
    triangle1 = Triangle(3, 4, 5)
    
    # print_shape_info demonstriert Polymorphie
    print_shape_info(rect1)
    print_shape_info(circle1)
    print_shape_info(triangle1)
    
    # Flächenvergleich
    print_area_comparison(rect1, circle1)
    print_area_comparison(circle1, triangle1)
  
    # Teil C: Klassenmethoden

    print("\n" + "="*60)
    print("TEIL C: Klassenmethoden")
    print("="*60)
    
    # from_dict()
    rect2 = Rectangle.from_dict({'width': 8, 'height': 6})
    circle2 = Circle.from_dict({'radius': 5})
    triangle2 = Triangle.from_dict({'side1': 6, 'side2': 8, 'side3': 10})
    print_shape_info(rect2)
    print_shape_info(circle2)
    print_shape_info(triangle2)
    
    # from_string()
    rect3 = Rectangle.from_string("Rectangle:12,4")
    circle3 = Circle.from_string("Circle:3.5")
    triangle3 = Triangle.from_string("Triangle:5,5,6")
    print_shape_info(rect3)
    print_shape_info(circle3)
    print_shape_info(triangle3)
    
    # from_diameter()
    circle4 = Circle.from_diameter(10)
    print_shape_info(circle4)
    print(f" (Erstellt aus Durchmesser 10)")
    
    # Fabrikmethode
    rect4 = Shape.create_shape("rectangle", 15, 7)
    circle5 = Shape.create_shape("circle", 4.2)
    triangle4 = Shape.create_shape("triangle", 7, 24, 25)
    print_shape_info(rect4)
    print_shape_info(circle5)
    print_shape_info(triangle4)

    # Teil D: Statische Methoden

    print("\n" + "="*60)
    print("TEIL D: Statische Methoden")
    print("="*60)
    
    # is_valid_shape()
    print(f"\nShape.is_valid_shape(rect1): {Shape.is_valid_shape(rect1)}")
    print(f"Shape.is_valid_shape('not a shape'): {Shape.is_valid_shape('not a shape')}")
    
    # Pythagoras
    a, b = 3, 4
    hyp = Shape.calculate_pythagoras(a, b)
    print(f"\nPythagoras: {a}² + {b}² = {hyp}²")
    
    # Dreiecksvalidierung
    valid_triangles = [(3, 4, 5), (1, 1, 2), (2, 3, 6)]
    print(f"\nDreiecksvalidierung:")
    for sides in valid_triangles:
        valid = Shape.is_triangle_valid(*sides)
        print(f" {sides}: {'Gültig' if valid else 'Ungültig'}")
    
    # Pi-Approximation
    print(f"\nPi-Approximation mit Leibniz-Formel:")
    iterations = [10, 100, 1000, 10000]
    for n in iterations:
        approx = Circle.pi_approx(n)
        error = abs(math.pi - approx)
        print(f" n={n:5d}: {approx:.10f} (Fehler: {error:.2e})")
    print(f" exakter Wert: {math.pi:.10f}")
  
    # Zusätzliche Herausforderung: ShapeCollection
   
    print("\n" + "="*60)
    print("ZUSÄTZLICHE HERAUSFORDERUNG: ShapeCollection")
    print("="*60)
    
    # Collection erstellen und füllen
    collection = ShapeCollection([rect1, circle1, triangle1])
    collection.add_shape(rect2)
    collection.add_shape(circle2)
    collection.add_shape(triangle2)
    
    print(f"\nCollection: {collection}")
    print(f"Anzahl Shapes: {len(collection)}")
    print(f"Gesamtfläche: {collection.total_area():.2f}")
    print(f"Durchschnittsfläche: {collection.average_area():.2f}")
    
    # Filtern
    print(f"\nRechtecke in der Collection:")
    for shape in collection.get_shapes_by_type("rectangle"):
        print(f" - {shape.describe()}: Fläche = {shape.area():.2f}")
    
    print(f"\nKreise in der Collection:")
    for shape in collection.get_shapes_by_type("circle"):
        print(f" - {shape.describe()}: Fläche = {shape.area():.2f}")
    
    # Iteration
    print(f"\nIteration über alle Shapes:")
    for i, shape in enumerate(collection, 1):
        print(f" {i}. {shape.describe()} (Fläche: {shape.area():.2f})")
    
    # Shape entfernen
    removed = collection.remove_shape(0)
    print(f"\nEntferntes Shape: {removed.describe()}")
    print(f"Collection jetzt: {collection}")
    
    print("\n" + "="*60)
    print("DEMONSTRATION ABGESCHLOSSEN")
    print("="*60)

# Zusätzliche Test-Hilfsfunktion

def test_duck_typing():
    """
    Testet Duck Typing mit verschiedenen Objekten
    """
    print("\n" + "="*60)
    print("DUCK TYPING TEST")
    print("="*60)
    
    class Duck:
        def area(self): return 10
        def perimeter(self): return 14
        def describe(self): return "I'm a duck!"
    
    class NotAShape:
        def area(self): return 5
        # Fehlt perimeter und describe
    
    # Funktioniert - hat alle Methoden
    duck = Duck()
    print_shape_info(duck)
    
    # Würde fehlschlagen - nicht alle Methoden vorhanden
    not_a_shape = NotAShape()
    print(f"\nIst NotAShape ein gültiges Shape? {Shape.is_valid_shape(not_a_shape)}")
    
    # Aber wir können trotzdem die area() verwenden
    rect = Rectangle(10, 5)
    print(f"Fläche von Rectangle: {rect.area():.2f}")
    print(f"Fläche von NotAShape: {not_a_shape.area():.2f}")

if __name__ == "__main__":
    main()
    # Zum Testen auskommentieren:
    # test_duck_typing()
'''i_approx: Eine Variable (Float), die das Zwischenergebnis speichert pi_approx	Float (Gleitkommazahl)	Zwischenergebnis der Pi-Berechnung

term: Eine Variable (Float), die den aktuellen Reihenterm enthält term	Float (Gleitkommazahl)	Einzelner Term der Reihe (1, 1/3, 1/5, ...)

+=: Ein Operator, der den Wert von term zu pi_approx addiert Zweck: Mathematische Approximation von Pi (Kreiszahl)

Shape ist eine abstrakte Klasse für geometrische Formen

Dictionary ist eine Datenstruktur für Schlüssel-Wert-Paar'''   