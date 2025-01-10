"""This program uses python's turtle module to draw a spyrograph of circles with a radius of 100 units.
by JBAmenorfe on 8th January 2025"""
import turtle
# Import necessary modules
from turtle import Turtle, Screen
import random

# Define a function to return rgb colors
def random_color():
    """Returns random rgb colors"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb = (r,g,b)
    return rgb

# Create a turtle object called tom
def draw_spyrograph(gap):
    """Draws a spyrogram using the gap provided"""
    tom = Turtle()
    number_of_circles = int(360/gap)
    for step in range(number_of_circles):
        tom.circle(100)
        tom.color(random_color())
        tom.left(gap)

# Change the colormode of the turtle module
turtle.colormode(255)

# Create screen object
screen = Screen()
screen.screensize(canvwidth=600, canvheight=600, bg="wheat")

# Call the draw_spyrograph function
draw_spyrograph(10)

# Call the exitonclick method
screen.exitonclick()
