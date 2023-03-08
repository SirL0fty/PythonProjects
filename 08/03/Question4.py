#!/usr/bin/env python3

def find_palindromes(start, end):
        palindromes = []
        for num in range(start, end+1):
        # Check if the number is equal to its reverse
            if str(num) == str(num)[::-1]:  # * [::-1] reverses a sequence such as a string, list or tuple.
                        palindromes.append(num)
        return palindromes

palindromes = find_palindromes(100, 200)
print(palindromes)