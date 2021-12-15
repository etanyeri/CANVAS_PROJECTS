""" The program is to draw a dashed line across on the x-axis.
Entire canvas is 400-400 pixell width-length"""

penup()
backward(200)
for i in range(4):   #we want the same moves 4 times
    pendown()
    forward(50)
    penup()
    forward(50)

#OR


penup()         # first moves start with a command that called (penup).
backward(200)   # whick makes the moves without a line.
pendown()
forward(50)
penup()    
forward(50)
pendown()       #to bring the drawing line give command of (pendown)
forward(50)
penup()
forward(50)     #Space between lines and 'lines' themselves are 50 pixels
pendown()
forward(50)
penup()
forward(50)
pendown()
forward(50)
penup()
forward(50)