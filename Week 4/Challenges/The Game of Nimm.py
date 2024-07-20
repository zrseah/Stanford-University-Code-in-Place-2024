STONES = 20
PLAYER_1 = "Player 1 would you like to remove 1 or 2 stones? "
PLAYER_2 = "Player 2 would you like to remove 1 or 2 stones? "

def main():
    # first round 
    # not included in while loop as stone_left not defined yet 
    print("There are", STONES, "stones left.")
    player_1_input = int(input(PLAYER_1))
    while player_1_input != 1 and player_1_input != 2:
        player_1_input = int(input("Please enter 1 or 2: "))
    print(" ")
    stones_left = STONES - player_1_input # define stone_left before while loop
    
    # subsequent rounds 
    while stones_left > 0:
        # prompts player 2
        print("There are", stones_left, "stones left.")
        player_2_input = int(input(PLAYER_2))
        # ensures that player 2 only keys in 1 or 2 stones only 
        while player_2_input != 1 and player_2_input != 2:
            player_2_input = int(input("Please enter 1 or 2: "))
        # ensures that player 2 does not key in more stones than there are left 
        while player_2_input > stones_left:
            player_2_input = int(input("There is only {} stone left. Please enter again: ".format(stones_left)))
        print(" ")
        stones_left = stones_left - player_2_input
        # announce winner when there are no stones left 
        if stones_left == 0:
            print("Player 1 wins!")

        # prompts player 1 
        if stones_left > 0: # ensures that code will not run to an issues if player 2 is the winner
            print("There are", stones_left, "stones left.")
            player_1_input = int(input(PLAYER_1))
            # ensures that player 1 only keys in  1 or 2 stones 
            while player_1_input != 1 and player_1_input != 2:
                player_1_input = int(input("Please enter 1 or 2: "))
            # ensures that player 1 does not key in more stones than there are left 
            while player_1_input > stones_left:
                player_1_input = int(input("There is only {} stone left. Please enter again: ".format(stones_left)))
            print(" ")
            stones_left = stones_left - player_1_input
            # annouce winner when there are no stones left 
            if stones_left == 0:
                print("Player 2 wins!")
                


if __name__ == '__main__':
    main()