"""
    This is a python program that Generates Password with the following features.
    # A program that generates a random password for the user.
    # - User input: Length of password, amount of numbers, amount of special characters.
    # - Mix of upper and lower case numbers
    # - Minimum of 6 characters
    # - Instantly copy to clipboard (optional)
    # - Give it an UI (optional)
    
"""
#------------------Importing Packages-------------------------
import random, pyperclip, string

def pre_PasswordGenerator():
    letters = string.ascii_letters
    digits = string.digits
    special = "@#$%!^&*"
    return letters, digits, special
