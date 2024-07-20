"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    num_one = int(input("Enter first number: "))
    num_two = int(input("Enter second number: "))
    ans = num_one * num_two
    print(ans)
    # your code here


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()