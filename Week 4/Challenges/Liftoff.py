"""
Program: Liftoff
--------------------
Countdown from 10 to 1 and then print Liftoff!
"""

def main():
    countdown = 11
    for i in range(10):
        countdown = countdown - 1
        print(countdown)
    print("Liftoff!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()