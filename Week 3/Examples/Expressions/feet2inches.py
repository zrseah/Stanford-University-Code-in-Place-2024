"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

"""
An example program with constants
"""

INCHES_IN_FOOT = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")
    
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()