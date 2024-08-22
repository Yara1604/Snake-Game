import turtle
ALIGNMENT= "center"
FONT= ('Fixedsys',18,'normal')


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.update_score()

    def update_score(self):
        self.write(f"SCORE: {self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)
        self.goto(0,-20)
        self.write("Press 'r' to restart",align=ALIGNMENT,font=FONT)

    def restart(self):
        self.reset()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.update_score()
