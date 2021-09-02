'''
CIS 122 Summer 2020 Lab 5
Author: Morgan Bartlett
Credit:
Description: Develop a factorial function
'''
import math

def factorial(num):
    '''
    This function takes a number, and returns a value that are all of the
    numbers that count up to said number, multiplied together.

    Args:
        num (int): a number
    Returns:
        None: if num < 0
        1 (int): if num == 0
        total (int): all numbers that count to num, multipled together
    '''
    # Convert the number to integer
    int(num)
    # If num < 0, print error and return None
    if num < 0:
        print("Must be >= 0")
        return None
    # If num == 0, return 1
    elif num == 0:
        return 1
    # if num > 0
    elif num > 0:
        # Intialize total to 1
        total = 1
        # Loop from 1 to num
        for i in range(1,num+1):
            total = total * i
        # Return total
        return total
    else:
        print("Not a valid number")

# print(factorial(5))

def test_factorial(num, show=False):
    '''
    Tests the function factorial(), prints evidence of errors/ no errors if
    show=True, prints total number of errors regardless

    Args:
        num (int): A number to test
        show (bool): If user would like to show a list of each factorial
                     set show=True. Default is False
    Returns:
        None
    '''
    errors = 0
    range_num = num + 1
    for i in range(range_num):
        alpha = factorial(num)
        bravo = math.factorial(num)
        if show == True:
            print(i,":",factorial(i),factorial(i))
        if alpha != bravo:
            errors = errors + 1
            print("*", alpha, bravo)
    print("Errors ({}):".format(num),errors)

# test_factorial(5,True)

user = int(input("Enter factorial number: "))
print(factorial(user))
