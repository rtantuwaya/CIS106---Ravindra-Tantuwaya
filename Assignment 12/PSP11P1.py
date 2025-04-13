lastName = ["Smith", "Johnson", "Brown", "Taylor", "Anderson",
            "Thomas", "Jackson", "White", "Harris", "Martin"]

# Function to display names
def displayName(names):
    print("Last Name:")
    for name in names:
        print(name)

# Function to display names in reverse order
def displayNameReverse(names):
    print("Last Names in Reverse Order:")
    for name in reversed(names):
        print(name)


# Call the function
displayName(lastName)
print()
displayNameReverse(lastName)