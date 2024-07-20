from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
# pre: karel facing east, at first column 
    while left_is_clear():
        fill_row_with_beepers()
        return_to_org_position()
        move_to_next_row()
    fill_row_with_beepers()
    
def fill_row_with_beepers():
# pre: karel facing east in first col 
# post: karel facing east in last col 
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

def return_to_org_position():
# pre: karel facing east in last col
# post: karel facing west in first col 
    turn_right() #karel facing north
    turn_right() #karel facing west 
    while front_is_clear():
        move()

def move_to_next_row():
# pre: karel facing west in first col 
# post karel facing east in first col
    turn_right() #karel facing north 
    move()
    turn_right() #karel facing east 



def turn_right():
    for i in range(3):
        turn_left()



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()