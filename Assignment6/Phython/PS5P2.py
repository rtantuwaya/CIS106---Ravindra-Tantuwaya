partNumber = input("Enter part number: ")
quantity = int(input("Enter quantity: "))

if partNumber == "10" or partNumber == "55":
    unitCost = 1.0
else:
    if partNumber == "99":
        unitCost = 2.0
    else:
        if partNumber == "80" or partNumber == "70":
            unitCost = 3.0
        else:
            unitCost = 5.0

totalCost = quantity * unitCost

print(f"Part Number: {partNumber}")
print(f"Cost Per Unit: ${unitCost:.2f}")
print(f"Total Cost: ${totalCost:.2f}")