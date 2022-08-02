from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 24, 'normal')





class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # возьмем из файла data.txt последнюю запись, занесем ее в high_score:
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()  # убирает курсор с экрана
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}, High score = {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        # записываем в файл data.txt значение high_score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"Game Over", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

