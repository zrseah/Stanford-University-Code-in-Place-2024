# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
   age = int(input("Enter an age in calendar years: "))
   dog_years = age * DOG_YRS_MULTIPLIER
   
   print("That's", dog_years, "in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()