'''
CIS 122 Summer 2020 Assignment 2
Author: Morgan Bartlett
Credit:
Description: Create functions that calculate the amount of cement poured in yards
'''
# References
# https://www.concretenetwork.com/concrete/howmuch/calculator.htm
# https://todayshomeowner.com/cubic-yard-calculator/

import math

# Function to calculate the slabs
def calc_yards_cement(t,w,l):
    # Convert the dimension in inches to feet
    thick_ft = t / 12
    # Multiply the dimensions together to find cubic feet
    t_w_l = thick_ft * w * l
    # Divide cubic feet by the number of cubic feet in a cubic yard
    cubic_yard = t_w_l / 27
    return round(cubic_yard,2)

# Print function
def print_results(t,w,l,calc_yards_cement):
    print("A cement slab", t,'" thick,',w,"' wide and", l,"' long requires", calc_yards_cement, "yards of cement")
