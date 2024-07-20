"""
File: Rainbow.py
------------------------------
Karel makes a rainbow!
"""

"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!

Note: The unit test for this worked example is currently not working. Ignore it!
"""

from karel.stanfordkarel import *

def main():
    paint_corner('red')
    move()
    paint_corner('orange')
    move()
    paint_corner('yellow')
    move()
    paint_corner('green')
    move()
    paint_corner('blue')
    move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    
    
    
