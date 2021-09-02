'''
CIS 122 Summer 2020 Assignment 6
Author: Morgan Bartlett
Credit:
Description: Program that reads a .txt file and prints the amount of numbers,
any comments, the sum of the numbers, and their average.
'''
import math
import os
from cis122_assign06_shared import pad_left, pad_right

while True:
    user = input("Enter filename (blank to exit): ")
    exists = os.path.exists(user)
    if user == '':
        break
    elif exists == False:
        print("Invalid filename:", user)
    if exists:
        fin = open(user)
        c_count = 0
        l_count = 0
        total = 0
        avg = 0
        for line in fin:
            stripped = line.strip()
        
            if line[0] == '#':
                c_count += 1
            else:
                l_count += 1
                num = int(line)
                total += num
        avg = total / l_count
        fin.close()
        print("Count:", pad_left(str(l_count),10))
        print("Comments:", pad_left(str(c_count),10))
        print("Total:", pad_left(str(total),10))
        print("Average:", pad_left(str(round(avg,2)),10))
