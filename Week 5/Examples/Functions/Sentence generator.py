"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print("I am excited to add this", word, "to my vast collection of them!")
    elif part_of_speech == 1:
        print("It's so nice outside today it makes me want to", word + "!")
    elif part_of_speech == 2:
        print("Looking out my window, the sky is big and", word + "!")

# There is no need to edit code beyond this point

def main():
    word = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()