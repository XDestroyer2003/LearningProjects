import time
import turtle

colors = ['green', 'red', 'purple', 'blue', 'orange', 'yellow']
wn = turtle.Screen()
wn.bgcolor('black')
p = turtle.Turtle()
p.shape()
angle = 0
while True:
    p.setheading(0)
    for i in range(360):
        p.pencolor(colors[i % 6])
        p.width(i // 100 + 1)
        p.forward(i)
        p.left(59)
    angle += 12
    time.sleep(1)