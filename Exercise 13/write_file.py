#!/usr/bin/env python3

#* opens a file called pelican.txt in write mode 
file = open("pelican.txt", "w")

#* writes a line in the file and add's a new line using /n
file.write("A wonderful bird is the pelican, \n")

#* adds a second line to the file
file.write("His bill holds more than his belican, \n")

#* creates lines in a list
lines = ["He can take in his beak, \n", "Enough food for a week, \n", "But I'm damned if I see how the helican. \n"]

#*add lines of text from the list using writelines
file.writelines(lines)