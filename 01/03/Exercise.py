#!/usr/bin/env python3

# Try at least one part from each question!!
# 1a - Given a list of the numbers between 1 and 10 (but excluding one number) find the missing number
# 1b - Modify your program to remove a random number
# 1c - Update the program to have all numbers from 1 to 100 and remove a random number of elements. Find how many numbers were removed and what they were
# 1d - Create a new program that duplicates one element in the list at random and then find which number has been duplicated

# 2a - Given the following tuple of numbers, what is the difference between the biggest and smallest number? 2, 5, 12, 7, 9
# 2b - Find the product of the elements of the tuple(product is each item multiplied together)
# 2c - Modify your program to generate a tuple of random numbers of a random length and still show what the difference and product is

# 3a - Create a dictionary to store the favourite colours of the following individuals
#    * Becci prefers green
#     * Steve prefers orange
#     * Melinda prefer purple
#     * Ryan prefers orange
#     * Nate prefers green
#     * Anna prefers green
#  3b - Add your own favourite colours. Update Melinda’s preference to green and remove Sandy’s preference from the dictionary
#  3c - Write code to create a new dictionary that has the key as each colour’s name and the value being how many people have that colour as their favourite
#  3d - Write code to create another dictionary that has the colour name as the key and a list of all the people that don’t have that colour as their favourite as the value

#1a and 1b
listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
numbers = set(listOfNumbers)
newList = []
for i in range(1, listOfNumbers[-1]):
    if i not in numbers:
        newList.append(i)
print("The missing number is:", newList)

#2a
my_tuple = 2, 5, 12, 7 ,9

# my_list = list(my_tuple)
# my_list.sort()
# difference = my_list[-1] - my_list[0]
# print(difference)

difference = max(my_tuple) - min(my_tuple)
print(difference)

#3a


