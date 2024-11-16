"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Omar Soliman
Student ID: osolima6
File created: October 22, 2024
******************************
This file contains functions to ask the user to either create a new password or generate
a random password and check its strength. The program will continue this process until the password
is strong enough.
The function in this file is:
1. process_password(min_strength): Asks the user to input a password until one is strong enough.
"""

from password import *
from generate import *

def process_password(min_strength):
    """
    Description: The function will prompt the user to either create a new password or generate
    a random password and check its strength.

    Parameter: min_strength is the minimum requirement strength for the password.
    """
    while True:
        # Asks the user to enter a password or enter X to generate a random password.
        user_password = input("Type in a new password or type X for a randomly generated password: ")
        if "x" in user_password.lower():
            # Generates a random password with the length of 15 characters.
            generated_password = generate_password(15)
            strength = password_strength(generated_password)
            print(f"Your password: {generated_password}")
            print(f"Your password has a strength of {strength}")
        else:
            # Calculates the strength of the password.
            strength = password_strength(user_password)
            print(f"You entered: {user_password}")
            print(f"Your password has a strength of {strength}")

        # Check if the password is strong enough.
        if strength >= min_strength:
            print("Your password is strong enough! Thank you.")
            break
        else:
            print("Your password is not strong enough, please create a new password that is strogner.")
