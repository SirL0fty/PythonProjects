#!/usr/bin/python

import getpass

PIN: str = '1234' #hard codes the pin number
max_tries = 3 #sets the max tries


def check_pin(the_pin): #defines the function check_pin
    return the_pin == PIN


def run():
    tries = 0 #set's the amount of tried

    while tries < max_tries: #checks tries vs max tries
        entered_pin = getpass.getpass(prompt='Please enter your PIN: ') #ask's the user to input their pin
        if check_pin(entered_pin): #checks if pin is correct
            print('Correct')
            break
        else:
            print('Incorrect. Please enter again: ') #if not correct prompts the customer to enter again
        tries += 1

    else:  # Else will run when no `break` statement is run in while loop.
        print("Sorry you have enter your pin 3 incorrect times, you are now locked out!")

if __name__ == '__main__':
    run()
