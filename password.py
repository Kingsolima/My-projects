"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Omar Soliman
Student ID: osolima6
File created: October 22, 2024
******************************
This file contains functions that evaluates the strength of the password based off of the length
and the number of groups used (lowercase letter, uppercase letters, digits, and symbols).
The functions used are:
1. count_groups(pwd) - Counts the number of groups used in the password.
2. password_strength(pwd) - Does The calculation of the strength of
the password using the length and number of groups used.
"""

def count_groups(pwd):
    """
    Description: This function takes the string pwd (the password) Counts the number of groups
    (lowercase letter, uppercase letters, digits, and symbols) used in the password. If it uses
    any characters not in the groups it will be ignored.

    Parameters: pwd is the password that's going to be checked.

    Returns: It will return the integer of the number of groups used.
    """
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    SYMBOLS = "!@#$%^&*/?-+=,.|~"

    groups = 0
    has_lower = has_upper = has_digit = has_symbol = False

    # It will iterate through every character in the password to see what group they are in.
    for char in pwd:
        if char in LOWERCASE:
            has_lower = True
        elif char in UPPERCASE:
            has_upper = True
        elif char in DIGITS:
            has_digit = True
        elif char in SYMBOLS:
            has_symbol = True

    # Count how many groups are used.
    if has_lower:
        groups += 1
    if has_upper:
        groups += 1
    if has_digit:
        groups += 1
    if has_symbol:
        groups += 1

    return groups

def password_strength(pwd):
    """
    Description: This function will use count_groups(pwd) (or the number of groups used)
                and the length of the password to calculate the strength of the password.

    Parameters: pwd is the password to be calculated.

    Returns: It returns the integer value of the strength variable.
    """

    strength = 0

    # Gets the length and number of groups used.
    length = len(pwd)
    groups = count_groups(pwd)

    # If the password contains these invalid characters the strength value will equal 0 automatically.
    if " " in pwd or "\t" in pwd or "/n" in pwd:
        strength = 0

    # Determines the strength of tha password.
    elif length < 5:
        strength = 0

    elif 5 <= length <= 8:
        if groups == 1:
            strength = 1
        elif groups == 2 or groups == 3:
            strength = 2
        elif groups == 4:
            strength = 3

    elif 9 <= length <= 12:
        if groups == 1:
            strength = 2
        elif groups == 2 or groups == 3:
            strength = 3
        elif groups == 4:
            strength = 4

    elif length > 12:
        if groups == 1:
            strength = 3
        elif groups == 2 or groups == 3:
            strength = 4
        elif groups == 4:
            strength = 5

    return strength