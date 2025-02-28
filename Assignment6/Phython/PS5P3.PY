principleAmount = float(input("Enter the principal amount: "))
yearsToMaturity = int(input("Enter the years to maturity: "))

if principleAmount > 100000 and yearsToMaturity >= 5:
    interestRate = 0.06
else:
    if principleAmount >= 50000 and yearsToMaturity >= 10:
        interestRate = 0.05
    else:
        if principleAmount >= 50000 and yearsToMaturity >= 5:
            interestRate = 0.04
        else:
            interestRate = 0.02

firstYearInterest = principleAmount * interestRate

print(f"Principal Amount: ${principleAmount:.2f}")
print(f"Interest Rate: {interestRate * 100:.2f}%")
print(f"Interest amount for the first year: ${firstYearInterest:.2f}")