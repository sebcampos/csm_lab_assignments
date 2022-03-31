# Homework 14 Assignment
# Sebastian Campos
# 2022-03-28


from html.parser import HTMLParser
from urllib.request import urlopen
import datetime


class MyHTMLParser(HTMLParser):
    def __init__(self) -> None:
        """
        This class inherits from the HTMLParser
        Attributes:
            :text A string that is written when the handle_data method is invoked
            :counter a python dictionary used by the frequency method to count words
        """
        super().__init__()
        self.text = []
        self.raw_text = ""
        self.counter = {}

    def handle_data(self, data: str) -> None:
        """
        This method is inherited from the HTMLParser class and parses html strings.
        It is used to save the data into the text attribute
        :param data: html string
        :return: void
        """
        self.raw_text += data
        for d in data.split():  # create a list of words by splitting the text by whitespace
            if not d.isalpha() and d != "\n":
                continue  # skip this word if it does not contain alphabetical characters
            self.text.append(d)

    def frequency(self, n: int) -> None:
        """
        This method takes an integer `n` and builds a dictionary from the text attribute
        containing every word and the number of times the word occurs. After it prints the words
        which occured `n` or more times.
        :param n: integer representing which values to print
        :return: void
        """
        for word in self.text:
            if word == "\n":
                continue
            lowercase_word = word.lower()  # lower the word to account for case sensitivity
            if lowercase_word in self.counter:
                self.counter[lowercase_word] += 1  # check if word is in dictionary and if so increment its count by 1
                continue
            self.counter[lowercase_word] = 1  # add word to dictionary with a count of 1

        for word, count in self.counter.items():  # iterate over words and counts
            if count >= n:
                print(f"Word '{word}' occurred {count} time(s)")  # print all counts greater than or equal to n

    def dump_data(self, filename) -> None:
        """
        Write the contents of the
        :param filename:
        :return:
        """
        with open(filename, "w") as f:
            f.write(f"[{datetime.datetime.now()}]\n{self.raw_text}")  # write string to file


# add the code here to test your class if this is called as a top-level module
# make sure to add the call to frequency at the end

if __name__ == "__main__":
    link = 'https://collegeofsanmateo.edu/wellnesscenter/'

    response = urlopen(link)
    html_page = response.read().decode().lower()

    parser = MyHTMLParser()
    parser.feed(html_page)

    parser.frequency(3)
    parser.dump_data("test.txt")
