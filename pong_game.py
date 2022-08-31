from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
ball.home()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
        time.sleep(ball.move_speed)
        ball.move()
        screen.update()
        
# Hitting the wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()
            
# Hitting the paddles
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
            ball.horiz_bounce()
            ball.move_speed *= 0.9
        if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.horiz_bounce()
            ball.move_speed *= 0.9
            
# Return the ball to the original position in case of a miss
        if ball.xcor() > 380:
            ball.home()
            ball.horiz_bounce()
            scoreboard.l_point()
            ball.move_speed = 0.1
        if ball.xcor() < -380:
            ball.home()
            ball.horiz_bounce()
            scoreboard.r_point()
            ball.move_speed = 0.1



screen.exitonclick()
