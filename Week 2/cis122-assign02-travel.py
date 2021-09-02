'''
CIS 122 Summer 2020 Assignment 2
Author: Morgan Bartlett
Credit:
Description: Question 3- travel time function
'''

# References
# https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php

# Calculate travel time in minutes given the distance in miles and the speed in mph
def calc_travel_time(distance, speed):
    # Divide distance by speed
    hour = distance // speed
    minutes = (distance / speed) - hour
    seconds = minutes / 60
    print("To travel",distance,"miles at",speed,"MPH it will take",hour,"hr", int(minutes),"min and", int(seconds),"sec")

# Output the travel time hours, minutes, and seconds given distance and speed
def print_travel_time(distance,speed):
    print(calc_travel_time(distance, speed))
    
