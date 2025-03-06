numberOfStudent = 0
userEntry = input("Do you want to continue run this program? (Yes/No): ")

while userEntry == "Yes":
    lastName = input("Enter last name: ")
    examOneScore = float(input("Enter the first exam score: "))
    examTwoScore = float(input("Enter the second exam score: "))

    averageScore = (examOneScore + examTwoScore )/ 2

    print(f"Student Last Name: {lastName}")
    print(f"Average Score: {averageScore:.2f}")

    numberOfStudent = numberOfStudent + 1

    userEntry = input("Do you want to continue run this program? (Yes/No): ")

    print(f"Total number of students entered: {numberOfStudent}")







