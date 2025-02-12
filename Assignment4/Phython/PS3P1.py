# 1.	Allow the user to enter two exam scores from the keyboard. 
# The first exam is worth 60% of the total points and the second exam is worth 40%. 
# Calculate the total score by multiplying each exam score input by 
# the respective weighting then add the two results together.
# Display the total. 

examScore1 = float(input("Enter the score for the first exam: "))
examScore2 = float(input("Enter the score for the second exam: "))

weightExam1 = 0.60
weightExam2 = 0.40

weightedScore1 = examScore1 * weightExam1
weightedScore2 = examScore2 * weightExam2

totalScore = weightedScore1 + weightedScore2

print("Total score is:  ", float(totalScore))