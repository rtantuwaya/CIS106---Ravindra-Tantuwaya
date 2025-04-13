# Function to load players names and batting averages from file
def loadPlayers(fileName):
    playerNames = []
    battingAverages = []
    with open(fileName, 'r') as file:
        for line in file:
            name, avg = line.strip().split(',')
            playerNames.append(name)
            battingAverages.append(float(avg))
    return playerNames, battingAverages

# Function to display player names and batting averages
def displayPlayers(names, averages):
    print("Player Name\tBatting Average")
    for i in range(len(names)):
        print(f"{names[i]}\t\t{averages[i]:.3f}")

# Function to serach for a player name
def searchPlayer(names, averages, searchName):
    for i in range(len(names)):
        if names[i].lower() == searchName.lower(): # Case -insensitive match
            return names[i], averages[i]
    return None, None

# Main Program
fileName = "players.txt"
playerNames, battingAverages = loadPlayers(fileName)

# Display all players
displayPlayers(playerNames, battingAverages)

# Repeatedly ask user for a name to search
while True:
    searchName = input("\nEnter a plyer's last name to search(or tyoe 'exit' to quit): ")
    if searchName.lower() == 'exit':
        print("Exiting search.")
        break
    name, avg = searchPlayer(playerNames, battingAverages, searchName)
    print(f"{name}'s batting averages is {avg:.3f}")
  