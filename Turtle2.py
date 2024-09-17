import turtle
import colorsys

turtle.speed(0)
turtle.bgcolor("Black")
h=0
for i in range(16):
    for j in range(18):
        c=colorsys.hsv_to_rgb(h,1,1)
        turtle.color(c)
        h += 0.005
        turtle.rt(90)
        turtle.circle(150-j*6,90)
        turtle.lt(90)
        turtle.circle(150-j*6,90)
        turtle.rt(180)
    turtle.circle(40,24)
turtle.done()