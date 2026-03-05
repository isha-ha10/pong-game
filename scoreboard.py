from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score=0
        self.right_score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-100,250)
        self.write(f"Score={self.left_score}",font=("Arial",10,"normal"))

        self.goto(100, 250)
        self.write(f"Score={self.right_score}", font=("Arial", 10, "normal"))
    def increase_right(self):
        self.right_score+=1
        self.update_score()
    def increase_left(self):
        self.left_score+=1
        self.update_score()