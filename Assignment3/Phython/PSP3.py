# input phase
totalAmount = float(input("Enter the total amount received for the job: $"))
numberOfPerson  = int(input("Enter the number of person work"))

#process phase
amountPerPerson = totalAmount/numberOfPerson

# outpute phase
print("Each person will receive: ", amountPerPerson)
