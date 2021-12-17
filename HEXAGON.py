"""This program will have Tracy draw a hexagon. Hexagon has 6 points
that needs to be 60 degrees in each angle. When giving a command to 
right or left, it should be based on this angle"""


speed(9)

for i in range(6):

    forward(50)  #each side of hexagon will have 50 pixels long.
    left(60)