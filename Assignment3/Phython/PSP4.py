# input phase
make  = input("Enter the make of the car ")
model  = input("Enter the model of the car ")
msrp = float(input("Enter the MSRP (price) of the car "))
discountPercent = float(input("Enter the discount percent "))

#process phase
amountOff = msrp * discountPercent / 100
discountPrice = msrp - amountOff

# outpute phase
print("Make: ", make)
print("Model: ", model)
print("MSRP: ", msrp)
print("Discount Percent: ", discountPercent)
print("Amount Off: ", amountOff)
print("Discounted Price: ", discountPrice)
