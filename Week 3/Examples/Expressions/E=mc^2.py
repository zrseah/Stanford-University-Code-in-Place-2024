"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
C = 299792458

def main():
    mass = float(input("Enter kilos of mass: "))
    formula = mass * (C**2)
    print("e = m * C^2...")
    print("m =", mass, "kg")
    print("C =", C, "m/s") 
    print(formula, "joules of energy!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()