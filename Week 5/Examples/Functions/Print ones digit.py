"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def print_ones_digit(num):
    remainder = num % 10 
    if remainder != 0:
        print("The ones digit is", remainder)
    else:
        print("The ones digit is 0")

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)
    
    
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()