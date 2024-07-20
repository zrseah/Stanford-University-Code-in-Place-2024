"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    while beepers_present():
        pick_up_beepers()
        step_backwards()
        turn_left()
        move()
        if no_beepers_present():
            wrong_route()

def pick_up_beepers():
    while beepers_present():
        pick_beeper()
        move()
def wrong_route():
    step_backwards()
    turns_around()
    move()

def turns_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def step_backwards():
    turns_around()
    move()
    turns_around()





# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()