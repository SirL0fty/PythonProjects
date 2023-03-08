#!/usr/bin/env python3

def calculate_average(*values): 
        if not values:
                return 
        return sum(values) / len(values)


numbers = [int(input("Please enter a number: ")) for _ in range(5)]
average = calculate_average(*numbers)
print(average)