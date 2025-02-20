
numBook = int(input("Enter the number of books to order: "))
costPerBook = float(input("Enter the cost per book: $"))

orderTotalAmount = numBook * costPerBook

if orderTotalAmount > 50.0:
    shippingCharge = 0.0
else:
    shippingCharge = 25.0

print(f"\nOrder Total: ${orderTotalAmount:.2f}")
print(f"Shipping Charge: ${shippingCharge:.2f}") 