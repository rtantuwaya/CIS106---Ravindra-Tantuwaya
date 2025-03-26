# Function to compute the square footage of the room
def calculateSquareFootage(length, width, height):
  # Calculate the square footage (floor, ceiling, and 4 walls)
    square_footage = 2 * length * width + 2 * length * height + 2 * width * height
    return square_footage

# Main program loop

userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()

while userEntry == "yes":
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))

     # Calculate the square footage of the room
    squareFootage = calculateSquareFootage(length, width, height)
    
    # Calculate the number of gallons of paint needed (1 gallon covers 50 square feet)
    gallonsNeeded = squareFootage / 50

    # Display the result
    print(f"The square footage of the room is {squareFootage:.2f} square feet.")
    print(f"You will need {gallonsNeeded:.2f} gallons of paint.")

    userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()