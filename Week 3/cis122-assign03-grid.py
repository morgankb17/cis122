'''
CIS 122 Summer 2020 Assignment 3
Author: Morgan Bartlett
Credit:
Description: Create a void function that prints a grid of numbers
'''
def draw_grid(num):
    '''
    Prints a horizontal list of numbers counting up to the given variable num,
    starting at integer 1. It then prints the same line but only as much as
    the variable num.

    Args:
        num (int): A number to be counted to and printed as a "grid"

    Returns:
        None
    '''
    for i in range(1, num+1): # 1, 2, 3, ...
        row = ""
        for n in range(1, num+1):
            row = row + " " + str(n)
        print(row)
        
draw_grid(2)
print()
draw_grid(4)
print()
draw_grid(10)

