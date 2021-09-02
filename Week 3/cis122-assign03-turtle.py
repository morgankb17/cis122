'''
CIS 122 Summer 2020 Assignment 3
Author: Morgan Bartlett
Credit:
Description: Create a function that uses Turtle graphics to create radial lines
'''
import turtle
alpha = turtle.Turtle()

def draw_line(t, x, y, angle, length):
    """
    Draw a line given coordinates, a heading, and a desired line length. Turtule ends
    with pen lifted up.

    Args:
       t (Turtle): Drawing Turtle
       x (int/float): starting x location
       y (int/float): starting y location
       angle (int/float): heading the turtle should draw the line
       length (int/float): how long the line should be

   Returns:
      None
    """
    t.pu()
    t.goto(x,y)
    t.pd()
    t.seth(angle)
    t.fd(length)
    t.pu()

def draw_radial_lines(t, x, y, length, num_lines):
    '''
    Draw a given amount of radial lines at a certain x,y coordinate and desired length of each line.
    Uses a for loop to draw out each line.

    Args:
       t (Turtle): Drawing Turtle
       x (int/float): starting x location
       y (int/float): starting y location
       length (int/float): how long the line should be
       num_lines (int): how many lines should originate from the x,y coordinate

   Returns:
      None
    '''
    for i in range(num_lines):
        draw_line(t, x, y, i*360/num_lines, length)
   
def draw_radials_in_quadrants(t, length, num_lines):
    '''
    Draw four radial lines in separate quadrants on the plane using the length to both determine
    line length and how far each radial is from each other.

    Args:
        t (Turtle): Drawing Turtle
        length (int/float): how long the line should be, where radial should be on the plane, and
        how separate the radials are from each other
        num_lines (int): how many lines should originate from the origin of the radial

    Returns:
        None
    '''
    t.pu()
    t.setx(length) # Set x for Quandrant 1
    t.sety(length) # Set y for Quadrant 1
    draw_radial_lines(t, length, length, length, num_lines) # Quandrant 1, +,+
    t.setx(length-(length*4)) # Move to Quadrant 2
    draw_radial_lines(t, (length-(length*4)), length, length, num_lines) # Quandrant 2, -,+
    t.sety(length-(length*4)) # Move to Quandrant 3
    draw_radial_lines(t, (length-(length*4)), (length-(length*4)), length, num_lines) # Quandrant 3, -,-
    t.setx(length) # Move to Quadrant 4
    draw_radial_lines(t, length, (length-(length*4)), length, num_lines) # Quandrant 4, +,-




# draw_line(alpha, 100, 100, 0, 200)
# draw_line(alpha, -100, -100, 270, 50)
# draw_line(alpha, 200, -200, 45, 75)

# draw_radial_lines(alpha, -100, -100, 25, 8)
# draw_radial_lines(alpha, -100, 100, 100, 4)
# draw_radial_lines(alpha, 100, -100, 200, 16)
# draw_radial_lines(alpha, 100, 100, 50, 32)

draw_radials_in_quadrants(alpha, 75, 8)
# draw_radials_in_quadrants(alpha, 50, 16)

