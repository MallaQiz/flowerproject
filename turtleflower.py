from turtle import *
from colorsys import *
tracer(5)
width(2)

def square(x):
    for i in range(3):
        forward(x)
        left(90)
    forward(x)

n = 40
for i in range(35):
    color(hls_to_rgb(1-i/n, 1-i/n, 1))
    for j in range(4):
        square(30+(i*5))
        circle(30+(i*5))
hideturtle()
done()



