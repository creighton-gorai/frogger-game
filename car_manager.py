from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setx(300)
        self.sety(position)

    def move(self, level):
        self.forward(-1 * (STARTING_MOVE_DISTANCE + MOVE_INCREMENT * level))
