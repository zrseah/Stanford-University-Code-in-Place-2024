from graphics import Canvas
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
STAND_WIDTH = 150
STAND_HEIGHT = 300
STAND_BASE = 100

def main():
    # Initiation of Hangman 
    words = word_bank()
    random_key, random_value = word_randomiser(words)
    display, formatted_display = display_list(random_value)
    input_list = user_input_list()
    hint = get_hint(random_key)

    # Hangman Graphics 
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    hangman_stand(canvas)
    error_count = draw_hangman()

    # Execution of Hangman Game 
    hangman(random_key, random_value, display, formatted_display, input_list, hint, canvas, error_count)    
    
def word_bank(): # Create a dictionary of words and their character lengths  
    words = {
        "line": 4,
        "enter": 5,
        "era": 3,
        "right": 5,
        "lily": 4,
        "absence": 7,
        "extort": 6,
        "appreciate": 10,
        "paragraph": 9,
        "consciousness": 13,
        "title": 5,
        "victory": 7,
        "inspiration": 11,
        "lake": 4,
        "tray": 4}
    return words

def word_randomiser(words): # Function to select words randomly
    random_key = random.choice(list(words.keys())) # randomly choosing a word from words 
    random_value = words[random_key]
    return random_key, random_value

def display_list(random_value): # Create a display list corresponsding to the number of letters in the randomly selected word
    display = [] # Begin with empty list 
    for i in range(int(random_value)): # Loop through range of word length 
        display = [ "_" ] * int(random_value)
    formatted_display = f"[{' '.join(display)}]" # Create a formatted string in display list, with underscores separated by spaces and enclosed in brackets 
    return(display, formatted_display)

def user_input_list(): # Create an empty list to store a list of letters that have already been guessed by the user 
    input_list = []
    return(input_list)

def get_hint(random_key): # Define hints for each key 
    if random_key == "line":
        return("hint: I can be straight, I can be curved, but without me, drawing would be absurd.")
    elif random_key == "enter":
        return("hint: I open doors without a key, and on your keyboard, you'll find me.")
    elif random_key == "era":
        return("Hint: I define a time that's grand, a long stretch in history's sand.")
    elif random_key == "right":
        return("Hint: I'm never wrong, you see, and I’m the opposite of left, trust me.")
    elif random_key == "lily":
        return("Hint: In gardens, pure and fair, I bloom with a fragrant air.")
    elif random_key == "abscence":
        return("Hint: When I’m here, you are not, marked by an empty spot.")
    elif random_key == "extort":
        return("Hint: I get what I want through fear or threat, my methods you should never forget.")
    elif random_key == "appreciate":
        return("Hint: To see my value grow, or to thank and let it show.")
    elif random_key == "paragraph":
        return("Hint: A block of text that tells a tale, in writing, I never fail.")
    elif random_key == "consciousness":
        return("Hint: Aware and awake, this state is profound, in dreams and thoughts, it’s where you’re found.")
    elif random_key == "title":
        return("Hint: I’m at the start of a story or song, a name or rank where I belong.")
    elif random_key == "victory":
        return("Hint: The sweet taste of success, in games or battles, I bless.")
    elif random_key == "inspiration":
        return("Hint: A spark of genius, a creative fire, what artists and writers most desire.")
    elif random_key == "lake":
        return("Hint: A peaceful body, calm and wide, with fish and boats that gently glide.")
    elif random_key == "tray":
        return("Hint: I carry your meal or tea set with grace, holding items neatly in place.")

def hangman_stand(canvas): # Draw the hangman stand 
    draw_hline(canvas, (CANVAS_WIDTH - STAND_WIDTH)/2, (CANVAS_HEIGHT - STAND_HEIGHT)/2, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH, (CANVAS_HEIGHT - STAND_HEIGHT)/2, 'black') # stand width
    draw_vline(canvas, (CANVAS_WIDTH - STAND_WIDTH)/2, (CANVAS_HEIGHT - STAND_HEIGHT)/2, (CANVAS_WIDTH - STAND_WIDTH)/2, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + STAND_HEIGHT, 'black') # stand height 
    draw_hline(canvas, ((CANVAS_WIDTH - STAND_WIDTH)/2) - STAND_BASE/2, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + STAND_HEIGHT, ((CANVAS_WIDTH - STAND_WIDTH)/2) + STAND_BASE/2, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + STAND_HEIGHT, 'black') # stand base
    draw_dline(canvas, (CANVAS_WIDTH - STAND_WIDTH)/2, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/5 * STAND_HEIGHT, (CANVAS_WIDTH - STAND_WIDTH)/2 + 1/4 * STAND_WIDTH, (CANVAS_HEIGHT - STAND_HEIGHT)/2, 'black')
    draw_vline(canvas, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH, (CANVAS_HEIGHT - STAND_HEIGHT)/2, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT, 'black') #hanger

def draw_hline(canvas, x1, y1, x2, y2, colour): # Horizontal line
    canvas.create_line(x1, y1, x2, y2, colour)

def draw_vline(canvas, x1, y1, x2, y2, colour): # Vertical line
    canvas.create_line(x1, y1, x2, y2, colour)

def draw_dline(canvas, x1, y1, x2, y2, colour): # Diagonal line 
    canvas.create_line(x1, y1, x2, y2, colour)

def draw_hangman(): # Cretae a dictionary to store different drawing functions based on error count
    error_count = {
        1: draw_head,
        2: draw_body,
        3: draw_lhand,
        4: draw_rhand,
        5: draw_lleg,
        6: draw_rleg}
    return(error_count)

def draw_head(canvas):
    draw_circle(canvas, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH - 25, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH + 25, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50, 'white', 'red')

def draw_circle(canvas, x1, y1, x2, y2, fill, outline):
    canvas.create_oval(x1, y1, x2, y2, fill, outline)

def draw_body(canvas):
    draw_hline(canvas, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50 + 100, 'red')

def draw_lhand(canvas): # Left hand 
    draw_dline(canvas, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH - 30, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50 + 30, 'red')

def draw_rhand(canvas): # Right hand
    draw_dline(canvas, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH + 30, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50 + 30, 'red')

def draw_lleg(canvas): # Left leg 
    draw_dline(canvas, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50 + 100, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH - 30, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50 + 100 + 30, 'red' )

def draw_rleg(canvas): # Right leg 
    draw_dline(canvas, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50 + 100, (CANVAS_WIDTH - STAND_WIDTH)/2 + STAND_WIDTH + 30, (CANVAS_HEIGHT - STAND_HEIGHT)/2 + 1/7 * STAND_HEIGHT + 50 + 100 + 30, 'red' )

def get_indices(word, letter): # Generate the index of the letter in random key 
    return [index for index, char in enumerate(word) if char == letter]

def hangman(random_key, random_value, display, formatted_display, input_list, hint, canvas, error_count):
    error = 0
    max_error = 6
    print("Welcome to the Game of Hangman!")
    start_game = input("Press Enter to start: ")
    clear_terminal()
    print("Guess the word!")

    while "_" in display: # Code will continue to loop through as long as underscores are present in display i.e. user unable to guess the correct letters
        if error < max_error: # Remaining chunk of the code will only be executed if this condition is met 
            print(formatted_display)
            if error == 0:
                user_input = input("Enter a letter: ")
                if user_input.isalpha(): # Ensure that only alphabets are entered
                    user_input = user_input.lower() # Convert user input to lower cases just in case they typed in caps 
                    if len(user_input) == 1: # Ensure only one character is entered at a time
                        if user_input not in input_list: # Ensure letters entered are not already entered by user previously
                            if user_input in random_key: # If user made a correct guess
                                input_list.append(user_input) # Append input list based on user input
                                index = get_indices(random_key, user_input) # Populate the index number of the correct guess in random key
                                for index in index: 
                                    display[index] = user_input # Update the display list with the correct guess by the index number populated above 
                                formatted_display = f"[{' '.join(display)}]" # Formatted into string for display to user on the positions of the correct guess
                                clear_terminal()
                                print("Correct!")
                                print(" ")
                            else: # If a wrong guess is made
                                clear_terminal()
                                print("Incorrect, please try again!")
                                print(" ")
                                error += 1 # Counts the number of errors made
                                if error in error_count: 
                                    error_count[error](canvas) # Draw the relevant body parts on hanman stand based on error count
                                input_list.append(user_input) # Append input list based on user input 
                        else:
                            clear_terminal()
                            print("Letter has already been keyed in, please key in another!")
                    else:
                        clear_terminal()
                        print("One letter at a time! Please try again!")
                else:
                    clear_terminal()
                    print("Not a letter, try again.")
            else: # Hint prompted in this code chunk if user has an error count > 0
                user_input = input("Enter a letter or enter 'hint' for hints!: ")
                if user_input.isalpha():
                    user_input = user_input.lower()
                    if user_input == "hint":
                        clear_terminal()
                        print(hint)
                    else:
                        if len(user_input) == 1:
                            if user_input not in input_list:
                                if user_input in random_key:
                                    input_list.append(user_input)
                                    index = get_indices(random_key, user_input)
                                    for index in index: 
                                        display[index] = user_input
                                    formatted_display = f"[{' '.join(display)}]"
                                    clear_terminal()
                                    print("Correct!")
                                    print(" ")
                                else:
                                    clear_terminal()
                                    print("Incorrect, please try again!")
                                    print(" ")
                                    error += 1 
                                    if error in error_count:
                                        error_count[error](canvas)
                                    input_list.append(user_input)
                            else:
                                clear_terminal()
                                print("Letter has already been keyed in, please key in another!")
                        else:
                            clear_terminal()
                            print("One letter at a time! Please try again!")
                else:
                    clear_terminal()
                    print("Not a letter, try again.")
        else:
            clear_terminal()
            print("Game Over! The word is", random_key + '.')
            break # Break from the loop 
    else:
        print("Congratulations! You have won! The word is", random_key + '.') 
        
def clear_terminal():
    for i in range(20):
      print('\n')


if __name__ == "__main__":
    main()
