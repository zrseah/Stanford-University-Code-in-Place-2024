"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_right()
    turn_right()
    turn_right()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()