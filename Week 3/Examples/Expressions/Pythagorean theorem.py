"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

import math

def main():
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    cb = math.sqrt((ab**2)+(ac**2))

    print("The length of BC (the hypotenuse) is: " + str(cb))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()