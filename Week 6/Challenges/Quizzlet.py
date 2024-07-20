def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    score = 0
    for key, value in translations.items():
        user_response = input("What is the Spanish translation for "+ key + "? ")
        if user_response == value:
            print("That is correct!")
            score += 1
        else:
            print("That is incorrect, the Spanish translation for " 
            + key + " is " + value + ".")
        print("")
    print("You got " + str(score) + "/8 words correct, come study again soon!")


if __name__ == '__main__':
    main()