#4) ask the user for a number. Tell that user whether the number is odd or even

#creates the variable setting it as a number
myNumber = int(input("Please enter a number: "))

# Check if the number is even or odd
# % modulo checks if multiples given number fits exactly into value it is checked against
# i.e. 10 % 3 would leave 1, as 3, 3, 3, 1 equals 10
if myNumber % 2 == 0:
    print("This number is Even")
else:
    print("This number is Odd")


#andys code

# num = int(input("Please enter a number: "))
# #
# # if num % 2 == 0:
# #      print("This number is Even")
# #  else:
# #     print("This number is Odd")

# print("Number was even" if num % 2 == 0 else "number was odd")

