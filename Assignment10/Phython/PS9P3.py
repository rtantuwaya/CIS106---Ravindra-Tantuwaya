# Function to compute the out-the-door price
def computeOutTheDoorPrice(msrp, make, model, electricVehicleCode):
     if electricVehicleCode == "Y":
         discountPercent = 0.30
     elif make == "Honda" and model == "Accord":
         discountPercent = 0.10
     elif make == "Toyota" and model == "Rav4":
        discountPercent = 0.15
     else:
        discountPercent = 0.05

    # Calculate new MSRP after discount
     discountedPrice = msrp * (1 - discountPercent)

     # Add 7% sales tax
     totalPrice = discountedPrice * 1.07

     return totalPrice, msrp



# Main program loop
userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()
totalMsrpSum = 0
totalSalesPriceSum = 0

while userEntry == "yes":
    # Prompt for car details
     make = input("Enter the make of the car: ").strip()
     model = input("Enter the model of the car: ").strip()
     electricVehicleCode = input("Is it an electric vehicle (Y or N): ").strip().upper()
     msrp = float(input("Enter the MSRP (sticker price) of the car: ").strip())

    # Calculate the out-the-door price 
     totalPrice, originalMsrp    =  computeOutTheDoorPrice(msrp, make, model, electricVehicleCode)
    #  originalMsrp  =  computeOutTheDoorPrice(msrp, make, model, electricVehicleCode)

    # Display the results
     print(f"Out-the-door price for the {make} {model}: ${totalPrice:.2f}")

    # Update total sums
     totalMsrpSum = originalMsrp + totalMsrpSum
     totalSalesPriceSum = totalSalesPriceSum + totalPrice

     userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()
     # Display the total sums when the user exits
print(f"\nTotal MSRP of all cars: ${totalMsrpSum:.2f}")
print(f"Total sales price of all cars: ${totalSalesPriceSum:.2f}")