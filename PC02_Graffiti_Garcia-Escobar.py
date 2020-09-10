#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use



# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

Turtle()

up()
goto(110,-90)
right(5)

down()
width(18)
color("red")
forward(250)

width(10)
color("white")
backward(240)

up()
home()
goto(-15,110)
down()
color("blue")
circle(1)
right(20)
width(10)
forward(400)
color("white")
width(2)
backward(390)

up()

home()
goto(325,0)
color("yellow")
down()
width(20)
right(90)
forward(220)
right(90)
backward(40)
right(90)
forward(220)
left(90)
forward(40)
backward(20)
left(90)
forward(220)
up()

home()
color("black")
goto(315,0)
left(180)
down()
color("orange")
width(25)
circle(10,180)
up()
goto(315,-95)
left(180)
down()
circle(10,180)
up()
home()
#clear()