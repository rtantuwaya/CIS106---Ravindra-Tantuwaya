def calculateBattingAverage(hits, atBats):
    if hits == 0:
        averge = 0
    else:
        averge = float(hits) / atBats
    
    return averge

# Main

playerCount = 0
print("Enter player information (Ctrl+Z or Ctrl+D to stop):")
#userEntry = input()

while True:
    try:
        lastName = input("Enter player's last name: ")
        hits = int(input("Enter number of hits: "))
        atBats = int(input("Enter number of at-bats: "))
        battingAverage = calculateBattingAverage(hits, atBats)

        print(f"{lastName}'s Batting Average: {battingAverage:.3f}")
   
        playerCount += 1

    
    except ValueError:
        print("Invalid input! Please enter numeric values for hits and at-bats.")
        continue

    except EOFError:
        print(f"\nTotal number of players entered: {playerCount}")
        break