from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    for i in range(3):
        build_columns()
        head_towards_next_column_position()
    build_columns()
    while front_is_clear():
        move()
    turn_left()


def build_columns():
    turn_left()
    place_beepers()
    turn_right()
    turn_right()

def place_beepers():
    put_beeper()
    for i in range(4):
        move()
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

def head_towards_next_column_position():
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_left()
        for i in range(4):
            move()    



if __name__ == '__main__':
    main()