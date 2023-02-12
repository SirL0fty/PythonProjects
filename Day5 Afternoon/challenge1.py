#1) write a program that asks the user for the radius of a circle and returns the area and the circumference

#Setting the variable of pi 
pi = 3.14159
#prompting the user to enter a number using float which sets a decimal place number
radius = float(input('Please enter the radius of the circle: '))

#creating the variable for each maths equation to use lower in the code
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius * radius

#displays the results to 2 decimal places using modulo %.2f
print(" Diameter Of a Circle = %.2f" % diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle3 = %.2f" %area)

#Andy's code

# r = int(input("Enter the radius: "))
# area = 3.142 * r ** 2
# circ = 2 * 3.142 * r
# print(f"Area is {area} - Circumference is {circ}")