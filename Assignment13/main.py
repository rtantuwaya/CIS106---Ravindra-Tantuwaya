def dl1(mylist):
    n = int(input("Number of item for your list"))
    for n in range(0,n,1):
        s = int(input("Enter an integer"))
        mylist.append(s)
    return mylist

def displaylist(mylist):
    for item in mylist:
        print(item)



#main
mylist = [] #defining an empty list
mylist = dl1(mylist)
displaylist(mylist) # display each item in the list
print("Full list:", mylist)
mylist.insert(1, 90) 
print("Updated list.:", mylist)
if 99 in mylist:
    index = mylist.index(99)
    mylist[index] = 100
    print("Replace list.:", mylist)

# Create a second list
second_list = [500, 600, 700, 800, 900]
displaylist(second_list)
print("Second list:")

# Extend the first list with the second list
mylist.extend(second_list)

print("Updated first list after extending:")
displaylist(mylist)

# Remove the value 800 from the first list
if 800 in mylist:
    mylist.remove(800)
print("First list after removing 800:")
displaylist(mylist)

# Remove the third item (index 2) from the first list
if len(mylist) >= 3:
    del mylist[2]
print("First list after removing the third item:")
displaylist(mylist) 

grades = ["A", "B", "C", "A", "A", "C"]
print("Grades list:", grades)

# Count the number of A grades
a_count = grades.count("A")
print("Number of A grades:", a_count)
    
# Find the index of the first B grade
b_index = grades.index("B")
print("Index of the first B grade:", b_index)

# Check for grade "F" in the list
if "F" in grades:
    print("Grade F is in the list.")
else:
    print("Grade F is not in the list.") 


# Clear the list
second_list.clear()

# Display the cleared list
print("Second list after clearing:", second_list)

# Delete the list entirely
del second_list

# Try to display it with error handling
try:
    print(second_list)
except NameError:
    print("⚠️ The list 'second_list' no longer exists.")

players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print(players)

# Sort the list
players.sort()
# Display the sorted list
print(players)

# Make a copy of the list
players2 = players.copy()
# Display players2
print(players2)

# Reverse the order of players2
players2.reverse()

# Display players and players2
print("Original players list:", players)
print("Reversed players2 list:", players2)