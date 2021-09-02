'''
CIS 122 Summer 2020 Assignment 7
Author: Morgan Bartlett
Credit:
Description: List manager
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

t = []

def cmd_help():
    '''
    Function that displays a list of help commands
    '''
    column1 = ['Add','Delete','List','Clear']
    column2 = ['Add to list','Delete information','List information','Clear list']
    print("*** Available commands ***")
    for elem1 in column1:
        print(pad_right(elem1,12),end='')
        if elem1 == 'Add':
            print(column2[0])
        elif elem1 == 'Delete':
            print(column2[1])
        elif elem1 == 'List':
            print(column2[2])
        elif elem1 == 'Clear':
            print(column2[3])
    print("Empty to exit")
        
def cmd_add(t):
    '''
    Function that adds items that are inputted by the user into a list (t)
    '''
    count = 0
    while True:
        item = input("Enter information (empty to stop): ")
        if item != '':
            t.append(item)
            count += 1
            print("Added, item count =",count)
        else:
            break
        
def cmd_delete(t):
    '''
    Function that deletes items from list (t) by their index
    '''
    for i in range(len(t)):
        print(i,pad_right('',1),end='')
        print(t[i])
    while True:
        val = int(input("Enter a number to delete (empty to stop): "))
        if len(t) == 0:
            print("All items deleted")
        elif val in range(len(t)):
            del t[val]
            for i in range(len(t)):
                print(i,pad_right('',1),end='')
                print(t[i])
            if len(t) == 0:
                print("All items deleted")
        elif val == '':
            break

def cmd_list(t):
    '''
    Function that returns the amount of items in the list (t) and prints those items
    '''
    item_amt = len(t)
    print("List contains",item_amt,"item(s)")
    for i in t:
        print(i)

def cmd_clear(t):
    '''
    Function that clears all items from the list
    '''
    item_len = len(t)
    del t[:]
    print(item_len,"item(s) removed, list empty")

def get_max_list_item_size(t):
    '''
    Function that returns the amount of help commands
    '''
    return len(column1)

while True:
    user = input("Enter a command (? for help): ")
    if user == '':
        break
    elif user == '?':
        cmd_help()
    elif user == 'list':
        cmd_list(t)
    elif user == 'add':
        cmd_add(t)
    elif user == 'clear':
        cmd_clear(t)
    elif user == 'del':
        cmd_delete(t)
