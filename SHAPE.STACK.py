

"""This codes will draw a stack of 
squares and circles from the bottom of the canvas to the top."""


def make_square():   #we need two different functions
    for i in range(4):
        pendown()
        forward(50) #Each shape should have a height and width of 50 pixels
        left(90)
def make_circle():
    pendown()
    circle(25)


penup()
setposition(-25,-200) #Shapes should be stacked in the center of the canvas
make_square()
penup()
setposition(0,-150)
make_circle()

penup()
setposition(-25,-100)
make_square()
penup()
setposition(0,-50)
make_circle()

penup()
setposition(-25,0)
make_square()
penup()
setposition(0,50)
make_circle()

penup()
setposition(-25,100)
make_square()
penup()
setposition(0,150)
make_circle()