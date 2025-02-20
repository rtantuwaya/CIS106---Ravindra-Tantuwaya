quantity = int(input("Enter the quantity of the item: "))
tax = 0.07
if quantity >= 1000:
    unitPrice = 3.0
else:
    unitPrice = 5.0
extendedPrice = quantity * unitPrice
extendedPriceTax = extendedPrice * tax
total = extendedPrice + extendedPriceTax

print(f"\nQuantity: {quantity}")
print(f"Unit Price: ${unitPrice:.2f}")
print(f"Extended Price: ${extendedPrice:.2f}")
print(f"Tax: ${extendedPriceTax:.2f}")
print(f"Total: ${total:.2f}")
