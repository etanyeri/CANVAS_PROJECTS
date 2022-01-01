

"""This code will draw a sidewalk around 
the perimeter of the canvas."""


speed(0)
def squarerow():
 for i in range(8):  #8 squares along each side of the canvas
  for i in range(4):
    pendown()
    forward(50)
    left(90)
  forward(50)

penup()
setposition(-200,-200) #will start from left bottom corner

squarerow()

penup()
setposition(-200,150)

squarerow()

setposition(-200,150)
right(90)
squarerow()

penup()
setposition(200,-150)
left(180)
squarerow()