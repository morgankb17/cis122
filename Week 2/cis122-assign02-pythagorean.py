'''
CIS 122 Summer 2020 Assignment 2
Author: Morgan Bartlett
Credit:
Description: Create functions using the pythagorean theorem
'''
# References
# https://www.rapidtables.com/calc/math/pythagorean-calculator.html
# http://mathforum.org/dr.math/faq/faq.pythagorean.html
# https://docs.python.org/3/library/math.html

import math

# Question 1
print("*** Question 1 ***")

# Create two functions to calculate a missing side using the Pythagorean Theorem

# Function to calculate missing side c / hypotenuse
def calc_side_c(a,b):
    # c = square root of a^2 + b^2
    return round(math.sqrt(math.pow(a,2) + math.pow(b,2)),2)
# Test
print("c =", calc_side_c(5,10))

# Function to calculate missing side/leg a or b
def calc_side_ab(ab,c):
    # ab = square root of c^2 - ab^2
    return round(math.sqrt(math.pow(c,2) - math.pow(ab,2)),2)
# Test
print("a/b =", calc_side_ab(4,8))
