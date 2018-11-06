# fractalbranch.py
# Author: Daniel Ritchie
# Last Update: 11/5/2018

import turtle

def drawBranch(n, turt, length):
    turt.left(45)
    turt.fd(length)
    if (n > 0):
        drawBranch(n-1, turt, length/2)
    turt.left(180)
    turt.fd(length)
    turt.left(90)
    turt.fd(length)
    if (n > 0):
        drawBranch(n-1, turt, length/2)
    turt.left(180)
    turt.fd(length)
    turt.right(135)

iterNum = int(input("Number of iterations: "))
t = turtle.Turtle()
t.speed(0)
length = 200
t.penup()
t.left(90)
t.bk(length)
t.pendown()
t.fd(length)
drawBranch(iterNum, t, length/2)
