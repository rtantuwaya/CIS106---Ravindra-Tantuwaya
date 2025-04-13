# Function to load data from file into parallel arrays
def loadData(fileName):
    lastNames = []
    examScores = []
    with open(fileName, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')
            lastNames.append(name)
            examScores.append(int(score))
    return lastNames, examScores

# Function to display all names and scores
def displayNamesAndScores(names, scores):
    print("Names and Exam Scores:")
    for i in range(len(names)):
        print(f"{names[i]}: {scores[i]}")

def displayHighestAndLowest(names, scores):
    highVer = 0
    lowVar = 999
    highIndex = 0
    lowIndex  = 0

    for i in range(len(scores)):
        if scores[i] > highVer:
            highVer = scores[i]
            highIndex = i
        if scores[i] < lowVar:
            lowVar = scores[i]
            lowIndex = i

    print("\nHighest Score:")
    print(f"{names[highIndex]}: {scores[highIndex]}")

    print("\nLowest Score:")
    print(f"{names[lowIndex]}: {scores[lowIndex]}")

fileName = "students.txt"
lastNames, examScores = loadData(fileName)

displayNamesAndScores(lastNames, examScores)
displayHighestAndLowest(lastNames, examScores)