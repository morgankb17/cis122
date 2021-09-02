'''
CIS 122 Summer 2020 Assignment 8
Author: Morgan Bartlett
Credit:
Description: Group manager
'''
d = {}

def create_group(d):
    pass

def list_groups(d):
    pass

def add_group_data(d):
    pass

def list_group_data(d):
    pass

def cmd_help():
    print("?: List commands")
    print("C: Create a new group")
    print("G: List groups")
    print("A: Add data to a group")
    print("L: List data for a group")
    print("X: Exit")
    print()
    
print(">> Welcome to Group Manager <<")
print("This program creates groups with dynamic properties")
print()
while True:
    user = input("Command (empty or X to quit, ? for help): ")
    user = user.strip()
    user = user.upper()
    if user == '' or user == 'X':
        break
    elif user == '?':
        cmd_help()
    
