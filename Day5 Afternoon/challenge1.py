#1) write a program that asks the user for the radius of a circle and returns the area and the circumference

pi = 3.14
radius = float(input('Please enter the radius of the circle: '))

diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius * radius

print(" Diameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle3 = %.2f" %area)