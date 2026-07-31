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
    class Developer:
        def __init__(self  ):
            pass
        def calculate_month_salary(self):
            pass    
                 