import math
from typing import List, Optional

class Vehicle:
    def __init__(self, marke:str, model: str, jahr: int, kilometerStand:float =0):
        self.marke = marke
        self.model = model
        self.jahr = jahr
        self.kilometerStand = kilometerStand
    
    def calculate_range(self):
        """Berechnet die maximale Reichweite in Kilometern"""
        raise NotImplementedError("Subclasses must implement calculate_range()")
    
    def service_interval(self):
        """Gibt den Wartungsintervall in Monaten zurück"""
        return 12 # Standard: jährliche Wartung
    
    def is_electric(self):
        """Gibt zurück, ob das Fahrzeug elektrisch ist"""
        return False
    
    def __repr__(self):  #erstellt eine offizielle, eindeutige und möglichst exakte String-Darstellung eines Objekts
        return f"{self.jahr} {self.marke} {self.model}"
    
class Car(Vehicle):
        
    def __init__(self, marke: str, model: str, jahr: int,fuel_efficiency: float, fuel_capacity: float, kilometerStand: float = 0):
        super().__init__(marke, model, jahr, kilometerStand)
        self.fuel_efficiency = fuel_efficiency # Liter pro 100 Km
        self.fuel_capacity = fuel_capacity     # Liter
        
    def calculate_range(self):
        return (self.fuel_capacity / self.fuel_efficiency) * 100
            
        
    def service_Interval(self):    # was holen int 
        return 12
                
class ElectricCar(Vehicle):
       
    def __init__(self, marke:str, model:str, jahr:int, battery_capacity:float, efficiency:float, kilometerStand=0):
        super().__init__( marke, model, jahr, kilometerStand)
    
        self.battery_capacity = battery_capacity #kWH
        self.efficiency = efficiency             #Kwh pro 100
        
    def calculate_range(self):
        return (self.battery_capacity / self.efficiency) *100
        
     
    def is_electric(self):
        return True
     
    def service_interval(self):
        return super().service_interval()
       
class Motorcycle(Vehicle):
    def __init__(self, marke, model, jahr, fuel_efficiency, fuel_capacity, kilometerStand=0):
        super().__init__(marke, model, jahr, kilometerStand)
        self.fuel_efficiency = fuel_efficiency
        self.fuel_capacity = fuel_capacity

    def calculate_range(self):
        return (self.fuel_capacity / self.fuel_efficiency) * 100

    def service_interval(self):
        return 6


class FleetManager:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def get_total_range(self):
        return sum(v.calculate_range() for v in self.vehicles)

    def get_vehicles_needing_service(self, months_elapsed):
        return [v for v in self.vehicles if months_elapsed >= v.service_interval()]

    def get_electric_vehicles(self):
        return [v for v in self.vehicles if v.is_electric()]


def main():
    fleet = [
        Car("VW", "Golf", 2020, fuel_efficiency=6.5, fuel_capacity=50),
        Car("Toyota", "Corolla", 2021, fuel_efficiency=5.8, fuel_capacity=45),
        ElectricCar("Tesla", "Model 3", 2022, battery_capacity=60, efficiency=15),
        ElectricCar("VW", "ID.3", 2023, battery_capacity=58, efficiency=16),
        Motorcycle("Honda", "CB500", 2019, fuel_efficiency=4.0, fuel_capacity=17),
    ]

    manager = FleetManager(fleet)

    print(f"Gesamtreichweite der Flotte: {manager.get_total_range():.1f} km\n")

    print("Fahrzeuge mit Wartungsbedarf nach 14 Monaten:")
    for v in manager.get_vehicles_needing_service(14):
        print(f"  {v}")

    print("\nElektrofahrzeuge:")
    for v in manager.get_electric_vehicles():
        print(f"  {v}")

    print("\nAlle Fahrzeuge:")
    for v in fleet:
        print(f"  {v.marke} {v.model} | Reichweite: {v.calculate_range():.1f} km | "
              f"Wartungsintervall: {v.service_interval()} Monate")


if __name__ == "__main__":
    main()            
            
                            