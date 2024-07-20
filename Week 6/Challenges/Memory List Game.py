import random

NUM_PAIRS = 3

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    truth = truth_list() # neccessary to assign truth_list function to truth in order to pass truth list into shuffle function
    shuffle_list(truth)
    display = displayed_list()
    valid_index(truth, display)

def truth_list():
    truth = []
    for i in range(NUM_PAIRS):
        truth.append(i)
        truth.append(i)
    return(truth)

def shuffle_list(truth):
    random.shuffle(truth)
    return(truth)

def displayed_list():
    display = []
    for i in range(NUM_PAIRS* 2):
        display.append("*") 
    return(display)

def valid_index(truth, display):
    while "*" in display: 
        try:
            print(display)
            user_index_1 = int(input("Enter an index: "))
            if user_index_1 >=  0 and user_index_1 < NUM_PAIRS * 2:
                if display[user_index_1] == "*":
                    while True:
                        try: 
                            user_index_2 = int(input("Enter an index: "))
                            if user_index_2 != int(user_index_1):
                                if user_index_2 >=  0 and user_index_2 < NUM_PAIRS * 2:
                                    if display[user_index_2] == "*":
                                        print("Value at index", user_index_1, "is", truth[user_index_1])
                                        print("Value at index", user_index_2, "is", truth[user_index_2])
                                        if truth[user_index_1] == truth[user_index_2]:
                                            print("Match!")
                                            display[user_index_1] = truth[user_index_1]
                                            display[user_index_2] = truth[user_index_2]
                                            break
                                        else:
                                            print("No match. Try again.")
                                            input("Press Enter to continue...")
                                            clear_terminal()
                                            break
                                    else:
                                        print("This number has already been matched. Try again.")
                                else:
                                    print("Invalid index. Try again.")
                            else:
                                print("You entered the same index twice. Try again.")
                        except ValueError:    
                            print("Not a number. Try again.")
                else:
                    print("This number has already been matched. Try again.")
            else:
                print("Invalid index. Try again.")
        except ValueError: 
            print("Not a number. Try again.")
    print("Congratulations! You won!") 


def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()