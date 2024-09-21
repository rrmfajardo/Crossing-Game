from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(x=-230, y=270)
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", font=FONT, align="center")

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER!", align="center", font=FONT)
