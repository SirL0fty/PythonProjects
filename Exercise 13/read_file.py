#!/usr/bin/env python3

#* opens the file and runs through the file and prints it out
with  open('pelican.txt', 'r') as infile:
        for lines in infile:
                print(lines, end='')


#* Creates a list and opens the content of the file and add the content to the list removing all whitespaces and lines using .strip string method and prints the number of items in the list
mylist = []

with open('pelican.txt', 'r') as file:
    for line in file:
        mylist.append(line.strip())

print(f"There are {len(mylist)} items in my list")