"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        turn_right() # karel face south 
        move_towards_wall()
        place_beeper()
        return_to_initial_position()
        move_to_next_column()
    turn_right() # karel face south 
    move_towards_wall()
    place_beeper()
    return_to_initial_position()
    
def turn_right():
    for i in range(3):
        turn_left()

def move_towards_wall():
    while front_is_clear():
        move() # karel face south 

def place_beeper():
    put_beeper()

def return_to_initial_position():
    # pre: karel face south
    # post: 
    turn_left() # karel face east 
    turn_left() # karel face north 
    while front_is_clear():
        move()
    turn_right() # karel face east 

def move_to_next_column():
    move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()