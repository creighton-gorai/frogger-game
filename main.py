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
level = Scoreboard()
difficulty = 0

screen.listen()
screen.onkeypress(turtle.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Should car be created
    if random.randint(0, 5) == 1:
        cars.append(CarManager(random.randint(-250, 250)))

    # Move car
    for car in range(len(cars)):
        cars[car].move(difficulty)
        if cars[car].distance(turtle) < 30:
            game_is_on = False
            level.game_over()

    # Check if player got to the other side of the screen
    if turtle.crossed_finish_line():
        difficulty += 1
        level.update_scoreboard()

screen.exitonclick()
