principleAmount = float(input("Enter principal amount: "))
interestRate = float(input("Enter interest rate: "))

endBalance = principleAmount
earnInterestTotal = 0

print(f"\n{'Year':<5} {'Beginning Balance':<20} {'Ending Balance':<20}")
for numYear in range(1, 5 + 1, 1):
    beginBalance = endBalance
    interestEarned = beginBalance * 0.1
    endBalance = beginBalance + interestEarned
    print(f"{numYear:<5} ${beginBalance:,.2f} {'         '} ${endBalance:,.2f}")

    earnInterestTotal = earnInterestTotal + interestEarned

print(f"\nTotal interest earned: ${earnInterestTotal:,.2f}")