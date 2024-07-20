"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

MIN_HEIGHT = 50

def main():
    user_height = float(input("How tall are you? "))
    if user_height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else: 
        print("You're not tall enough to ride, but maybe next year!")


if __name__ == '__main__':
    main()