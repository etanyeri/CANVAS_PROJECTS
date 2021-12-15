"""Use the commands to draw a caterpillar on the canvas that are
400-400 pixel width and length."""

for i in range(5): #since body has 5 circles,ask the loop doing it 5 times.
    circle(20)
    penup()
    forward(40)
    pendown()
    
    #OR
    
circle(20)  #body has 5 circles and has a radius of 20 pxl
penup()     #make sure pen doesn't draw
forward(40) 
pendown()
circle(20)
penup()
forward(40)
pendown()
circle(20)
penup()
forward(40)
pendown()
circle(20)
penup()
forward(40)
pendown()
circle(20)
penup()
forward(40)