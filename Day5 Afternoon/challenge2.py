# 2) ask the user for a number between 1 and 100 - return all Even numbers form 0 to their chosen number

myNumber = int(input('Please enter a number between 1 - 100: '))

def show_evens(num):
    if num > myNumber:
        return
    print(num)
    show_evens(num+2)

show_evens(0)