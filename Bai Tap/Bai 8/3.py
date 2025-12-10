import turtle, random

colors = ["red", "green", "blue"]

painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0)

for i in range(12):
    painter.pencolor(colors[i % 3])  
    painter.circle(100)
    painter.left(30)                

turtle.done()
