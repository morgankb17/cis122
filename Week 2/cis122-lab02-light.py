'''
CIS 122 Summer 2020 Lab 2
Author: Morgan Bartlett
Partner:
Description: Create a function that calculates the average amount of time in seconds light will
take to reach the surface of the Earth and Pluto
'''

# Define the fruitful function
def avg_light_travel_seconds(distance_miles):
    # Declare variables
    light_speed = 186282
    
    # Calculate the time it takes for light to reach each planet
    avg_light_travel_seconds = distance_miles / light_speed

    # Return results
    return avg_light_travel_seconds
    

# Define the void function
def print_results(planetary_object, avg_light_travel_seconds):
    print("Light travels from the sun to", planetary_object, "an average of", round(avg_light_travel_seconds, 2),"seconds.")

    
    
    
