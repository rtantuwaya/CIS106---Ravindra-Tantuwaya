
def comptotal(qty, price, rate): 
    discontprice = price - (price * (rate/100))
    disconAmount = ((qty * price) * (rate/100))
  
    return discontprice, disconAmount

    

qty = int(input("Enter quanitity  "))
price = float(input("Enter price  "))
rate = float(input("Enter rate  "))
discontprice, disconAmount = comptotal(qty, price, rate)

print(f"Price: ${qty:.2f}")
print(f"Total: ${price:.2f}")
print(f"Total: ${rate:.2f}")
print(f"Price: ${discontprice:.2f}")
print(f"Total: ${disconAmount:.2f}")



