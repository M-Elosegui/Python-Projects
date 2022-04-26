from turtle import Turtle
import random
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
speed = 20


     #######################################################################
            ###################   SNAKE  ######################

class Snake:
    def __init__(self):
        self.segmentos = []
        self.criarSnake()
        self.head = self.segmentos[0]


    def criarSnake(self):
        for posicao in INITIAL_POSITIONS:
            self.add_segment(posicao)


    def add_segment(self,position):
        segmento = Turtle("square")
        segmento.color("white")
        segmento.penup()
        segmento.goto(position)
        self.segmentos.append(segmento)

    def extend(self):
        self.add_segment(self.segmentos[-1].position())

    def move(self):
        for seg_num in range(len(self.segmentos) -1, 0, -1):
            new_x = self.segmentos[seg_num -1].xcor()
            new_y = self.segmentos[seg_num -1].ycor()
            self.segmentos[seg_num].goto(new_x,new_y)
        self.head.forward(speed)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def reset(self):
        for seg in self.segmentos:
            seg.goto(1000,1000)

        self.segmentos.clear()
        self.criarSnake()
        self.head = self.segmentos[0]

    #######################################################################
            ###################   FOOD  ######################



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-360, 360)
        random_y = random.randint(-360, 360)
        self.goto(random_x, random_y)
        #######################################################################
            ###################   SCORE  ######################

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0,360)
        self.color("white")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))
        self.goto(0,0)

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", "w") as file:
                 file.write(str(self.score))
            with open("data.txt", "r") as file:
               self.highscore = int(file.read())

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}    HIGH SCORE: {self.highscore} ", align="center", font=("Arial", 24, "normal"))


################
"""
escreveria no main:
file = open("my_text.txt")
contents = file.read()
print(contents)
file.close()

melhor maneira:
with open("my_text.txt") as file:
    contents = file.read()
    print(contents)


para escrever:
with open("my_text.txt", mode="w") as file:
file.write("my text")

mas assim ele escreve por cima, por isso queremos mode="a" ( add )
with open("my_text.txt", mode="a") as file:
file.write("\n my text")
assim ele adiciona, sem apagar

"""
