numberOfemployees = 0
sumGrossPays = 0
assignHours = 40
overTimeHours = 0
overTimePayRate = 0

continueProgram = input("Do you want to continue? (Yes/No): ")

while continueProgram == "Yes":
    employeeLastName = input("Enter employee's last name: ")
    hoursWorked = float(input("Enter hours worked: "))
    payRate = float(input("Enter hourly rate of pay: "))

    if hoursWorked <= assignHours:
        regularHours = hoursWorked
        regularPay = regularHours * payRate
        grossPay = regularPay
    else:
        if hoursWorked > 40:
            overTimePayRate = payRate + payRate / 2
            overTimeHours = hoursWorked - assignHours
            overTimePayRate = payRate + payRate / 2
            overTimePay = overTimeHours * overTimePayRate
        regularPay = assignHours * payRate
        grossPay = regularPay + overTimePay

    print(f"Employee Last Name: {employeeLastName}")
    print(f"Gross Pay: ${grossPay:.2f}")

    numberOfemployees = numberOfemployees + 1
    sumGrossPays = sumGrossPays + grossPay
    continueProgram = input("Do you want to continue? (Yes/No): ")

    averagePay = sumGrossPays / numberOfemployees
    print(f"Total Number of Employees: {numberOfemployees}")
    print(f"Total Gross Pay for all Employees: ${sumGrossPays:.2f}")
    print(f"Average Gross Pay: ${averagePay:.2f}")

   