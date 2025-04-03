def calculateAverageScore(game1, game2, game3):
    # Calculate the average score
    return (game1 + game2 + game3) / 3

def calculateAverageWithHandicap(averageScore, handicap):
    # Calculate the average score with handicap
    return averageScore + handicap


last_name = input("Enter the bowler's last name: ")
game1 = float(input("Enter the score for Game 1: "))
game2 = float(input("Enter the score for Game 2: "))
game3 = float(input("Enter the score for Game 3: "))
handicap = int(input("Enter the handicap: "))

averageScore = calculateAverageScore(game1, game2, game3)
averageWithHandicap = calculateAverageWithHandicap(averageScore, handicap)

print(f"\n--- Bowler's Information ---")
print(f"Bowler's Last Name: {last_name}")
print(f"Average Score: {averageScore:.2f}")
print(f"Average Score with Handicap: {averageWithHandicap:.2f}")