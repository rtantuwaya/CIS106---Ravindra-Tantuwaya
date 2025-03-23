def computeMilesPerGallon(milesTravelled, gallonsGas):
    if gallonsGas != 0:
        milesPerGallon = gallonsGas / milesTravelled
    else:
        milesPerGallon = 0
    
    return milesPerGallon

# Main
numberOfDestination = 0
userEntry = input("Enter trip information (Ctrl+Z or Ctrl+D to stop)")
while userEntry == "Yes":
    destinationCity = input("Enter destination city: ")
    milesTravelled = float(input("Enter miles traveled: "))
    gallonsGas = float(input("Enter gallons used: "))
    milesPerGallon = computeMilesPerGallon(milesTravelled, gallonsGas)
    print(f"Miles Per Gallon: {milesPerGallon} ")
    numberOfDestination = numberOfDestination + 1
   
    userEntry = input()
    print(f"Number Of Destination: {numberOfDestination} ")
