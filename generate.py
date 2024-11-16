"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Omar Soliman
Student ID: osolima6
File created: October 22, 2024
******************************
This file contains a function that can generate a random password of a specific length,
using characters from four groups.
The function in this file:
1. generate_password(length): Generates a random password using the random module.
"""

import random

def generate_password(length):
    """
    Description: This function generates a random password of a specific length from the gour
                groups.

    Parameter: length is used to determine the length of the password.

    Returns: The randomly generate password.
    """
    password = ""
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    SYMBOLS = "!@#$%^&*/?-+=,.|~"

    # All the possible characters to be selected from
    ALL_CHARS = LOWERCASE + UPPERCASE + SYMBOLS + DIGITS

    # Randomly select letters from all_chars
    for i in range(length):
        password += random.choice(ALL_CHARS)

    return password