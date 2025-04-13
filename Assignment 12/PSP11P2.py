lastName = ["Smith", "Johnson", "Brown", "Taylor", "Anderson",
            "Thomas", "Jackson", "White", "Harris", "Martin"]

examScore = [85, 92, 78, 88, 95, 67, 80, 90, 73, 89]

def displayNameAndScore(names, scores):
    print("Last Name and Score:")
    for i in range(len(names)):
        print(f"{names[i]}: {scores[i]}")

def displayNameAndScoreReverse(names, scores):
    print("Names and Exam Scores in Reverse Order:")
    for i in range(len(names)-1, -1, -1):
        print(f"{names[i]}: {scores[i]}")

# Call the functions
displayNameAndScore(lastName, examScore)
print()
displayNameAndScoreReverse(lastName, examScore)