from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("coral")
        self.goto(-280, 260)
        self.score = 1
        self.write(arg=f"Level: {self.score}", font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(-80, 0)
        self.write(arg="GAME OVER", font=FONT)
