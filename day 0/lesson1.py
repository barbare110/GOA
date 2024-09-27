from turtle import *

#we want to paint a house

#step 1: draw a square
speed(5)
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draw windows
penup()
goto(160,160)
pendown()

color("blue")
right(60)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(93)
forward(25)
#draw another window
penup()
goto(77,160)
pendown()
 
left(85)
forward(40)
left(90)
forward(30)
left(90)
forward(45)
left(90)
forward(25)

exitonclick()