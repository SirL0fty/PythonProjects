#3) ask the user for 3 names, append each of the names to a list, then print out that list

name1 = input("Please enter name 1: ")
name2 = input("Please enter name 2: ")
name3 = input("Please enter name 3: ")

namesList = list()
namesList.append("Names:")
namesList.append(name1)
namesList.append(name2)
namesList.append(name3)

print(namesList)