from turtle import Turtle



pos = [40, 20, 0, -20, -40]


class Bar:

    def __init__(self):
        self.right_paddle = Turtle(shape="square")
        self.left_paddle=Turtle(shape="square")
        self.create_right_bar()
        self.create_left_bar()

    def create_right_bar(self):
        self.right_paddle.color("white")
        self.right_paddle.speed("fastest")
        self.right_paddle.penup()
        self.right_paddle.shapesize(stretch_len=1,stretch_wid=5)
        self.right_paddle.goto(x=350, y=0)

    def move_right_bar_up(self):
        y_cor=self.right_paddle.ycor()
        x_cor=self.right_paddle.xcor()
        self.right_paddle.goto(x=x_cor,y=y_cor+20)

    def move_right_bar_down(self):
        y_cor = self.right_paddle.ycor()
        x_cor = self.right_paddle.xcor()
        self.right_paddle.goto(x=x_cor, y=y_cor - 20)

    def move_left_bar_up(self):
        y_cor = self.left_paddle.ycor()
        x_cor = self.left_paddle.xcor()
        self.left_paddle.goto(x=x_cor, y=y_cor + 20)
    def move_left_bar_down(self):
        y_cor = self.left_paddle.ycor()
        x_cor = self.left_paddle.xcor()
        self.left_paddle.goto(x=x_cor, y=y_cor - 20)

    def create_left_bar(self):
        self.left_paddle.color("white")
        self.left_paddle.speed("fastest")
        self.left_paddle.penup()
        self.left_paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.left_paddle.goto(x=-350, y=0)


