'''
CIS 122 Summer 2020 Lab 7
Author: Morgan Bartlett
Credit:
Description: List exercises with score-related functions
'''
import random

def gen_random_integer_list(num, start_range = 1, end_range = 100, sort_list = 'N'):
    '''
    This function returns a list of random numbers between two integers given num for the amount of numbers.
    '''
    t = [] # Initialize an empty list
    if num <= 0: # Make sure num is greater than 0
        print('num must be > 0')
        
    elif not isinstance(num, int): # Make sure num is an integer
        print('num must be an integer')
        
    elif not isinstance(start_range, int) or not isinstance(end_range, int): # Make sure the start and end range are integers
        print('start_range and end_range must be integers')
        
    else:
        for i in range(num):
            r = random.randint(start_range, end_range) # Initialize a variable to handle each random element in the range
            t.append(r) # Append the random value to the list

        if sort_list.upper() == 'Y': # Sort the list if sort_list = Y
            t.sort()
    return t # Return the list

t = gen_random_integer_list(100) # Default number list

def get_high_score(lst=[]):
    '''
    This function returns the highest score in a list of numbers
    '''
    if not isinstance(lst, list): 
        print('List argument expected')
        return -1
    elif len(lst) == 0:
        return 0
    else:
        new_lst = lst[:] # Copy the list
        new_lst.sort() # Sort the new list
        high = new_lst.pop() # Pop out the highest number in the list
    return high # Return popped number

def get_low_score(lst=[]):
    '''
    This function returns the lowest score in a list of numbers
    '''
    if not isinstance(lst, list):
        print('List argument expected')
        return -1
    elif len(lst) == 0:
        return 0
    else:
        new_lst = lst[:] # Copy the list
        new_lst.sort() # Sort the list
        low = new_lst.pop(0) # Pop out the lowest number in the list
    return low

def get_mean_score(lst=[]):
    '''
    This function returns the average score from a list of numbers
    '''
    if not isinstance(lst, list):
        print('List argument expected')
        return -1
    elif len(lst) == 0:
        return 0
    else:
        avg = sum(lst) / len(lst) # Calculate average of all numbers in the list
    return avg

def get_median_score(lst=[]):
    '''
    This function returns the median score from a list of numbers
    '''
    if not isinstance(lst, list):
        print('List argument expected')
        return -1
    elif len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst.pop() # Return the median if the list has the length of 1
    elif len(lst) % 2 == 0 and len(lst) != 0: # If the length of the list is even...
        new_lst = lst[:] # Copy the list
        new_lst.sort() # Sort the list
        i = (len(new_lst) - 1) // 2 # Calculate median
        return new_lst[i] # Take index of new_lst with i
    else:
        return (new_lst[i] + new_lst[i + 1]) // 2 # Calculat median if len of lst is odd

def count_range(lst,start,end):
    '''
    This function counts the amount of letter grades from a list of score numbers
    '''
    if not isinstance(lst, list):
        print('List argument expected')
        return -1
    elif len(lst) == 0:
        return 0
    elif not isinstance(start, int) or not isinstance(end, int):
        print('start and end must be integers')
        return -1
    elif start > end or start == end:
        print('start must be < end')
        return -1
    else:
        # Initialize counters for letter grades
        a = 0
        b = 0
        c = 0
        d = 0
        f = 0
        for i in lst:
            if i >= start and i <= end:
                a += 1
            elif i >= start and i <= end:
                b += 1
            elif i >= start and i <= end:
                c += 1
            elif i >= start and i <= end:
                d += 1
            elif i < start and i <= end:
                f += 1
                
        return a # Return amount of letter grades in list of numbers
    
def list_range(t):
    '''
    This function calls count_range and prints the corresponding letter grades and the amount of them from
    a list of numbers
    '''
    print("A -",count_range(t,90,100))
    print("B -",count_range(t,80,89))
    print("C -",count_range(t,70,79))
    print("D -",count_range(t,60,69))
    print("F -",count_range(t,1,59))
