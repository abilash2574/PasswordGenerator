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
def enter():
    print("Enter the length of your password.")
    passLen = int(input())
    print("Enter the amount of numbers in your password.")
    passNums = int(input())
    print("Enter the amount of special characters in your password.")
    passSpCh = int(input())
    
    return(passLen, passNums, passSpCh)
    
  
