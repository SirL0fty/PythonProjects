#!/usr/bin/env python3

def celsius_to_fahrenheit(celcius):
        fahrenheit = (celcius * 9/5) + 32
        return fahrenheit

print("Celsius   Fehrenheit")
print("-5       ", celsius_to_fahrenheit(-5))
print("30       ", celsius_to_fahrenheit(30))
print("100      ", celsius_to_fahrenheit(100))
