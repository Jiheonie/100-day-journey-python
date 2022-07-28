from turtle import Turtle, Screen

my_tur = Turtle()

def move_forward():
    my_tur.forward(20)

def move_backward():
    my_tur.backward(20)

def turn_left():
    my_tur.setheading(my_tur.heading() + 10)

def turn_right():
    my_tur.setheading(my_tur.heading() - 10)


screen = Screen() 
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")



screen.exitonclick()