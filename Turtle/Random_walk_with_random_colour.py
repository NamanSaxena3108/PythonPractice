import turtle as t
import random

tim=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colo=(r,g,b)
    return random_colo

direction=[0,90,180,270]
tim.pensize(15)
tim.speed("fast")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))