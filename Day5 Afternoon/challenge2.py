# 2) ask the user for a number between 1 and 100 - return all Even numbers form 0 to their chosen number

# Start an infinite loop
while True:
    # Get user input and store it as a string
    user_number = input("Enter a number to check if it's odd or even: ")

    # Try to convert the string into an integer
    try:
        num = int(user_number)

        # Break out of the loop if the string can be converted into an integer
        break
    except ValueError:
        # If the string cannot be converted into an integer, print an error message
        print("Please enter a valid whole number.")

# Check if the number is even or odd
# % modulo checks if multiples given number fits exactly into value it is checked against
# i.e. 10 % 3 would leave 1, as 3, 3, 3, 1 equals 10

even_check = num % 2

# If the result of the modulus operation is 0, the number is even
if not even_check:
    print("Your number is even")
# If the result of the modulus operation is not 0, the number is odd
else:
    print("Your number is odd")

#andy's code

# num = int(input("Enter a number from 0 - 100: "))
# for i in range(0, num+1):
#     if i % 2 == 0:
#         print(i)