'''
CIS 122 Summer 2020 Assignment 1
Author: Morgan Bartlett
Credit:
Description: Introduction to programming problem set uses Python numeric data types
and operations to solve a variety of small problems.
'''

# Question 1

# Calculate the number of red hats and total cost for both red and blue hats
print("*** Question 1: Calculate total hat cost ***")
# Define the given variables
cost_red = 10
cost_blue = 5
total_hats = 65
# Part B bug fix: Used the "//" operator instead of "/" to round down the number of red hats
total_red = total_hats // 2 # 32.5 red hats
total_blue = total_hats - total_red # 32.5 blue hats
total_red_cost = total_red * cost_red # $325
total_blue_cost = total_blue * cost_blue # $162.5
total_cost = total_red_cost + total_blue_cost # $487.5
# print(total_red)
# print(total_blue)
# print(total_red_cost)
# print(total_blue_cost)
# print(total_cost)
print("Total Hat Cost:",total_cost)
print()

# Question 2

print("*** Question 2: Calculate the total daily steps ***")
# Define the variables
target_steps = 10000
steps_hourly = target_steps / 24
steps_minute = steps_hourly / 60
steps_second = steps_minute / 60
print("Daily steps:", target_steps)
print("Per hour:", steps_hourly)
print("Per minute:", steps_minute)
print("Per second:", steps_second)
print()
# Define the variables
target_steps = 50000
steps_hourly = target_steps / 24
steps_minute = steps_hourly / 60
steps_second = steps_minute / 60
print("Daily steps:", target_steps)
print("Per hour:", steps_hourly)
print("Per minute:", steps_minute)
print("Per second:", steps_second)
print()
# Define the variables
target_steps = 100000
steps_hourly = target_steps / 24
steps_minute = steps_hourly / 60
steps_second = steps_minute / 60
print("Daily steps:", target_steps)
print("Per hour:", steps_hourly)
print("Per minute:", steps_minute)
print("Per second:", steps_second)
print()
# Define the variables
target_steps = 200000
steps_hourly = target_steps / 24
steps_minute = steps_hourly / 60
steps_second = steps_minute / 60
print("Daily steps:", target_steps)
print("Per hour:", steps_hourly)
print("Per minute:", steps_minute)
print("Per second:", steps_second)
print()

# Question 3
print("*** Question 3: Calculate the miles walked in a single week ***")
# Define the variables
pi = 3.14
# Source of circumference equation: https://www.google.com/search?q=circumference+equation&rlz=1C5CHFA_enUS869US871&oq=cir&aqs=chrome.0.69i59j69i57j0j46j0l4.911j0j4&sourceid=chrome&ie=UTF-8
irr_circum = 2 * pi * 400
# print(irr_circum)
amt_systems = 4
amt_inspect = 2
daily_distance = irr_circum * amt_systems * amt_inspect
# print(daily_distance)
weekly_ft_distance = daily_distance * 6
weekly_ft_distance = round(weekly_ft_distance, 2)
print("Weekly distance (ft):", weekly_ft_distance)
weekly_distance = weekly_ft_distance / 5280
weekly_distance = round(weekly_distance, 2)
print("Weekly distance (miles):", weekly_distance)
