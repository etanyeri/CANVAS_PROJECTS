


""" This program will represent a popular kid’s toy that teaches
them about different shapes and colors."""

penup()
setposition(-60,60)
pendown()
color('red')   #a red square
begin_fill()
circle(60,360,4)   #You should use only the circle() 
end_fill().        #command to create all shapes. 
penup()
setposition(100,60)
pendown()
color('blue')   #a blue circle
begin_fill()
circle(60)
end_fill()
penup()
setposition(100,-100)
pendown()
color('green')   #a green pentagon
begin_fill()
circle(60,350,5)
end_fill()
penup()
setposition(-60,-80)
pendown()
color('yellow')  #a yellow semicircle
begin_fill()
circle(60,180)
end_fill()