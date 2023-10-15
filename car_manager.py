from turtle import Turtle

COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()

    def create_car(self, position):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.sety(position)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
