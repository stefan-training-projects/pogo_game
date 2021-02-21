from turtle import Screen
from paddle import Paddle
from ball import Ball

#screen details
screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title("Fun With POGO")
screen.tracer(0)

#objects
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()


# paddle key commands
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on = True

while game_is_on:
    screen.update()
        ball.move()








screen.exitonclick()