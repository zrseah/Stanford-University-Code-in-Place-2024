from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""
def main():
    fill_entire_world_with_beepers()
    remove_alternate_beepers()

def fill_entire_world_with_beepers():
    while left_is_clear():
        fill_entire_row_with_beepers()
        return_to_org_position()
        move_to_next_row()
    fill_entire_row_with_beepers()
    return_to_org_position()
    return_to_start_point()

def fill_entire_row_with_beepers():
    while no_beepers_present():
        put_beeper()
        if front_is_clear():
            move()
        if front_is_blocked():
            if no_beepers_present(): 
                put_beeper()
            turn_around()

def turn_around():
    turn_left()
    turn_left()

def return_to_org_position():
    while front_is_clear(): ### Karel is facing west 
        move()

def move_to_next_row():
    if front_is_blocked(): 
        turn_right()
        move()
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def return_to_start_point():
    turn_left() #karel faces south
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_left()


def remove_alternate_beepers():
    remove_first_row_beepers()
    u_turn()
    move_to_row_above() #karel faces north 
    while front_is_clear(): #karel faces north at the end 
        remove_beepers_across_rows()
        u_turn()
        move_to_row_above()
    starting_position()

def remove_first_row_beepers():
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
            if front_is_clear():
                move()

def u_turn():
    if front_is_blocked():
        turn_around()
    while front_is_clear(): #karel faces west 
        move()

def move_to_row_above():
    turn_right()

def remove_beepers_across_rows():
    if front_is_clear():
        if beepers_present():
            move()
            turn_right()
            pick_beeper()
            while front_is_clear():
                move()
                if front_is_clear():
                    move()
                    pick_beeper()
    if front_is_clear():
        if no_beepers_present():
            move()
            turn_right()
            while front_is_clear():
                move()
                pick_beeper()
                if front_is_clear():
                    move()

def starting_position():
    turn_right()
    turn_right() #karel faces south 
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()