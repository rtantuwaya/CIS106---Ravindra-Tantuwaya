numberOfTickets = int(input("Enter the number of tickets: "))

if numberOfTickets >= 25:
    pricePerTicket = 50.0
else:
    if numberOfTickets >= 10:
        pricePerTicket = 60.0
    else:
        if numberOfTickets >= 5:
            pricePerTicket = 70.0
        else:
            pricePerTicket = 75.0

totalCost = numberOfTickets * pricePerTicket

print(f"Number of Tickets: {numberOfTickets}")
print(f"Price Per Ticket: ${pricePerTicket:.2f}")
print(f"Total Cost: ${totalCost:.2f}")