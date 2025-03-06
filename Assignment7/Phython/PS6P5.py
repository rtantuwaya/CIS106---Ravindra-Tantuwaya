# Initialize variables
sumOfDiscontAmount = 0

# Ask if the user wants to continue
continueProgram = input("Do you want to continue? (Yes/No): ")

# While loop to process orders
while continueProgram == "Yes":
    # Get quantity and priitemPricece of item
    quantity = int(input("Enter quantity of the item: "))
    itemPrice = float(input("Enter itemPrice of the item: "))

    # Calculate extended itemPrice
    extendedPrice = quantity * itemPrice

    # Apply discount based on extended itemPrice
    if extendedPrice > 10000.00:
        discountPercent = 0.25  # 25% discount
    else:
        discountPercent = 0.10  # 10% discount

    # Calculate discount amount
    discountAmount = extendedPrice * discountPercent

    # Calculate total itemPrice after discount
    totalPrice = extendedPrice - discountAmount

    # Display the details of the order
    print(f"Extended itemPrice: ${extendedPrice:.2f}")
    print(f"Discount Amount: ${discountAmount:.2f}")
    print(f"Total itemPrice after Discount: ${totalPrice:.2f}")

    # Sum the discount amount
    sumOfDiscontAmount += discountAmount

    # Ask if the user wants to continue
    continueProgram = input("Do you want to continue? (Yes/No): ")

# After the loop ends, display the total discount
print(f"\nTotal Discount Given: ${sumOfDiscontAmount:.2f}")
