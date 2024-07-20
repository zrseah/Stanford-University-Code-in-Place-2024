"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution
"""

"""
This program computes square roots
"""

import math  # Imports the math library so we can use math.sqrt()

def main():
    num = float(input("Enter number: "))  # Make sure to cast the user's input to a float!
    root = math.sqrt(num)  # Get the square root of the user's input and store it in a variable
    print("Square root of", num, "is", root)
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()