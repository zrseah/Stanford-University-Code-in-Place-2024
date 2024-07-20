"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
# pre: karel facing east in col 1 
    for i in range(2):
        move_towards_wall()
        move_along_wall_up()
        place_beepers()
        move_along_wall_down()
    move_towards_wall()

def move_towards_wall():
    while front_is_clear():
        move()

def move_along_wall_up():
    turn_left()
    while right_is_blocked():
        move()

def move_along_wall_down():
    while front_is_clear():
        move()
    turn_left()


def place_beepers():
    put_beeper()
    for i in range(3):
        move()
        put_beeper()
        turn_right()
    turn_left()
    move()

    


def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()