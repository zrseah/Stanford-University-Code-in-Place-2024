"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    beepers_columns()
    while front_is_clear():
        non_beeper_columns()
        beepers_columns()

def beepers_columns():
#pre: karel facing east in col 1 with no beepers 

#fill up column 1 with beepers 
    turn_left()
    move_to_wall()
    turn_right()
    move()
#fill up column 2 with beepers
    turn_right()
    move_to_wall()
    turn_left()

def move_to_wall():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

def non_beeper_columns():
    for i in range(4):
        move()
    





    
        




# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()