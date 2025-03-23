def computeGrossPay(hoursWorked, payRate):
    overTimePay = 0
    if hoursWorked <= 40:
        regularPay = hoursWorked * payRate
    else:
        regularPay = 40 * payRate
        overTimePay = (hoursWorked - 40) * (payRate * 1.5)
    grossPay = regularPay + overTimePay
    
    return grossPay

def determinePayRate(jobCode):
    if jobCode == "L":
        hourRate = 25
    else:
        if jobCode == "A":
            hourRate = 30
        else:
            if jobCode == "J":
                hourRate = 50
            else:
                hourRate = 0
    
    return hourRate
# Main
userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()
assignHours = 40
overTimeHours = 0
overTimePayRate = 0
totalGrossPay = 0
while userEntry == "yes":
    employeeLastName = input("Enter employee's last name: ")
    jobCode = input("Enter employee's job code (L, A, J): ").upper() 
    hoursWorked = float(input("Enter number of hours worked: "))

    payRate = determinePayRate(jobCode)
    print(f"Pay Rate: {payRate}")

    grossPay = computeGrossPay(hoursWorked, payRate)

    print(f"Employee LastName:{employeeLastName}") 
    print(f"Gross pays:{grossPay}") 


    totalGrossPay = totalGrossPay + grossPay
    userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()

print(f"Total Gross Pay: {totalGrossPay}")


