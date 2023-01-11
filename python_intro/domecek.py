from turtle import forward, right, left
from turtle import exitonclick, shape, penup, pendown
from math import sqrt
from random import randint

# pep8 - standard pro psaní py

def draw_case(a):
    koeficientVyskyKominku = 0.15
    
    c = sqrt(2*a**2)
    left(90)
    forward(a)
    right(90)
    forward(a)
    left(135)
    forward(c/2)
    left(90)
    # komínek - střecha
    forward(c/8)
    right(135)
    # komínek nalevo
    forward(a*koeficientVyskyKominku)
    left(90)
    # horní část komínku
    forward(a/8)
    left(90)
    # dolní část komínku
    forward(a*koeficientVyskyKominku + sqrt((c**2)/64-(a**2)/64))
    right(45)
    forward(3*a/8)

    left(90)
    forward(c)
    left(135)
    forward(a)
    left(135)
    forward(c)
    left(135)
    forward(a)

uhel = 0
while uhel<360:
    draw_case(randint(30,60))
    rand = randint(10,25)
    uhel = uhel + rand
    right(rand)
exitonclick()