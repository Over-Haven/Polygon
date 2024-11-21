import turtle #import
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,300)
polygon = turtle.Turtle() #defined

num_sides = 6
side_length = 70
angle = 360.0/ num_sides
#loop
for i in range(num_sides) :
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()