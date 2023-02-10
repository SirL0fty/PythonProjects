# 2) ask the user for a number between 1 and 100 - return all Even numbers form 0 to their chosen number

# myNumber = int(input('Please enter a number between 1 - 100: '))
#
# def show_evens(num):
#     if num > myNumber:
#         return
#     print(num)
#     show_evens(num+2)
#
# show_evens(0)

#andy's code

num = int(input("Enter a number from 0 - 100: "))
for i in range(0, num+1):
    if i % 2 == 0:
        print(i)