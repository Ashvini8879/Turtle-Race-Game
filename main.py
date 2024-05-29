import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(player.move_turtle,"Up")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    
    #Detect the collision with car

    for car in car_manager.all_cars:
        if car.distance(player) <20:
            game_is_on = False
            scoreboard.Game_over()

    #Detect when the player has reached the other side

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()




screen.exitonclick()