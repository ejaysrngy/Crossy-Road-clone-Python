import random as r
import time
from turtle import Screen

from cars import Cars
from player import Player
from score import Score

# Crossy Road game
# 1. Make game area
#   1.1 try to randomize road and grass
# 2. Make turtle
#   2.1 make turtle move up down left and right

screen = Screen()

screen.setup(height=500, width=500)
screen.listen()

score = Score()

sleep_time = 0.089
not_game_over = True
while not_game_over:
    screen.tracer(0)
    player = Player()

    # movement for player
    screen.onkeypress(player.up, "w")
    screen.onkeypress(player.down, "s")
    screen.onkeypress(player.turn_left, "a")
    screen.onkeypress(player.turn_right, "d")

    # creates instances of the Cars class; with random "roads", and speeds

    cars = Cars(-180, r.randrange(10, 30, 5))
    cars2 = Cars(-130, r.randrange(5, 30, 5))
    cars3 = Cars(-80, r.randrange(10, 30, 5))
    cars4 = Cars(0, r.randrange(10, 30, 5))
    cars5 = Cars(50, r.randrange(10, 30, 5))
    cars6 = Cars(100, r.randrange(10, 30, 5))
    
    cars.make_cars()
    cars2.make_cars()
    cars3.make_cars()
    cars4.make_cars()
    cars5.make_cars()
    cars6.make_cars()

    screen.update()

    car_list = [cars.car_group,
                cars2.car_group,
                cars3.car_group,
                cars4.car_group,
                cars5.car_group,
                cars6.car_group
                ]

    game_on = True
    while game_on:

        time.sleep(0.1)
        screen.update()

        cars.repeat()
        cars2.repeat()
        cars3.repeat()
        cars4.repeat()
        cars5.repeat()
        cars6.repeat()


        #optimized the code, instead of multiple for loops; On^2
        for group_of_cars in car_list:
            for specific_car in group_of_cars:
                if player.distance(specific_car) < 5:
                    game_on = False
                    not_game_over = False
                    score.you_lose()

        # for i in cars.car_group:
        #     if player.distance(i) < 10:
        #         print('this')
        #         game_on = False
        #         not_game_over = False
        #         score.you_lose()
        #
        # for i in cars2.car_group:
        #     if player.distance(i) < 10:
        #         print('this')
        #         game_on = False
        #         not_game_over = False
        #         score.you_lose()
        #
        # for i in cars3.car_group:
        #     if player.distance(i) < 10:
        #         print('this')
        #         game_on = False
        #         not_game_over = False
        #         score.you_lose()
        #
        # for i in cars4.car_group:
        #     if player.distance(i) < 10:
        #         print('this')
        #         game_on = False
        #         not_game_over = False
        #         score.you_lose()
        #
        # for i in cars5.car_group:
        #     if player.distance(i) < 10:
        #         print('this')
        #         game_on = False
        #         not_game_over = False
        #         score.you_lose()
        #
        # for i in cars6.car_group:
        #     if player.distance(i) < 10:
        #         print('this')
        #         game_on = False
        #         not_game_over = False
        #         score.you_lose()

        if player.ycor() == 230:
            game_on = False
            player.goto(0, -220)
            for i in car_list:
                i.clear()

            screen.clear()
            score.increase_score()
            sleep_time -= 0.010
            print(sleep_time)

screen.exitonclick()
