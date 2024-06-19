from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    going_straight()
    exit_house()
    move()
    pick_beeper()
    enter_house()
    going_straight()
    turn_right()
    turn_right()
    
def going_straight():
    while front_is_clear():
        move()
        
def exit_house():
    turn_right()
    move()
    turn_left()
        
def enter_house():
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()

    
    

def turn_right():
    for i in range(3):
        turn_left()
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()