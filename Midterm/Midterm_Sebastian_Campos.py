# Midterm Programming Assignment
# Sebastian Campos
# 2022-03-25


def total_word_count(text: str) -> int:
    """
    receives a string as parameter and returns the total number of words in the text
    :param text: string of words to process
    :return: total number of words as an integer
    """
    text = text.replace("\n", " ")  # replace all \n with " " for processing
    for char in text:
        if not char.isalpha() and char != " ":  # replace all punctuation with empty string
            text = text.replace(char, "")
    return len(text.split())  # split the text by white space and use len function to return the lists size


def unique_word_count_ignore_case(text: str) -> int:
    """
    receives a string as parameter and returns the number
    of unique words (after repetitions are eliminated and upper/lower case is ignored)
    :param text: string of words to process
    :return: number of unique words as an integer
    """
    text = text.replace("\n", " ")  # replace all \n with " " for processing
    for char in text:
        if not char.isalpha() and char != " ":  # replace all punctuation with empty string
            text = text.replace(char, "")
    return len(set([i.lower().strip() for i in text.split()]))


def word_frequency_ignore_case(text: str) -> dict:
    """
    receives a string as parameter and returns a dictionary where the
    keys are words and values are the corresponding word count
    :param text: string of words to process
    :return: dictionary of word counts
    """
    text = text.replace("\n", " ")  # replace all \n with " " for processing
    for char in text:
        if not char.isalpha() and char != " ":  # replace all punctuation with empty string
            text = text.replace(char, "")
    count_dict = {}  # init dictionary
    for word in text.split():  # split text by white spaces and iterate over every word)
        lowercase = word.lower().strip()  # lower the word to account for case sensitivity
        if lowercase in count_dict:  # if the word is in our dictionary increment its count
            count_dict[lowercase] += 1
        else:
            count_dict[lowercase] = 1  # if it is not in dictionary create it with a count of 1
    return count_dict  # after iteration return dictionary


def print_frequencies(count_dict: dict, n: int) -> None:
    """
    receives the dictionary with word frequencies and a value `n` and prints all the words
    whose frequencies are greater than the value passed as a second parameter `n`
    :param count_dict: dictionary of word counts
    :param n: value to compare word counts as an integer
    :return: None
    """
    print("Word frequencies:")
    column = 0
    for word, count in count_dict.items():
        if count > n and column == 0:
            formatting_spaces = (15 - len(word)) * " "
            column = 1
            print(f"{word}{formatting_spaces}: {count}", end=10*" ")
        elif count > n and column == 1:
            formatting_spaces = (15 - len(word)) * " "
            column = 0
            print(f"{word}{formatting_spaces}: {count}")
        elif count <= n:
            continue


if __name__ == "__main__":
    testing_data = """
    The governing wisdom about writing sentences says not to repeat. 
    Repetition is bad. Repetition is sloppy. 
    Writers are encouraged to consult a thesaurus and change up that pesky offending word. 
    But is this really true? 
    Literature is full of repetition. 
    Literary writers constantly use the literary device of repeated words. 
    I think the only type of repetition which is bad is sloppy repetition. Repetition which is unintentional, 
    which sounds awkward. If you repeat on purpose, repetition is gorgeous. I mean, think about music. 
    Music is all about repetition and patterns. If you didn’t have repetition in music, 
    it would all just be noise.
    """
    print("Total word count", total_word_count(testing_data))  # print the return to total word count

    print("Total unique word count", unique_word_count_ignore_case(testing_data), end="\n\n")  # print the return of
    # unique word count

    print_frequencies(word_frequency_ignore_case(testing_data), 2)  # use print frequencies handing it the return of
    # word_frequency_ignore_case (a python dictionary) and the integer of words frequencies

