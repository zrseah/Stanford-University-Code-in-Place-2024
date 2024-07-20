"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def print_multiple(message, repeats):
    for i in range(repeats):
        print(message)

# There is no need to edit code beyond this point

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)
    

if __name__ == '__main__':
    main()