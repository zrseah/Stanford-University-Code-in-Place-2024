"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def print_divisors(num):
    print("Here are the divisors of", num)
    for i in range(num):
        if num % (i + 1) == 0:
            print(i + 1)
def main():
    num = int(input("Enter a number: "))
    print_divisors(num)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()