def print_upper_words(words, must_start_with):
    
    for word in words:  # Loopd through each word in the list
        if word[0].lower() in must_start_with:  # Checks if the word starts with a letter in the set
            print(word.upper())  # Converts the word to uppercase and prints it

# Example usage:
print_upper_words(["apple", "banana", "cherry", "apricot", "blueberry"], must_start_with={"a", "b"})
