applianceName = input("Enter the name of the appliance: ")
applianceCost = float(input("Enter the cost of the appliance: $"))

if applianceCost > 1000:
    warrantyCost = applianceCost * 0.1
else:
    warrantyCost = applianceCost * 0.05
totalCost = applianceCost + warrantyCost

print(f"\nAppliance: {applianceName}")
print(f"Cost of Appliance: ${applianceCost:.2f}")
print(f"Warranty Cost: ${warrantyCost:.2f}")
print(f"Total Cost (Appliance + Warranty): ${totalCost:.2f}")