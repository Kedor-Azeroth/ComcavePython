
#Lösung Übung 3: Temperatur-Sensor-Netzwerk
import random
class Temperatursensor:
    def __init__(self, standort, aktuelle_temperatur=20.0,min_temperatur=20.0, max_temperatur=20.0):
        self.standort = standort
        self.aktuelle_temperatur = aktuelle_temperatur
        self.min_temperatur = min_temperatur
        self.max_temperatur = max_temperatur
        self.anzahl_messungen = 1
    def messen(self):
        neue_temp = random.uniform(-10.0, 40.0)
        self.aktuelle_temperatur = neue_temp
        self.anzahl_messungen += 1
        if neue_temp < self.min_temperatur:
            self.min_temperatur = neue_temp
        if neue_temp > self.max_temperatur:
            self.max_temperatur = neue_temp
        print(f"{self.standort}: Messung {self.anzahl_messungen} -{neue_temp:.2f}°C")
    def temperatur_anzeigen(self):
        print(f"Standort: {self.standort}")
        print(f" Aktuell: {self.aktuelle_temperatur:.2f}°C")
        print(f" Minimum: {self.min_temperatur:.2f}°C")
        print(f" Maximum: {self.max_temperatur:.2f}°C")
        print(f" Anzahl Messungen: {self.anzahl_messungen}")
    def reset(self):
        self.aktuelle_temperatur = 20.0
        self.min_temperatur = 20.0
        self.max_temperatur = 20.0
        self.anzahl_messungen = 1
        print(f"{self.standort}: Sensor wurde zurückgesetzt.")
# Testcode
sensor1 = Temperatursensor("Wohnzimmer")
sensor2 = Temperatursensor("Küche", 22.5, 22.5, 22.5)
sensor3 = Temperatursensor("Garten", 15.0, 10.0, 20.0)
# Sensoren initial anzeigen
print("=== Initiale Sensorwerte ===")
sensor1.temperatur_anzeigen()
sensor2.temperatur_anzeigen()
sensor3.temperatur_anzeigen()
print()

# Messungen durchführen
print("=== Messungen durchführen ===")
for i in range(10):
    print(f"\n--- Messrunde {i+1} ---")
    sensor1.messen()
    sensor2.messen()
    sensor3.messen()
    
# Zusammenfassung
print("\n=== Zusammenfassung aller Sensoren ===")
sensor1.temperatur_anzeigen()
print()
sensor2.temperatur_anzeigen()
print()
sensor3.temperatur_anzeigen()

# Auswertung
print("\n=== Auswertung ===")
sensoren = [sensor1, sensor2, sensor3]

# Sensor mit höchster Maximaltemperatur
max_temp_sensor = max(sensoren, key=lambda s: s.max_temperatur)
print(f"Höchste Maximaltemperatur: {max_temp_sensor.max_temperatur:.2f}°C bei{max_temp_sensor.standort}")

# Sensor mit niedrigster Minimaltemperatur
min_temp_sensor = min(sensoren, key=lambda s: s.min_temperatur)
print(f"Niedrigste Minimaltemperatur: {min_temp_sensor.min_temperatur:.2f}°C bei {min_temp_sensor.standort}")

# Reset testen
print("\n=== Reset testen ===")
sensor1.reset()
sensor1.temperatur_anzeigen()

     