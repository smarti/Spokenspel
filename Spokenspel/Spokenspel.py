# ----------------------------------------------------
# -                                                  -
# -                                                  -
# -   Scroll naar beneden om het programma te zien   -
# -                                                  -
# -                                                  -
# ----------------------------------------------------

from turtle import *

def teken_deuren(aantal_deuren):
    reset() #leeg het speelveld
    speed("fastest")

    penup()
    setposition(-300, 0)
    pendown()

    aantal_getekend = 0
    while aantal_getekend < aantal_deuren:
        left(90)
        forward(95) #1
        right(90)
        forward(10) #2
        right(90)
        forward(85) #3
        left(90)
        forward(35) #4
        penup()
        forward(10) #oversteken
        pendown()
        forward(35) #5
        left(90)
        forward(85) #6
        left(90)
        forward(35) #7
        left(90)
        forward(85) #8
        right(90)
        penup()
        forward(10) #oversteken
        pendown()
        right(90)
        forward(85) #9
        left(90)
        forward(35) #10
        right(90)
        forward(10 + 85) #11 en 12
        right(90)
        forward(80) #13
        right(90)
        forward(85) #14
        right(90)
        forward(90) #15 en 16
        left(90)
        forward(10) #17
        right(180)
        forward(105) #17 (nogmaals) en 18
        right(90)
        forward(100) #19
        right(90)
        forward(200) #20
        right(90)
        forward(100) #21
        right(180)

        penup()
        forward(150) #schuif pen op voor volgende deur
        pendown()

        aantal_getekend += 1

def teken_gekozen_deur(door_num):
    penup()
    setposition(-300 + (door_num - 1) * 150, 0) #Zet cursor op de juiste plaats
    pendown()

    fillcolor("Black") #kleur om te vullen
    begin_fill() #start met vullen
    left(90)
    forward(200)
    right(90)
    forward(100)
    right(90)
    forward(200)
    right(90)
    forward(100)
    right(180)
    end_fill() #vul de vorm

def teken_geest(ghost_door):
    penup()
    setposition(-300 + (ghost_door - 1) * 150, 230)
    pendown()

    right(30)
    forward(55)
    left(60)
    forward(55)
    right(30)


# ---------------------------------------------------
# -                                                 -
# -                                                 -
# -                  PROGRAMMA                      -
# -                                                 -
# -                                                 -
# ---------------------------------------------------

from random import randint

print("spakun spol")

feeling_brave = True
score = 0

while feeling_brave:
    teken_deuren(3)

    ghost_door = randint(1, 3)
    
    print('Three doors ahead...')
    print('A ghost behind one.')
    print('Which door do you open?')
    
    door = input('1, 2, or 3?')
    door_num = int(door)

    if door_num == ghost_door:
        print('GHOST!')
        feeling_brave = False
    else:
        print('No ghost!')
        print('You enter the next room.')
        score = score + 1
        
    teken_gekozen_deur(door_num)
    teken_geest(ghost_door)
    input('<enter> to continue')


print('Run away!')
print('Game over! You scored: ', score)