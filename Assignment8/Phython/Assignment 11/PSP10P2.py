def computeScore(exam1, exam2, exam3):
    
    totalPoint = exam1 + exam2 + exam3 
    average =  totalPoint/3

    return totalPoint, average

name = input("Student last name  ")
exam1 = int(input("exam1  "))
exam2 = int(input("exam2  "))
exam3 = int(input("exam3  "))
totalPoint, average = computeScore(exam1, exam2, exam3)

print(f"name: ${name}")
print(f"totalPoint: ${totalPoint:.2f}")
print(f"average: ${average:.2f}")





