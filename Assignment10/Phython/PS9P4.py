def computeTicketPrice(miles):
     if miles >= 30:
          ticketPrice = 12
     elif 20 <= miles <= 29:
      ticketPrice = 10
     elif 10 <= miles <= 19:
        ticketPrice = 8
     else:
        ticketPrice = 5
     return ticketPrice


# Main program loop
userEntry = input("Would you like to calculate a ticket price? (Yes/No): ").strip().lower()

totalTicketPrice = 0

while userEntry == "yes":

     lastName = input("Enter the last name: ").strip()
     miles = int(input("Enter the miles from downtown Chicago: ").strip())

    #  Calculate the ticket price
     ticketPrice = computeTicketPrice(miles)
     
     print(f"The ticket price for {lastName} is ${ticketPrice}.")

     totalTicketPrice += ticketPrice
     
     userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()
     
print(f"\nTotal price of all tickets: ${totalTicketPrice}.")