def commissionFunction(sales):

    if sales > 100000:
     commission = sales * 10/100 
    else :
       commission = sales * 5/100

    nextYearsales = sales * 5/100
    yearTarget = sales + nextYearsales

    return commission, yearTarget



name = input("Salesperson  last name  ")
sales = float(input("Sales  "))

commission, yearTarget =  commissionFunction(sales)

print(f"Salesperson : {name}")
print(f"commission: ${commission:.2f}")
print(f"Next year’s target.: ${yearTarget:.2f}")


