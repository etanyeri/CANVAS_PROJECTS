
""" This program will have Tracy draw a row of circles 
across the canvas."""

penup()       #first command penup() to stop draw the lines
backward(190) 

for i in range(20):
    pendown()
    circle(10)  #Each circle should have a radius of 10 pixels.
    penup()     #There will be 20 circles along the x-axis
    forward(20)