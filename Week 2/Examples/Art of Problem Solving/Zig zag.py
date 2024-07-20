"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Places beepers in a zig zag pattern.
    """
    while front_is_clear():
        zig_zag_one()
        move_to_next_zig_zag_one_spot()

def zig_zag_one():
    put_beeper()
    turn_left()
    move()
    turn_right()
    if front_is_clear():
        move()
        put_beeper()

def move_to_next_zig_zag_one_spot():
    turn_right() # facing south
    move()
    turn_left()
    if front_is_clear():
        move()


def turn_right():
    for i in range (3): 
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()