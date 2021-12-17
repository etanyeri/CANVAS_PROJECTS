""" This program is to let Tracy draw lines by splitting 
the canvas into 4 equal column"""

penup()    #First let Tracy go to the first position.
left(90)
forward(200)
left(180)
pendown()
for i in range(2): #these below moves will repeat 2 times
    forward(400)
    penup()
    right(90)
    forward(100)
    right(90)
    pendown()
    forward(400)
    penup()
    right(90)
    forward(200)
    right(90)
    pendown()
    forward(400)
    
# OR

penup()
left(90)
forward(200)
left(180)
pendown()
forward(400)
penup()
right(90)
forward(100)
right(90)
pendown()
forward(400)
penup()
right(90)
forward(200)
right(90)
pendown()
forward(400)


#OR

penup()
right(90)
forward(200)
right(90)
forward(100)
right(90)
for i in range(2):
    pendown()
    forward(400)
    penup()
    right(90)
    forward(100)
    pendown()
    right(90)
penup()
right(90)
forward(200)
pendown()
left(90)
forward(400)