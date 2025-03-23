#function
def compExtPrice(qty, unitprice):
    extendedPrice = qty * unitprice
    if extendedPrice > 100000.00:
        discamt = extendedPrice * 0.10
    else: 
        discamt = 0
    newExtPrice = extendedPrice - discamt
    return newExtPrice

 #Main

totalExtPrice = 0
  
userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()
while userEntry == "yes":
    try:
        print("Enter a quantity:")
        quantity = int(input())
        print("Enter the Price:")
        price = float(input())
        extprice = compExtPrice(quantity, price)

        print(f"quantitye: {quantity}")
        print(f"Price: {price}")
        print(f"Extended Price: {extprice}")

        totalExtPrice = totalExtPrice + extprice

        print(f"Total Extended Price: {totalExtPrice}")

    except ValueError:
        # Handle invalid input (e.g., if the user enters a string instead of a number)
        print("Invalid input! Please enter numeric values for quantity and price.")
    print("Do you want to do this program (Yes or No)")
    userEntry = input().strip().lower()
print(f"Total Extended Price: {totalExtPrice}")
print("Thank you for using the program. Goodbye!")