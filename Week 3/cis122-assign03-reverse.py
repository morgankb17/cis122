'''
CIS 122 Summer 2020 Assignment 3
Author: Morgan Bartlett
Credit:
Description: Create a function that reverses a given string
'''
def reverse(s):
    '''
    Reverses a given string
    
    Args:
        s (str): A word, phrase, or sentence

    Returns:
        reverse_string (str): The word, phrase, or sentence, reversed
    '''
    reverse_string = "" # Empty string to hold the reversed string
    for i in s:
        reverse_string = i + reverse_string # Adds each letter of the string to the beginning of the "empty" string
    return reverse_string

print("Original: When in the Course of human events")
print("Reversed:", reverse("When in the Course of human events"))



