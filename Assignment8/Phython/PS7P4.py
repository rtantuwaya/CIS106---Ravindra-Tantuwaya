extendedPrice = 0
totalExtendedPrice = 0
orderCount = 0
averageOrder = 0

# Define the file name


infile = open('orders.txt', 'r')
nextLine = infile.readline()

while nextLine != "":
    item = nextLine.strip() 
    nextLine = infile.readline()
    quantity = int(nextLine)
    nextLine = infile.readline()
    price = float(nextLine)
    nextLine = infile.readline()

    extendedPrice = quantity * price

    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")
    print(f"Extended Price: {extendedPrice}")
    print("\n") 

    totalExtendedPrice = totalExtendedPrice + extendedPrice
    orderCount = orderCount + 1
infile.close()

averageOrder =  totalExtendedPrice / orderCount

print(f"Total Extended Price: {totalExtendedPrice}")
print(f"Total Extended Price: {orderCount}")
print(f"Total Extended Price: {averageOrder}")






