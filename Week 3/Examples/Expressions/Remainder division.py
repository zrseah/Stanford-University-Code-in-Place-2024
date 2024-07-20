"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    int_one = int(input("Please enter an integer to be divided: "))
    int_two = int(input("Please enter an integer to divide by: "))
    result = int_one // int_two
    remainder = int_one % int_two
    print("The result of this division is " + str(result) +  " with a remainder of", str(remainder))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()