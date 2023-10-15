import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.title("Frogger")
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = []

screen.listen()
screen.onkeypress(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Allow car to be created randomly

    # Check if player got to the other side of the screen
    turtle.crossed_finish_line()
    # Check to see if the player was hit by a car
