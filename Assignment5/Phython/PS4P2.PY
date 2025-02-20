item = input("Enter the item: ")
quantity = int(input("Enter the quantity: "))
if item == "A":
    unitPrice = 10.0
else:
    unitPrice = 20.0
extendedPrice = quantity * unitPrice

print(f"\nItem: {item}")
print(f"Unit Price: ${unitPrice:.2f}")
print(f"Extended Price: ${extendedPrice:.2f}")