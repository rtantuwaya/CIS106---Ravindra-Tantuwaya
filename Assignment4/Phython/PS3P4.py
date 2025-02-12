# 4.	Enter first name and number of steps walked in a day. 
#     For each step you burned .25 calories. 
#     Computer the number of calories burned. 
#     Display first name and calories burned. 

firstName = input("Enter your first name: ")
stepsWalked = int(input("Enter the number of steps you walked day: "))
caloriesBurned = stepsWalked * 0.25
print("First name: " + firstName + ", " + "Calories Burned: " + "%.2f" % (caloriesBurned))