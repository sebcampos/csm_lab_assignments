# Midterm Programming Assignment
# Sebastian Campos
# 2022-03-25


def total_word_count(text: str) -> int:
    """
    receives a string as parameter and returns the total number of words in the text.
    :param text: string
    :return: total number of words as an integer
    """
    return len(text.split())


def unique_word_count(text: str) -> int:
    """
    receives a string as parameter and returns the number
    of unique words (after repetitions are eliminated and upper/lower case is ignored).
    :return: number of unique words as an integer
    """
    return len(set([i.lower() for i in text.split()]))


def word_frequency_ignore_case(text: str) -> dict:
    """
    receives a string as parameter and returns a dictionary where the
    keys are words and values are the corresponding word count
    :param text:
    :return: dictionary of word counts
    """
    count_dict = {}  # init dictionary
    for word in text.split():  # split text by white spaces and iterate over every word
        lowercase = word.lower()  # lower the word to account for case sensitivity
        if lowercase in count_dict:  # if the word is in our dictionary increment its count
            count_dict[lowercase] += 1
        count_dict[lowercase] = 1  # if it is not in dictionary create it with a count of 1
    return count_dict  # after iteration return dictionary


def print_frequencies(count: dict, n: int) -> None:
    """
    receives the dictionary with word frequencies and a value and prints all the words
    whose frequencies are greater than the value passed as a second parameter `n`
    :param count:
    :param n:
    :return:
    """
    pass
