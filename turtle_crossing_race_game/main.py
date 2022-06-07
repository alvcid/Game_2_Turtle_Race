import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkeypress(player.move, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.car()
    car_manager.move()

    # Collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Winning car
    if player.win():
        player.reset_player()
        scoreboard.up_level()
        car_manager.increase_speed()


screen.exitonclick()