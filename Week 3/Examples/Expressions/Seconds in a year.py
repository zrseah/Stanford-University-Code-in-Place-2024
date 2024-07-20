"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
DAYS_PER_YEAR = 365 
HOURS_PER_DAY = 24 
MINUTES_PER_HOUR = 60 
SECONDS_PER_MINUTE = 60
def main():
    seconds_in_a_year = DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE

    print("There are", seconds_in_a_year, "seconds in a year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()