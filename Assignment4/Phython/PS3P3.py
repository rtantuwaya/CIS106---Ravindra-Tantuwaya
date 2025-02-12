# 3.	Enter the total for a meal. Compute a tip at 15%, 18% and 20%.
#  Display total, each tip value and total with each tip value. 
# Your output should have total for the meal as entered, tip and 
# total with tip for each tip value. (9 lines). 
# Put a blank line between each tip of the set of tip values. 

totalMeal = float(input("Enter the total for the meal: "))
tipPersentage15 = 0.15
tipPersentage18 = 0.18
tipPersentage20 = 0.20

tipValue15 = totalMeal * tipPersentage15
tipValue18 = totalMeal * tipPersentage18
tipValue20 = totalMeal * tipPersentage20

totalWithTip15 = totalMeal + tipValue15
totalWithTip18 = totalMeal + tipValue18
totalWithTip20 = totalMeal + tipValue20

print("With 15% Tip:")
print("         Total:  %.2f" % (totalMeal))
print("           Tip:  %.2f" %(tipValue15))
print("Total with Tip:  %.2f" %(totalWithTip15))

print("With 18% Tip:")
print("         Total:  %.2f" %(totalMeal))
print("           Tip:  %.2f" %(tipValue18))
print("Total with Tip:  %.2f" %(totalWithTip18))

print("With 20% Tip:")
print("         Total:  %.2f" %(totalMeal))
print("           Tip:  %.2f" %(tipValue20))
print("Total with Tip:  %.2f" %(totalWithTip20))
