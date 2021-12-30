

"""
This code will fill the canvas with light blue circles."""

speed(0)

# This function will draw one row of 10 circles
def draw_circle_row():
    for i in range(10):
        pendown()
        begin_fill()
        color("light blue")
        circle(20)
        end_fill()
        penup()
        forward(40)

# This function will move Tracy from end of row up to beginning of the row on top        
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)
    
    
    
    
# Send Tracy to starting position in bottom left corner
penup()
setposition(-180,-200)

# Call circle drawing function 10 times to fill ten rows
for i in range(10):
    draw_circle_row()
    move_up_a_row()
  
  
  
  
    
 
"""
Now add a function that will draw a white highlight on each bubble.
"""

 
#This function called make_highlight that will draw a 
#white quarter-circle with a radius of 10

def make_highlight():
    left(90)
    pendown()
    color('white')
    begin_fill()
    circle(10,90)
    end_fill()



## this function makes sure that highlight is being drawn 
# in the correct location
def move_right():
    penup()
    left(90)
    forward(10)
    left(90)
    forward(50)
    
    
       
    
penup()
setposition(-170,-180)

def one_row_highlight():
    for i in range(10):
        make_highlight()
        move_right()
        
for i in range(10):     
    one_row_highlight()
    move_up_a_row()