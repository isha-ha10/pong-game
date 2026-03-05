# pong-game
A simple Pong game component built using Python’s turtle module. This project implements the ball mechanics for a classic Pong game including movement, bouncing, restarting, and speed increase.
Features
1.Ball movement across the screen
2.Bounce on X-axis (paddles)
3.Bounce on Y-axis (top and bottom walls)
4.Restart ball position after scoring
5.Ball speed increases during gameplay

Requirements
Python 3.x
turtle module (comes pre-installed with Python)

Code Overview
1.Ball Class
The Ball class inherits from Turtle and controls the behavior of the Pong ball.
->Sets the ball shape to a circle
->Colors the ball white
->Sets movement speed values
2.Movement
Moves the ball by updating its x and y coordinates.
3.Bounce on Walls
Reverses vertical movement when the ball hits the top or bottom wall.
4.Bounce on Paddles
Reverses horizontal movement when the ball hits a paddle.
5.Restart Ball
->Moves the ball back to the center (0,0)
->Reverses its direction
6.Increase Speed
Increases the speed of the ball during gameplay.

Future Improvements

->Add paddle controls
->Implement scoreboard
->Add collision detection with paddles
->Improve ball speed logic
