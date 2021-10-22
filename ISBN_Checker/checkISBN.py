""" Author: Lucy An
    Date: December 1 2017
    Description: Defining functions in the checkISBN module. 

"""

def get_digit(number, position):
    """This function returns a certain digit from the user-provided number by accepting the number and the desired postion as parameters."""
     
    digit = int((number % 10**(position + 1))/10**position)
    return digit 

def is_ISBN10(number):
    """This function checks the validity of an ISBN-10 number by accepting the ISBN number as a parameter and then returns either True or False."""
    sum = 0
    # Weighted Value is 9 because we start at the last digit 
    weightedValue = 9     
    
    checkDigit10 = get_digit(number, 0) 
    
    # This block adds the products of each digit with a weighted value, then uses it to find the thereotical last digit, and compares it with the actual check digit.  
    for position in range(1,10):
        digit = int((number % 10**(position + 1))/10**position)
        sum += digit*weightedValue
        weightedValue -= 1  
    lastDigit10 = sum % 11
    if lastDigit10 == checkDigit10:
        status = True 
    else:
        status = False 
    return status 

def is_ISBN13(number):
    """This function checks the validity of an ISBN-13 number by accepting the ISBN number as a parameter and then returns either True or False. """
    sum = 0
    checkDigit13 = get_digit(number, 0)
    
    # This block adds the products of each digit with a weighted value, then uses it to find the thereotical last digit, and compares it with the actual check digit.
    for position in range(12,0,-1):
        digit = int((number % 10**(position + 1))/10**position)
        if position % 2 == 0:
            sum += digit
        else:
            sum += digit*3
    lastDigit13 = 10 - (sum % 10)
    if checkDigit13 == lastDigit13:
        status = True
    else:
        status = False 
    return status 
