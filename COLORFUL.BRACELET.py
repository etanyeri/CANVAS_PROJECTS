

""" This code is to draw the bracelet with colored beads."""

speed(0)
def colorful_beads():
    for i in range(12): # A for loop will help shorten 
        left(10)
        forward(100)
        pendown()
        color('red') #Alternate between blue, red, and purple
        begin_fill()
        circle(10)
        end_fill()
        penup()
        backward(100)
        left(10)
        forward(100)
        pendown()
        color('purple')
        begin_fill()
        circle(10)
        end_fill()
        penup()
        backward(100)
        left(10)
        forward(100)
        pendown()
        color('blue')
        begin_fill()
        circle(10)
        end_fill()
        penup()
        backward(100)
penup()
colorful_beads()