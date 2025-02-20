lastName = input("Enter your last name: ")
numDependents = int(input("Enter the number of dependents: "))
grossIncome = float(input("Enter your gross income: $"))
adjustedGrossIncome = grossIncome - numDependents * 12000

if adjustedGrossIncome > 50000:
    taxRate = 0.2
else:
    taxRate = 0.1
incomeTax = adjustedGrossIncome * taxRate
if incomeTax < 0:
    incomeTax = 100

print(f"\nLast Name: {lastName}")
print(f"Gross Income: ${grossIncome:.2f}")
print(f"Number of Dependents: {numDependents}")
print(f"Adjusted Gross Income: ${adjustedGrossIncome:.2f}")
print(f"Income Tax: ${incomeTax:.2f}")  