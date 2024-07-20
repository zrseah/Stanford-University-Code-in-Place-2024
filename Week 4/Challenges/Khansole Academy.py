import random

STREAK = 3

def main():
    y = random.randint(10, 99)
    x = random.randint(10,99)
    print("Khansole Academy")
    print("What is " + str(y) + " + " + str(x) + "?")
    user_ans = int(input("Your answer: "))
    correct_ans = x + y 
    if user_ans == correct_ans:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is", correct_ans)
    
    
    
if __name__ == '__main__':
    main()