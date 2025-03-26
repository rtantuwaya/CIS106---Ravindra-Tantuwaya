# Function to compute the assessed value based on county and market value
def  computeAssessedValue(county, marketValue):
     countyAssessedValuePercent = {'Cook': 0.90, 'DuPage': 0.80, 'McHenry': 0.75,'Kane': 0.60 }

     # If the county is not in the predefined list, use 0.70 as the default for all others
     assessedValuePercent = countyAssessedValuePercent.get(county, 0.70)
    
    # Calculate the assessed value
     assessedValue = marketValue * assessedValuePercent
     return assessedValue
    
    # Define the assessed value percent based on the county
     

# Main program loop
userEntry = input("Would you like to calculate the assessed value for a home? (Yes/No): ").strip().lower()

totalMarketValue = 0
totalAssessedValue = 0

while userEntry == "yes":
      county = input("Enter the county: ").strip()
      marketValue = float(input("Enter the market value of the home: ").strip())

    # Compute the assessed value
      assessedValue = computeAssessedValue(county, marketValue)
      print(f"The assessed value for the home in {county} with a market value of ${marketValue} is ${assessedValue:.2f}")

    # Update total sums
      totalMarketValue += marketValue
      totalAssessedValue += assessedValue

      userEntry = input("Would you like to calculate the assessed value for a home? (Yes/No): ").strip().lower()
    # Display the total sum of market values and assessed values
print(f"\nTotal market value of all homes: ${totalMarketValue:.2f}")
print(f"Total assessed value of all homes: ${totalAssessedValue:.2f}")


        