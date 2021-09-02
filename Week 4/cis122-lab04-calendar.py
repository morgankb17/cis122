'''
CIS 122 Summer 2020 Lab 4
Author: Morgan Bartlett
Credit:
Description: Calendar-related functions
'''
def get_full_month(m):
    '''
    Given a number, return the corresponding month

    Args:
        m (int): Number of the month
    Returns:
        "" (str): the correct month, depending on the given number
    '''
    if m == 1:
        return "January"
    elif m == 2:
        return "February"
    elif m == 3:
        return "March"
    elif m == 4:
        return "April"
    elif m == 5:
        return "May"
    elif m == 6:
        return "June"
    elif m == 7:
        return "July"
    elif m == 8:
        return "August"
    elif m == 9:
        return "September"
    elif m == 10:
        return "October"
    elif m == 11:
        return "November"
    elif m == 12:
        return "December"
    elif m < 1 or m > 12:
        return 'Must be an integer between 1 and 12 ('+ str(m) +' is invalid).'
    else:
        return print("")

def test_get_full_month():
    for i in range(14):
        print(i, end=' ')
        print(get_full_month(i))
        
test_get_full_month()

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

def test_is_leap_year(start_year, end_year):
    for year in range(start_year, end_year + 1):
        print(is_leap_year(year))
