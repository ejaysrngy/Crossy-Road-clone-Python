from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto(0, -220)
        self.setheading(90)

    def up(self):
        if self.heading() == 0 or self.heading() == 180:
            self.setheading(90)
        else:
            self.forward(10)

    def down(self):
        if self.heading() == 0 or self.heading() == 180:
            self.setheading(90)
        else:
            self.back(10)

    def turn_left(self):
        if self.heading() == 180:
            self.forward(10)
        else:
            self.left(90)

    def turn_right(self):
        if self.heading() == 0:
            self.forward(10)
        else:
            self.right(90)
