
from turtle import Turtle, Screen





screen = Screen()
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.penup()
        self.goto(STARTING_POSITION)
        self.hideturtle()
        self.shape("turtle")
        self.shapesize(1)
        self.setheading(90)
        self.showturtle()


    def move(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def win(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

    def reset_player(self):
        self.goto(STARTING_POSITION)
