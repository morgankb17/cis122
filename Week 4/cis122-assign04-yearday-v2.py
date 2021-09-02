'''
CIS 122 Summer 2020 Assignment 4
Author: Morgan Bartlett
Credit:
Description: Create a function that takes a year and a day of that year, then returns the corresponding date
'''
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
    
def valid_year(year):
    '''
    Function that checks for valid year. Prints an error if year is invalid (false). Returns True
    if year is valid

    Args:
        year (int): Given year from user

    Returns:
        True (bool): True if year > 0
        False (bool): False if year is not > 0
    '''
    if year > 0:
        return True
    else:
        return False
    
def valid_day_of_year(year, day_of_year):
    '''
    Check if the day is a valid day of the year

    Args:
        year (int): given year
        day_of_year (int): desired day of year
    Returns:
        day_of_year (int): returns the day of year if its valid
        False (bool): an invalid day of year
    '''
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        if day_of_year > 0 and <= 366:
    else:
        return False
    
def input_year():
    '''
    Prompts the user for a year
    '''
    year = int(input("Enter the year: "))
    if year <= 0:
        return 0
    else:
        return year
def input_day_of_year(year):
    '''
    Prompts the user for a day of the year
    '''
    if valid_year(year) == True:
        if valid_day_of_year(year, day_of_year) == True:
            day = int(input("Enter the day of year: "))
            return day
        else:
            return 0
    else:
        return 0
        

    

    
