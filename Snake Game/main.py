# This is a sample Python script.

from turtle import Turtle, Screen

"""

tim = Turtle()
screen = Screen()

def frente():
    tim.forward(10)

def tras():
    tim.backward(10)

def esquerda():
    nova_direcao = tim.heading() + 45
    tim.setheading(nova_direcao)

def direita():
    nova_direcao = tim.heading() - 45
    tim.setheading(nova_direcao)

def limpar():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

######################


screen.listen()
screen.onkey(frente,"w")
screen.onkey(tras,"s")
screen.onkey(esquerda,"a")
screen.onkey(direita,"d")
screen.onkey(limpar,"c")

screen.exitonclick()

"""

from snake import Snake
from snake import Food
from snake import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Jogar ao snaki snaki!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


contador = 1
game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    #### CABEÇA COMER MAÇA

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    #### HIT SIDES

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        scoreboard.reset()
        snake.reset()


    #### HEAD HITTING THE BODY

    for segmento in snake.segmentos:
        if segmento == snake.head:
            pass
        elif snake.head.distance(segmento) < 9:
            scoreboard.reset()
            snake.reset()



    print(snake.head.position())
