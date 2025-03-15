try:
    file = open('employees.txt', 'r')
except FileNotFoundError:
    print("Error: The file 'employees.txt' was not found.")
    exit(1)

totalBonuses = 0

# Read the first line (first employee's last name)
employeeLastName = file.readline().strip()

if not employeeLastName:
    print("Error: The file is empty or improperly formatted.")
    file.close()
    exit(1)

# Loop to read employee data
while employeeLastName != "": # Continue until we reach the end of file
    # Read the next line (employee's salary)
    salaryLine = file.readline().strip()

    #check if salary is a valid number
    try:
        employeeSalary = float(salaryLine)
    except ValueError:
        print(f"Error: Invalid salary value for {employeeLastName}. Salary should be a number.")
        employeeLastName = file.readline().strip() # Skip to next entry
        continue  # Move to the next employee

    # Calculate the bonus based on salary
    if employeeSalary >= 100000:
        bonus = employeeSalary * 0.20
    elif employeeSalary >= 50000:
        bonus = employeeSalary * 0.15
    else:
        bonus = employeeSalary * 0.10



   # Display employee information and bonus
    print(f"Employee: {employeeLastName}")
    print(f"Salary: {employeeSalary}")
    print(f"Bonus: {bonus}\n")

    totalBonuses =  totalBonuses + bonus


    # Add the bonus to the total bonuses paid

    #Read the next employee's last name (if any)
    employeeLastName = file.readline().strip()

# Close the file after processing
file.close()

# After the loop, display the total bonuses paid out
print(f"Total Bonuses Paid Out: {totalBonuses}")