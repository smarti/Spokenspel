# ----------------------------------------------------
# -                                                  -
# -                                                  -
# - Scroll naar beneden om het programma te zien     -
# -                                                  -
# -                                                  -
# ----------------------------------------------------

from turtle import *

def teken_a():
    left(60)
    forward(100)
    right(120)
    forward(50)
    right(120)
    forward(50)
    right(180)
    forward(50)
    right(60)
    forward(50)
    left(60)
    penup()
    forward(10)
    pendown()

def teken_b():
    left(90)
    forward(100)
    right(90)
    forward(20)
    circle(-25, 180, 30)
    forward(20)
    right(180)
    forward(20)
    circle(-25, 180, 30)
    forward(20)
    right(180)
    penup()
    forward(45 + 10)
    pendown()

def teken_c():
    penup()
    forward(23)

# ---------------------------------------------------
# -                                                 -
# -                                                 -
# - PROGRAMMA                                       -
# -                                                 -
# -                                                 -
# ---------------------------------------------------

#woord = input("Geef woord: ")

reset() #leeg het speelveld
speed("fastest") #verhoog de snelheid van het spel
teken_a()
teken_b()

input()
