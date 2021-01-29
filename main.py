############ animated race game ##################

from turtle import *
from random import randint

speed(0)
penup()
goto(-140,140)  #where we have to start from

for step in range(15):
    write(step,align="center")
    right(90)

    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

#desgining a player color, size and shape
player_1=Turtle()
player_1.color('red')
player_1.shape('turtle')


player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()


for turn in range(10):
    player_1.right(36)


player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')

player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()

for turn in range(60):
    player_2.right(6)


player_3 = Turtle()
player_3.color('green')
player_3.shape('turtle')

player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()

for turn in range(60):
    player_3.right(6)

for turn in range(100):
    player_1.forward(randint(1, 5))
    player_2.forward(randint(1, 5))
    player_3.forward(randint(1,5))
