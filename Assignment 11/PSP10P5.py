# Global variables for total and tax
total = 0
tax = 0

def calculateTotalAndTax(quantity, unitPrice):
    global total, tax
    # Calculate the total cost
    total = quantity * unitPrice
    # Calculate the tax (7% of total)
    tax = total * 0.07

def main():
    # Input values
    quantity = int(input("Enter the quantity of the item: "))
    unitPrice = float(input("Enter the unit price of the item: "))
    
    # Call the function to compute total and tax
    calculateTotalAndTax(quantity, unitPrice)
    
    # Display the results
    print(f"\n--- Receipt ---")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: ${unitPrice:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Grand Total: ${total + tax:.2f}")

# Run the main function
if __name__ == "__main__":
    main()
