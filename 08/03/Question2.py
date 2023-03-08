#!/usr/bin/env python3

def multiplication_table(number, maximum=12):
       for num in range(1, maximum+1):
        result = number * num
        print(f"{number} x {num} = {result}")
        
        
multiplication_table(3)