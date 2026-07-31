# Lösung Übung 1: Mitarbeiter-Verwaltungssystem
'''Employee (Oberklasse)
    ├── Attribute:
    │   ├── employee_id  → Identifikationsnummer
    │   ├── name         → Vollständiger Name
    │   └── base_salary  → Jahresgehalt in €
    │
    └── Methode:
        └── get_role()   → Gibt die Rolle zurück

Manager (Unterklasse von Employee)
    ├── Zusätzliches Attribut:
    │   └── bonus        → Jährlicher Bonus in €
    │
    └── Überschriebene Methode:
        └── get_role()   → Gibt "Manager" zurück
        BasesalaryJahresgehaltDeveloperSoftwareentwicklerinternPRaktikant
        '''
class Employee:
    def __init__(self, employee_id, name, base_salary):
        self.employee_id = employee_id
        self.name = name
        self.base_salary = base_salary
    
    def calculate_monthly_salary(self):
        """Berechnet das monatliche Gehalt"""
        return self.base_salary / 12
    
    def get_role(self):
        """Gibt die Rolle des Mitarbeiters zurück"""
        return "Generic Employee"
    
    def __str__(self):
        return f"{self.name} (ID: {self.employee_id})"

class Manager(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name, base_salary)
        self.bonus = bonus
    
    def calculate_monthly_salary(self):
        """Berechnet monatliches Gehalt inklusive Bonus"""
        annual_salary_with_bonus = self.base_salary + self.bonus
        return annual_salary_with_bonus / 12
    
    def get_role(self):
        return "Manager"

class Developer(Employee):
    def __init__(self, employee_id, name, base_salary, overtime_hours, hourly_rate):
        super().__init__(employee_id, name, base_salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate
    
    def calculate_monthly_salary(self):
        """Berechnet monatliches Gehalt inklusive Überstunden"""
        total_annual = self.base_salary + (self.overtime_hours * self.hourly_rate)
        return total_annual / 12
    
    def get_role(self):  # gibt die Postion des Mitarbeiters zurück,
        return "Developer"

class Intern(Employee):
    def __init__(self, employee_id, name, base_salary, mentor_name):
        super().__init__(employee_id, name, base_salary)
        self.mentor_name = mentor_name
    
    def get_role(self):
        return "Intern"
    
    def get_mentor(self):
        return self.mentor_name

def main():
    # Mitarbeiter erstellen
    manager = Manager(101, "Anna Schmidt", 75000, 5000)
    developer = Developer(102, "Max Mustermann", 65000, 120, 35)
    intern = Intern(103, "Lisa Chen", 30000, "Anna Schmidt")
    
    # Informationen ausgeben
    employees = [manager, developer, intern]
    for emp in employees:
        print(f"\n{'='*40}")
        print(f"Mitarbeiter: {emp}")  # __str__() wird vererbt
        print(f"Rolle: {emp.get_role()}")
        print(f"Monatliches Gehalt: {emp.calculate_monthly_salary():.2f} €")
        
        # Typspezifische Informationen
        if isinstance(emp, Manager):
            print(f"Bonus: {emp.bonus:.2f} €")
        elif isinstance(emp, Developer):
            print(f"Überstunden: {emp.overtime_hours} Stunden")
            print(f"Stundensatz: {emp.hourly_rate:.2f} €")
        elif isinstance(emp, Intern):
            print(f"Mentor: {emp.get_mentor()}")
    
    # Polymorphie demonstrieren
    print(f"\n{'='*40}")
    print("Polymorphie-Demonstration:")
    for emp in employees:
        print(f"{emp.name} verdient {emp.calculate_monthly_salary():.2f} €/Monat")

if __name__ == "__main__":
    main()
    
# Lösung Übung 1: Mitarbeiter-Verwaltungssystem
class Employee:
    def __init__(self, employee_id, name, base_salary):
        self.employee_id = employee_id
        self.name = name
        self.base_salary = base_salary
    
    def calculate_monthly_salary(self):
        """Berechnet das monatliche Gehalt"""
        return self.base_salary / 12
    
    def get_role(self):
        """Gibt die Rolle des Mitarbeiters zurück"""
        return "Generic Employee"
    
    def __str__(self):
        return f"{self.name} (ID: {self.employee_id})"

class Manager(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name, base_salary)
        self.bonus = bonus
    
    def calculate_monthly_salary(self):
        """Berechnet monatliches Gehalt inklusive Bonus"""
        annual_salary_with_bonus = self.base_salary + self.bonus
        return annual_salary_with_bonus / 12
    
    def get_role(self):
        return "Manager"

class Developer(Employee):
    def __init__(self, employee_id, name, base_salary, overtime_hours, hourly_rate):
        super().__init__(employee_id, name, base_salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate
    
    def calculate_monthly_salary(self):
        """Berechnet monatliches Gehalt inklusive Überstunden"""
        total_annual = self.base_salary + (self.overtime_hours * self.hourly_rate)
        return total_annual / 12
    
    def get_role(self):
        return "Developer"

class Intern(Employee):
    def __init__(self, employee_id, name, base_salary, mentor_name):
        super().__init__(employee_id, name, base_salary)
        self.mentor_name = mentor_name
    
    def get_role(self):
        return "Intern"
    
    def get_mentor(self):
        return self.mentor_name

def main():
    # Mitarbeiter erstellen
    manager = Manager(101, "Anna Schmidt", 75000, 5000)
    developer = Developer(102, "Max Mustermann", 65000, 120, 35)
    intern = Intern(103, "Lisa Chen", 30000, "Anna Schmidt")
    
    # Informationen ausgeben
    employees = [manager, developer, intern]
    for emp in employees:
        print(f"\n{'='*40}")
        print(f"Mitarbeiter: {emp}")  # __str__() wird vererbt
        print(f"Rolle: {emp.get_role()}")
        print(f"Monatliches Gehalt: {emp.calculate_monthly_salary():.2f} €")
        
        # Typspezifische Informationen
        if isinstance(emp, Manager):
            print(f"Bonus: {emp.bonus:.2f} €")
        elif isinstance(emp, Developer):
            print(f"Überstunden: {emp.overtime_hours} Stunden")
            print(f"Stundensatz: {emp.hourly_rate:.2f} €")
        elif isinstance(emp, Intern):
            print(f"Mentor: {emp.get_mentor()}")
    
    # Polymorphie demonstrieren
    print(f"\n{'='*40}")
    print("Polymorphie-Demonstration:")
    for emp in employees:
        print(f"{emp.name} verdient {emp.calculate_monthly_salary():.2f} €/Monat")

if __name__ == "__main__":
    main()
    
    
    