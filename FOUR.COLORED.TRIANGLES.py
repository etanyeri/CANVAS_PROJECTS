

""" This code is to raw four tri-colored triangles 
next to one another in the center of the canvas."""


penup()
setposition(-100,0) # take the starting position
pendown()
for i in range(4): # each time with 3 different colors 
    pensize(5)     # a triangle will be drawn by Tracy
    color('red')
    forward(50)
    left(120)
    color('blue')
    forward(50)
    left(120)
    color("green")
    forward(50)
    left(120)
    penup()
    forward(50)
    pendown()