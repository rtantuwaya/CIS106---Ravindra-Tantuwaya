# 5.You are setting up a business and need to compute the break even point. 
# This indicates how many items you must sell at a given price to cover your overhead. 
# Enter fixed costs, price per unit and cost per unit into your program. 
# Compute the break even point by dividing fixed costs by the difference of price per unit and 
# cost per unit. 

fixedCosts = float(input("Enter the fixed costs: "))

pricePerUnit = float(input("Enter the price per unit: "))
costPerUnit = float(input("Enter the cost per unit: "))

breakEvenPoint = fixedCosts / (pricePerUnit - costPerUnit)

print("Break-even point: ", float(breakEvenPoint))
