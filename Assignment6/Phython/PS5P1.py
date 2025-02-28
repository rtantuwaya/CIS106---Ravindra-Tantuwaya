quantity = int(input("Enter the quantity of widgets: "))
tax = 0.07

if quantity > 10000:
    price = 10.0
else:
    if quantity >= 5000:
        price = 20.0
    else:
        price = 30.0

extendedPrice = quantity * price
taxAmount = extendedPrice * tax
total = extendedPrice + taxAmount

print(f"Extended Price: ${extendedPrice:.2f}")
print(f"Tax Amount: ${taxAmount:.2f}")
print(f"Total: ${total:.2f}")