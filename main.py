#create a screen
import time
from turtle import Screen
from paddle import Bar
from ball import Ball
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Welcome to the arcade game")

#create a  bar which can be controlled by wasd and up down keys
bar=Bar()
ball=Ball()
score=ScoreBoard()
screen.tracer(0)
screen.listen()
screen.onkey(bar.move_right_bar_up, "Up")
screen.onkey(bar.move_right_bar_down, "Down")
screen.onkey(bar.move_left_bar_up, "w")
screen.onkey(bar.move_left_bar_down, "s")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    # create a ball
    ball.move_ball()



    # detect collision of the ball with the wall and bounce
    if ball.ycor()>275 or ball.ycor()<-275:
        ball.bounce_y()
    # ensure the direction of the ball if it hits one of the bars
    if ball.distance(bar.right_paddle)<40 and ball.xcor()>340:
        ball.setx(340)
        ball.bounce_x()
    if  ball.distance(bar.left_paddle)<40 and ball.xcor()<-340:
        ball.setx(-340)
        ball.bounce_x()
    #detect right_paddle misses
    if ball.xcor()>380:
        ball.restart()
        # scoreboard of the left player
        score.increase_left()


    #detect left_paddle misses
    if ball.xcor() < -380:
        ball.restart()
        # scoreboard of the right player
        score.increase_right()




screen.exitonclick()

