
#define the object
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
   
    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b
    
    def longTermBonus(self, longTerm):
        m = float(longTerm) * float(self.pay)
        return m
    
class Manager(Employee):
    def longTermBonus(self, longTerm):
        m = float(longTerm) * float(self.pay)
        return m
   
empl1 = Employee('Frank', 'Alvino', 60000.00)
mgr1  = Manager ('Mike','Jorden', 80000.00  )
   
rateInput = float(input("Enter the bonus of rate  "))
bonusInput = rateInput/100
print("Email:",empl1.email)
print("First Name:", empl1.first)
print("Last Name:",empl1.last)
print("Pay:", empl1.pay)
print("Bonus (10%):", empl1.bonus(0.10))
print("Bonus (20%):",empl1.bonus(0.20))
print("Bonus (User Input):", empl1.bonus(bonusInput))

print("Email:", mgr1.email)
print("First Name:", mgr1.first)
print("Last Name:", mgr1.last)
print("Pay:", mgr1.pay)
print("Long Term Bonus (40%):", mgr1.longTermBonus(0.40))

