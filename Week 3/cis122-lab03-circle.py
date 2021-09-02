'''
CIS 122 Summer 2020 Lab 3
Author: Morgan Bartlett
Credit:
Description: Create some amount of concentric circles using turtle graphics
'''
# Import Turtle graphics module and create a turtle for drawing
import turtle
morla = turtle.Turtle()

def move(t, x, y):
   """
   Move Turtle to x, y position
   """
   t.pu()
   t.goto(x, y)
   t.pd()

def draw_circle(t, radius, x, y):
   """
   Draw a circle of length radius using Turtle t at position x, y
   """
   t.pu()
   t.goto(x, y)
   t.pd()
   move(t, x, y - radius)
   t.circle(radius)

def draw_concentric_circles(n, radius, gap_size, x, y):
    '''
    Draw many circles given n, of length radius and gap_size between circles
    at position x, y
    '''
    start_size = 0;
    for i in range(n):
        # changed t to morla because I was getting the NameError: t is not defined
        draw_circle(morla, start_size + radius, x, y)
        start_size = start_size + gap_size
       
draw_concentric_circles(3, 50, 25, 0, 0)


