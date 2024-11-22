import math

"""
imports math so that the program can access mathematical functions
"""

def area_of_rectangle(length, width):
    return length * width
"""Multiplies the length and the width of a rectangle and returns the result
Args:
    length: the first sumand.
    width: the second summand.
Returns:
    The result of the length and the width(area of rectangle).
"""

def area_of_triangle(base, height):
    return 0.5 * base * height
"""Multiplies 0.5 times the base times the height and returns the result
Args:
    0.5: decimal
    base: the first summand.
    height: the second summand.
Returns:
    The result of 0.5 * base * height(area of triangle).
"""

def area_of_circle(radius):
    return math.pi * (radius ** 2)
"""Multiplies the radius times 2 and returns the result
Args:
    radius: the first summand.
    2: the number
Returns:
    The result of radius times 2 (area of circle).
"""

def main():
    print("Area Calculator!")
    print("Choose a shape and calculate the area:")
    print("1.) Rectangle")
    print("2.) Triangle")
    print("3.) Circle") 
    
    choice = input("Enter your choice 1,2,3")
    
"""Menu displayed and ask input from user
Returns:
    Displays the title and ask the user what shape they want to calculate.
"""