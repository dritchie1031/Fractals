# fractaltriangle.py
# Author: Daniel Ritchie
# Last Update: 11/5/2018

import turtle

def drawTriangle(n, turt, length):
    turt.left(120)
    # Loops through three times: once for each side
    # Drawing a side, and if n>0, going another layer into the fractal
    for i in range(0,3):
        # Only going halfway, continuing the other half after possible recursion
        turt.fd(length/2)
        if (n > 0):
            drawTriangle(n-1, turt, length/2)
        turt.fd(length/2)
        turt.right(120)
    # This left turn counteracts the last right turn in the above loop, and returns the
    # turtle to the same direction it was going before the function was called
    turt.left(240)

iternum = int(input("Enter the number of iterations you would like to do: "))
# You can make the length an input as well, but I didn't because it fits nicely
# on the page this way
length = 500
# The drawing goes REALLY slow if you don't have it at max speed
spd = int(input("Enter the speed of the turtle: "))

t = turtle.Turtle()
t.speed(spd)

# Moving the starting point of the turtle so that the center of the triangle is the
# center of the turtle screen
t.penup()
t.left(180)
t.fd(length/2)
t.left(90)
triHeight = (((length**2)-((length/2)**2))**(1/2))/2 # there's probably a better way to do this
t.fd(triHeight)
t.left(90)
t.pendown()

# Manually drawing the outermost triangle because I haven't been able to figure out how
# to do it otherwise. Possible updates to come. 
t.fd(length/2)
drawTriangle(iternum-1, t, length/2)
t.fd(length/2)
t.left(120)
t.fd(length)
t.left(120)
t.fd(length)

input("Press enter to exit")
