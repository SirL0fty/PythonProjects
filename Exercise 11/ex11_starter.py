#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

#defines yell
def yell(text):
    number_of_characters = len(Belgium) #counts the number of letters in Belgium
    result = text + "!" * (number_of_characters) #sets the variable 
    print(result)

yell(Belgium)#runs the definition

#variable Belgium is decalred above
new_Belgium = Belgium.replace(",", ":")#creates a new variable and uses the replace function
print(new_Belgium)#prints new fucntion

ls = new_Belgium.split(":")#Spilts the new list at the semicolon 
print(int(ls[1]) + int(ls[3]))#converts the string to a number and add's them together to make 11183818
