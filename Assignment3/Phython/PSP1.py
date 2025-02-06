# input phase
stockTicker = input("Enter the stock ticker symbol")
numberOfShare = int(input("Enter the number of shares"))
costPerShare = float(input("Enter the cost per share"))

#process phase
amountInvested = numberOfShare * costPerShare

# outpute phase
print("Stock Ticker:  ", stockTicker)
print("Number of Shares:", numberOfShare)
print("Cost per Share:", costPerShare)
print("Amount Invested:", amountInvested)