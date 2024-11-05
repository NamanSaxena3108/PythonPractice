from turtle import Turtle
import random

tim=Turtle()

color=['CornflowerBlue','DarkOrchid','IndianRed','DeepSkyBlue','LightSeaGreen','wheat','SlateGray','SeaGreen']

def draw_shapes(num_sides):
    for _ in  range(num_sides):
        angles=360/num_sides
        tim.forward(100)
        tim.right(angles)
        
for shape_side_n in range(3,11):
    tim.color(random.choice(color))
    draw_shapes(shape_side_n)