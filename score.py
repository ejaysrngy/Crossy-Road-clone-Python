from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 220)
        self.score = 1
        self.write(f"Level {self.score}", align="left", font=("Arial", 15))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level {self.score}", align="left", font=("Arial", 15))

    def you_lose(self):
        self.goto(0, 0)
        self.write(f"YOU SUCK", align="center", font=("Courier", 30))
        self.goto(0,-10)
        self.write(f"Best run: level {self.score}", align="center")