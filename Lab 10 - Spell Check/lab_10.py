import re
# --- Spell Check ---


def main():
    # Assign names for the files.
    my_text = open("AliceInWonderland200.txt")
    dictionary = open("dictionary.txt")

    # List to store each word in dictionary.txt.
    dictionary_words = []

    # Variable to keep track of the line number.
    line_number = 0

    # This function takes in a line of text and returns
    # a list of words in the line.
    def split_line(lines):
        return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', lines)

    # Read dictionary.txt into an array.
    for line in dictionary:
        line = line.strip()
        dictionary_words.append(line)

    dictionary.close()

    print("--- Linear Search ---")

    # Split my_text into words and do a linear search for each word.
    for line in my_text:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            # key will change every time it loops.
            key = word.upper()

            # We will start at the beginning of the list.
            current_list_position = 0

            # Loop to check if the word matches on of the words in dictionary_words, or check
            # is we go to the end of the list.
            while current_list_position < len(dictionary_words) and dictionary_words[current_list_position] != key:
                current_list_position += 1

            # If the word doesn't match one of the words in the dictionary, print something.
            if current_list_position >= len(dictionary_words):
                print("Line", line_number, "possible misspelled word:", word)

    my_text.close()

    print("--- Binary Search ---")

    # Reopen my_text to use it again.
    my_text = open("AliceInWonderland200.txt")

    # Reset line_number to 0.
    line_number = 0

    # Split my_text into words and do a binary search for each word.
    for line in my_text:
        word_list = split_line(line)
        line_number += 1

        for word in word_list:
            # key will change every time it loops.
            key = word.upper()

            # Lower and upper bounds for our binary search..
            lower_bound = 0
            upper_bound = len(dictionary_words) - 1
            found = False

            # Loop until the item is found or the bounds meet.
            while lower_bound <= upper_bound and not found:

                # Middle position.
                middle_pos = (lower_bound + upper_bound) // 2

                # Move the bounds up and down, or we found our item.
                if dictionary_words[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_words[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            # If the word does not exist in the dictionary, print something.
            if not found:
                print("Line", line_number, "possible misspelled word:", word)


main()
