"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
LEAP = "That's a leap year!"
NOT_LEAP = "That's not a leap year."

def main():
    year = int(input("Please input a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(LEAP)
            else:
                print(NOT_LEAP)
        else:
            print(LEAP)
    else:
        print(NOT_LEAP) 



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()