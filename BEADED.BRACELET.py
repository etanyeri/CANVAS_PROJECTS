
"""This program will draw one beaded bracelet 
that must have a diameter of 200 pixels"""

speed(3)
def make_circle_beads():
    for i in range(36): #there must be 36 beads.
        left(10)        #needs to turn 10 degrees after drawing each bead
        forward(100)
        pendown()
        circle(10)   #each beed must have a radius of 10 pixels
        penup()
        backward(100)
penup()

make_circle_beads()

setposition(0,0)