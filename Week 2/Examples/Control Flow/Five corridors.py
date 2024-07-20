from karel.stanfordkarel import *

def main():
    while left_is_clear():
        move_towards_wall()
        check_for_beeper()
        return_to_initial_position()
        move_to_next_row()
    move_towards_wall()
    check_for_beeper()
    return_to_initial_position() # karel facing west 
    turn_right() # karel facing north 
    turn_right() # karel facing east

def move_towards_wall():
    # pre: karel facing east 
    # post: karel facing east 
    while front_is_clear():
        move()

def check_for_beeper():
    # pre: karel facing east 
    # post: karel facing east 
    if no_beepers_present():
        put_beeper()

def return_to_initial_position():
    # pre: karel facing east 
    # post: karel facing west
    turn_left() # karel facing north 
    turn_left() # karel facing west 
    while front_is_clear():
        move() # karel facing west
def move_to_next_row():
    # pre: karel facing west
    # post: karel facing east 
    turn_right() # karel facing north 
    move()
    turn_right() # karel facing east 

def turn_right():
    for i in range(3):
        turn_left()



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
