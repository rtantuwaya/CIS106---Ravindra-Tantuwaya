employeeLastName = input("Enter the employee's last name: ")
jobLevel = int(input("Enter the job level: "))
employeeSalary = float(input("Enter the employee's salary: "))

if jobLevel >= 10:
    bonusRate = 0.25
else:
    if jobLevel >= 5:
        bonusRate = 0.2
    else:
        bonusRate = 0.1

bonus = employeeSalary * bonusRate

print(f"Employee Last Name: {employeeLastName}")
print(f"Bonus: ${bonus:.2f}")