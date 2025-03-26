def computeForecast(month, sales):
    nextMonthSales = 0
    # Determine the forecast percent based on the month
    if month in ['Jan', 'Feb', 'Mar']:
         forecastPercent = 0.10
    elif month in ['Apr', 'May', 'Jun']:
        forecastPercent = 0.15
    elif month in ['Jul', 'Aug', 'Sep']:
        forecastPercent = 0.20
    elif month in ['Oct', 'Nov', 'Dec']:
        forecastPercent = 0.25
    else:
        return None  # Invalid month input
    
    # Calculate next month's sales
    nextMonthSales = sales * (1 + forecastPercent)
    return nextMonthSales

userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower() 
while userEntry == "yes":
        
    # Collect user input
    lastName = input("Enter last name: ")
    month = input("Enter the month (e.g., Jan, Feb, Mar): ").strip().capitalize()
    sales = float(input("Enter sales amount: "))
        
        # Compute the forecast for next month
    nextMonthSales = computeForecast(month, sales)
        
        # Check if month input is valid
    if nextMonthSales is None:
        print(f"Invalid month input: {month}. Please enter a valid month (e.g., Jan, Feb, Mar, etc.).")
    else:
            # Display next month's forecast sales
            print(f"Next month's forecast for {lastName} ({month}): {nextMonthSales:.2f}")
    
    userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()

