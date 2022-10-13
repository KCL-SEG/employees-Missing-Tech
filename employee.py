"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly_salary=0, hourly_rate=0, hours=0, contract_rate=0, contracts_done=0, bonus=0):
        self.name = name
        self.monthly_salary = monthly_salary
        self.hourly_rate = hourly_rate
        self.hours = hours
        self.contract_rate = contract_rate
        self.contracts_done = contracts_done
        self.bonus = bonus

    def calculate_pay(self, arg):
        pay = self.monthly_salary
        if self.hourly_rate != 0:
            pay += self.hourly_rate * self.hours
        if self.contract_rate != 0:
            pay += self.contract_rate * self.contracts_done
        if self.bonus != 0:
            pay += self.bonus
        return pay

    def get_pay(self):
        return self.calculate_pay(self)

    def __str__(self):
        string = f"{self.name} works on a "
        if self.monthly_salary != 0:
            string += f"monthly salary of {self.monthly_salary}"
        if self.hourly_rate != 0:
            string += f"contract of {self.hours} hours at {self.hourly_rate}/hour"
        if self.contract_rate != 0:
            string += f" and receives a commission for {self.contracts_done} contract(s) at {self.contract_rate}/contract"
        if self.bonus != 0:
            string += f" and receives a bonus commission of {self.bonus}"

        string += f". Their total pay is {self.calculate_pay(self)}."
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthly_salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hourly_rate=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthly_salary=3000, contract_rate=200, contracts_done=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, hourly_rate=25, contract_rate=220, contracts_done=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthly_salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourly_rate=30, bonus=600)
