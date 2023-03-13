#!/usr/bin/env python3

# 	this isn't
#               very easy¡

# print("\tthis isn't\n\t\t very easy\u00A1")

# print("\u0276 \u0278 \u025D")

# sentence = ("Finished files are the result of years of scientific study combined with the experience of years.")
# count = sentence.lower().count("f")

# print(count)

# names = ['Tom', 'Harry', 'Jane', 'Mary']
# suffix = ['st', 'nd', 'rd', 'th']
# n = 1
# s = f"{str(n+1) + suffix[n]} of {len(names)} is {names[n]}"
# print(s)
# Exercises
# ‘ThisIsAReallyLongStringThatIsFunToConvert’
# 1. PascalCase to snake_case
# ‘this_is_a_really_long_string_that_is_fun_to_convert’
# 2. snake_case to PascalCase
# 3. Is one an anagram of the other?
# * “wholesome python activity”
# * “Woven Polytheistic Mat Toy”

# Q1 Convert PascalCase to snake_case
import re

pascal_string = "ThisIsAReallyLongStringThatIsFunToConvert"
snake_string = re.sub(r'(?<!^)([A-Z])', r'_\1', pascal_string).lower()
print(snake_string)

#Q2 Convert snake_case to PascalCase
snake_string = "this_is_a_really_long_string_that_is_fun_to_convert"
pascal_string = snake_string.title().replace('_', '')
print(pascal_string)

#Q3
string1 = "wholesome python activity"
string2 = "Woven Polytheistic Mat Toy"

# Remove all spaces and convert to lowercase
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Sort the letters of each string
string1_sorted = sorted(string1)
string2_sorted = sorted(string2)

# Compare the sorted strings
if string1_sorted == string2_sorted:
        print("These strings are anagrams of each other!")
else:
        print("These strings are not anagrams.")

pascal_string = "ThisIsAReallyLongStringThatIsFunToConvert"
snake_string = ""

for i, char in enumerate(pascal_string):
        if char.isupper() and i != 0:
                snake_string += "_"
                snake_string += char.lower()

print(snake_string)
