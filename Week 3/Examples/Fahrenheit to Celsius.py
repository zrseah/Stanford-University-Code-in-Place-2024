"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    fahrenheit = input("Enter temperature in Fahrenheit: ")
    fahrenheit = float(fahrenheit)
    degrees_celcius = (fahrenheit - 32) * 5.0/9.0
    print("Temperature: " + str(fahrenheit) + "F" +" = " + str(degrees_celcius) + "C")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()