def computeTuitionOwed(creditsTaken, districtCode):
    if districtCode == "I":
        costPerCredit = 250.0
    else:
        if districtCode == "O":
            costPerCredit = 550.0
    tuitionOwed = (creditsTaken * costPerCredit)

    return tuitionOwed


# Main
totaTuitionOwed = 0
studentCount = 0
userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()
while userEntry == "yes":
    studentLastName = input("Enter student's last name: ")
    creditsTaken = int(input("Enter number of credit hours: "))
    districtCode = input("Enter student's district code (I for In-district, O for Out-of-district):").upper() 

    tuitionOwed = computeTuitionOwed(creditsTaken, districtCode)

    print(f"Student Last Name: {studentLastName}, Tuition Owed: {tuitionOwed:.2f}")
    totaTuitionOwed = totaTuitionOwed + tuitionOwed
    userEntry = input("Do you want to continue run this program? (Yes/No): ").strip().lower()

print(f"Total Tution Owed: {totaTuitionOwed}")


