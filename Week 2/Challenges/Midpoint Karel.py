from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    fill_row_with_beepers()
    remove_unnecessary_beepers()

def fill_row_with_beepers():
    fill_both_corners_with_beepers()
    move_to_new_position()
    fill_in_between_with_beepers()

def fill_both_corners_with_beepers():
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()

def fill_in_between_with_beepers():
    while no_beepers_present():
        fill_RHS()
        fill_LHS()

def move_to_new_position():
    turn_around()
    move() # karel faces west 

def fill_RHS():
    while no_beepers_present():
        move()
        turn_around() # karel faces east 
        move()
        put_beeper()

def fill_LHS():
    if beepers_present():
        turn_around() # karel faces west
        move()
    while no_beepers_present():
        move()
        if beepers_present():
            turn_around() # karel faces east 
            move()
            if no_beepers_present():
                move()
                turn_around()
                move()
                put_beeper()
                turn_around()
                move()



def turn_around():
    turn_left()
    turn_left()

def remove_unnecessary_beepers():
    pick_beepers_towards_east()
    head_towards_opp_direction()
    pick_beepers_towards_west()
    return_to_position()

def pick_beepers_towards_east():
    if facing_west():
        turn_around()
        move()
        if front_is_clear():
            move()
    while beepers_present():
        pick_beeper()
        while front_is_clear():
            move()
            pick_beeper()
        if front_is_blocked():
            turn_around()

def head_towards_opp_direction():
    while no_beepers_present():
        move()
    if front_is_clear():
        move()
    if front_is_blocked():
        turn_around()

def pick_beepers_towards_west():
    if facing_west():
        while beepers_present():
            pick_beeper()
            move()
            if front_is_blocked():
                turn_around()

def return_to_position():
    while no_beepers_present():
        move()
  
                
     
            

        

if __name__ == '__main__':
    main()