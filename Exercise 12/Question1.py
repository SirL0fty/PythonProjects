#!/usr/bin/env python3

#* sets a list called cheese 
cheese =  ['Cheddar', 'Stilton', 'Cornish Yarg']

#* this add's O, k, e to list and not in full
#cheese += 'Oke'

#* will also add new item to the list using the brackets
cheese += ['Parmesan']

#* apends adds Oke into the list
cheese.append ('Oke')

#* extends the list with the new cheeses
cheese.extend(['Mozzarella', 'Red Leicester'])
print(cheese)