"""
Project Name: Turtle Patterns
Author: Cody Behling
Due Date: 10/03/2020
Course: CS1400-X01

This program will ask for two inputs from a user to determine the width and height of the turtle window.
Users should put in the dimensions of 500 x 500 in order to see the picture in a decent size.
It will then use those dimensions to display the window and draw a picture using turtle commands.
The picture will be of a landscape, containing two of each: rectangle, triangle, circle
The shapes will consist of different colors, sizes, and angles making up the land, sky, mountains, sun, and lake.
"""

import turtle

# user inputs
def getWidth():
    width = input("Enter the turtle window's width: ")
    return width
def getHeight():
    height = input("Enter the turtle window's height: ")
    return height

# validate inputs
def validateNumber(userInput):
    try:
        userInput = int(userInput)
        return True
    except:
        return False

# rectangle code
def rectangle(cody, width, height, tilt, tiltDirection, borderColor, fillColor):
    if tiltDirection == 'left':
        cody.left(tilt)
    elif tiltDirection == 'right':
        cody.right(tilt)
    cody.pencolor(borderColor)
    cody.fillcolor(fillColor)
    cody.begin_fill()
    sides = 4
    for i in range(0, sides):
        if(i + 1) % 2 == 0:
            cody.forward(height/2)
            cody.left(90)
        else:
            cody.forward(width)
            cody.left(90)
    cody.end_fill()
    if tiltDirection == 'left':
        cody.right(tilt)
    elif tiltDirection == 'right':
        cody.left(tilt)

# triangle code
def triangle(cody, sideLength, tilt, tiltDirection, borderColor, fillColor):
    if tiltDirection == 'left':
        cody.left(tilt)
    elif tiltDirection == 'right':
        cody.right(tilt)
    cody.pencolor(borderColor)
    cody.fillcolor(fillColor)
    cody.begin_fill()
    sides = 3
    for i in range(0, sides):
        cody.forward(sideLength)
        cody.left(120)
    cody.end_fill()
    if tiltDirection == 'left':
        cody.right(tilt)
    elif tiltDirection == 'right':
        cody.left(tilt)

# circle code
def circle(cody, radius, borderColor, fillColor):
    cody.pencolor(borderColor)
    cody.fillcolor(fillColor)
    cody.begin_fill()
    cody.circle(radius)
    cody.end_fill()

# allows the turtle to move to another location without drawing a line to get there
def goto(cody, x, y):
    cody.penup()
    cody.goto(x, y)
    cody.pendown()

def main():

    try:
        # turtle setup
        turtleScreen = turtle.Screen()
        cody = turtle.Turtle()

        width = int(getWidth())
        height = int(getHeight())

    except ValueError:
        print("Enter positive integers for width and height.")
        return
    if width < 1 or height < 1:
        print("Enter positive integers for width and height.")
        return

    turtleScreen.setup(width + 30, height + 30)

    maxWidth = width / 2
    maxHeight = height / 2

    # sky
    goto(cody, (maxWidth * -1), 0)
    rectangle(cody, width, height, 1, 'right', 'darkblue', 'skyblue')

    # land
    goto(cody, (maxWidth * -1), (maxHeight * -1))
    rectangle(cody, width, height, 1, 'left', 'darkgreen', 'lightgreen')

    # first mountain
    goto(cody, (maxWidth / 2 * -1), 0)
    triangle(cody, (maxWidth / 2), 1.5, 'left', 'black', 'slategrey')

    # second mountain
    goto(cody, 0, 0)
    triangle(cody, (maxWidth / 2), 1.5, 'right', 'darkslategrey', 'lightslategrey')

    # sun
    goto(cody, (maxWidth - ((maxWidth / 10) * 2)) * -1, (maxHeight - ((maxHeight / 10) * 3)))
    circle(cody, (maxWidth / 10), 'red', 'yellow')

    # lake
    goto(cody, 0, ((maxWidth / 1.25) * -1))
    circle(cody, (maxWidth / 3), 'blue', 'steelblue')

    print("To exit the program, please click on the screen.")
    turtleScreen.exitonclick()

if __name__ == "__main__":
    main()
