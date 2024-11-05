from turtle import Turtle
import random

tim=Turtle()

color=['CornflowerBlue','DarkOrchid','IndianRed','DeepSkyBlue','LightSeaGreen','wheat','SlateGray','SeaGreen']
direction=[0,90,180,270]
tim.pensize(15)
tim.speed("fast")

for _ in range(200):
    tim.color(random.choice(color))
    tim.forward(30)
    tim.setheading(random.choice(direction))   #in this we are not using any left,right,up,down as it is difficult to implement so we use heading and the angles for the movement