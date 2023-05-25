import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.setup(width=600, height=600)
screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if player.distance(car) < 22:
            score_board.game_over()
            game_is_on = False

    # Detect turtle reach the other side
    if player.ycor() > 280:
        score_board.update()
        car_manager.next_level()
        player.next_level()
screen.exitonclick()
