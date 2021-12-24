

""" This program will draw a pyramid of circles with 3 circles
on the bottom row, 2 on the middle row, and 1 on the top."""


speed(9)
penup()
setposition(-100,-200)
pendown()
for i in range(3): # make Tracy complete this 3 times
    circle(50)  # Circle's radius should be 50 pixel.
    penup()
    forward(100)
    pendown()
penup()
setposition(0,0)
pendown()
circle(50)
penup()
setposition(-50,-100)
pendown()
for i in range(2): #complete the middle 2 circles at last.
    circle(50)
    penup()
    forward(100)
    pendown()
penup()
setposition(0,0)
# Tracy needs to go to the main position after commands.