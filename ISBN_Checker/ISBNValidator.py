""" Author: Lucy An
    Date: December 1 2017
    Description: Displaying the text-based user interface that will call upon functions in the checkISBN module. 

"""
# Calling the checkISBN module for the use of its functions.
import checkISBN


def main():
    """This function calls mainline logic and passes the menu_status into menu as an argument."""
    menu_status = True 
    # This statement tells the interpreter to call the menu() functon and to pass menu_status from main() as an argument.
    menu(menu_status)

def menu(menu_status):
    """This function accepts menu_status as a parameter, displays the menu and evaluates the user's choice of action."""
    while menu_status == True: 
        print ""
        print "BOOK ISBN VALIDATOR"
        print 
        print "What type of ISBN code would you like to validate:"
        print 
        print "1. ISBN-10"
        print "2. ISBN-13"
        print "Q. Quit Program"
        
        choice = raw_input("Choice: ")
        
        if choice == str(1):
            number = input("Please enter your ISBN Number: ")
            result10 = checkISBN.is_ISBN10(number)
            if result10 == True:
                print "Your ISBN number is valid."
            else:
                print "Sorry, your ISBN number is NOT valid."
    
        elif choice == str(2):
            number = input("Please enter your ISBN Number: ")
            result13 = checkISBN.is_ISBN13(number)
            if result13 == True:
                print "Your ISBN number is valid."
            else:
                print "Sorry, your ISBN number is NOT valid."            
        elif choice == "Q" or choice == "q":
        # The user will exit the program since False does not satisfy the condition of the while loop.
            menu_status = False 
        else:
            print "Sorry, that's an invalid option."
            
            
main()
print "Have a nice day!"            
            



