from turtle import Turtle
import random as r


class Cars():
    def __init__(self, y_coord, speed):
        self.car_group = []
        self.y_coord = y_coord
        self.speed = speed

    # make a car "snake" that'll move along the grid with varying random spaces
    def make_cars(self):
        """ this will create a car 'snake' with a number of cars, min is 2, max is 4, depending
        on the segmentation d/t randomization"""
        x_coord = 350
        x_coord_rand = 350
        for i in range(7):
            for j in range(2):
                car = Turtle("square")
                car.setheading(180)
                car.penup()
                car.goto(x_coord, self.y_coord)
                car.color("black")
                x_coord += 20
                self.car_group.append(car)
            x_coord = r.randrange(x_coord_rand, 1000)
            x_coord_rand += 90

    def move_cars(self):
        for i in self.car_group:
            i.forward(self.speed)

    def repeat(self):
        if self.car_group[-2].xcor() < -400:
            self.car_group.clear()
            self.make_cars()
            self.move_cars()
        else:
            self.move_cars()
