#3) ask the user for 3 names, append each of the names to a list, then print out that list

#asks the user to enter 3 different names
name1 = input("Please enter name 1: ")
name2 = input("Please enter name 2: ")
name3 = input("Please enter name 3: ")

#creates the list to store the names
namesList = []
#adds the names to a list using the namesList variable starting with "Names"
namesList.append("Names:")
namesList.append(name1)
namesList.append(name2)
namesList.append(name3)

#prints the results
print(namesList)

# names = []
# for i in range (3):
#     name = input("Enter a name: ")
#     names.append(name)

# for name in names:
#     print(name)