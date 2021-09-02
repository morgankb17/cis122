'''
CIS 122 Summer 2020 Assignment 6
Author: Morgan Bartlett
Credit:
Description: Functions that add padding to content
'''
def pad_string(data, size, direct=-1, chr = ' '):
    '''
    Function that will add padding to the content of the argument data, either
    left or right
    Args:
        data (str)(int): content to be printed
        size (int): padding size
        direct (int): Direction of padding, default is left (-1), for right, enter 1
        chr: type of padding, default is one space
    Returns:
        res (str): the content with padding
    '''
    res = data
    if direct == -1:
        if len(data) < size:
            pad_size = size - len(data)
            res = chr * pad_size + data
        return res
    elif direct == 1:
        if len(data) < size:
            pad_size = size - len(data)
            res = data + chr * pad_size
        return res

def pad_left(data, size, chr = ' '):
    '''
    Function that add padding to the left of content
    Args:
        data (str, int): content to be printed
        size (int): padding size
        chr: type of padding, default is one space
    Returns:
        res (str): the content with padding
    '''
    res = data
    if len(data) < size:
        pad_size = size - len(data)
        res = chr * pad_size + data
    return res

def pad_right(data, size, chr = ' '):
    '''
    Function that add padding to the right of content
    Args:
        data (str, int): content to be printed
        size (int): padding size
        chr: type of padding, default is one space
    Returns:
        res (str): the content with padding
    '''
    res = data
    if len(data) < size:
        pad_size = size - len(data)
        res = data + chr * pad_size
    return res
