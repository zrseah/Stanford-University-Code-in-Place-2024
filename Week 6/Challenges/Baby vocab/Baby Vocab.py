def main():
    words = load_words_from_file("words.txt")
    counts = count_words(words)
    print_histogram(counts)

def count_words(words):
    counts = {}
    for i in range (len(words)):
        baby_words = words[i]
        if baby_words not in counts.keys():
            counts[baby_words] = 1
        else:
            counts[baby_words] += 1

    return counts

def print_histogram(counts):
    for word, counts in counts.items(): #naming can be set to be anything as long as it is consistent in the next few components
        print_histogram_bar(word, counts) #here



def print_histogram_bar(word, counts): #here
    """
    Prints one bar in the histogram.
    
    Uses formatted strings to do so. The 
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the 
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.
    
    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """
    print(f"{word : <8}: {'x' * counts}") #here

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words


if __name__ == '__main__':
    main()
