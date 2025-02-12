# 2.Input the purchase price per share, the current stock price and 
# quantity of stock, compute the increase (or decrease) of the value of the stock entered. 
# (value is computed as (current price – price per share) * quantity. 
# If the amount is negative that means you are losing money). 

purchasePricePerShare = float(input("Enter the purchase price per share: "))
currentStockPrice = float(input("Enter the current stock price: "))
quantityOfStock = int(input("Enter the quantity of stock: "))

stockValueChange = (currentStockPrice - purchasePricePerShare) * quantityOfStock

if stockValueChange > 0:
    print("Profit")
else:
    if stockValueChange < 0:
        print("Loss")
    else:
        print("No Change")
