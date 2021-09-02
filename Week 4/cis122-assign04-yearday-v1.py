'''
CIS 122 Summer 2020 Assignment 4
Author: Morgan Bartlett
Credit:
Description: Create a function that takes a year and a day of that year, then returns the corresponding date
'''
# 1. Prompt user for year
year = int(input("Enter a year: "))
  # a. Validate that year is > 0, otherwise print error message
# 2. Prompt user for day of the year (out of 365 or 366)
day = int(input("Enter a day of the year: "))
  # a. Validate that day of the year is > 0, otherwise print error message
  # b. Validate that the day of the year doesn't exceed the days in the year, depending if it's a leap year or not based on the first prompt.
# 3. Calculate the month based on the given year and day of year
def is_leap_year(year):
    '''
    Check if the given year is a leap year

    Args:
        year (int): A given year
    Returns:
        year (int): The leap year
        '' (str): Not a leap year
    '''
    is_leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return year
            else:
                return ''
        else:
            return year
    else:
        return ''
if is_leap_year(year) :
        
# 4. Print the result date
