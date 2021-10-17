'''Define a function drawCircle. This function should expect a Turtle object, the coordinates of the circle’s center point, 
and the circle’s radius as argu- ments. The function should draw the specified circle. The algorithm should draw the circle’s circumference by turning 3 degrees and moving a given distance 120 times. 
Calculate the distance moved with the formula 2.0 * p * radius / 120.0.'''

# import required header files:
import turtle

import math

def drawCircle(t, x, y, radius):

    distance = 2.0 * math.pi * radius / 120.0

    angle = 360 / 120

    t.penup()
    t.goto(x, y)
    t.right(90)
    t.forward(radius)
    t.left(90)
    t.pendown()
    for i in range (120):
        t.forward(distance)
        t.left(angle)

def main():
    x = int(input("Enter X : "))
    y = int(input("Enter Y : "))
    radius = int(input("Enter Radius : "))
    turtle.title('Circle')
    turtle.setup(300, 300, 0, 0)
    t = turtle.Turtle()
    t.color ('green')
    drawCircle (t, x, y,radius)
    turtle.done()
if __name__ == '__main__':
    main()