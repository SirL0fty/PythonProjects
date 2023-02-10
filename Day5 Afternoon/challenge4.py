#4) ask the user for a number. Tell that user whether the number is odd or even

myNumber = int(input("Please enter a number: "))

if myNumber % 2 == 0:
    print("This number is Even")
else:
    print("This number is Odd")