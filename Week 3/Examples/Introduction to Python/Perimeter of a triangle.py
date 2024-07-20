"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    side_1 = input("What is the length of side 1? ")
    side_1 = float(side_1)
    side_2 = input("What is the length of side 2? ")
    side_2 = float(side_2)
    side_3 = input("What is the length of side 3? ")
    side_3 = float(side_3)
    perimeter = side_1 + side_2 + side_3
    print("The perimeter of the triangle is", perimeter)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
