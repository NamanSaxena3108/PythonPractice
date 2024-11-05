from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)

screen.listen()  #it is used to interact with the turtle screen
screen.onkey(key="space",fun=move_forward)   #it takes 2 argument first is the key to be pressed and second is the function to perform 
screen.exitonclick()