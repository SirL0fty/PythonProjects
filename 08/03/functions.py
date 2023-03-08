#!/usr/bin/env python3

def multiply(*, x = 100, y = 10): #* defining multipy using forced named parameters

        return x * y

my_tup = 23, 45, 245
print(multiply())
print(multiply(x=10, y=10))
# print(multiply(10, 100))

#* Unpacking and variadic functions
def my_func(a, b, c):
        print(a, b, c)
        return
my_tup = 23, 45, 245
my_func(*my_tup)

