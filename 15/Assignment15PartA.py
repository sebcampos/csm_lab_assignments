# Homework 15 Assignment Part A
# Sebastian Campos
# 2022-03-28

from html.parser import HTMLParser
from urllib.request import urlopen
import re


class MyHTMLParser(HTMLParser):
    def __init__(self, url='https://collegeofsanmateo.edu/cis/') -> None:
        """
        This class inherits from the HTMLParser
        Attributes:
            :text A string that is written when the handle_data method is invoked
            :counter a python dictionary used by the frequency method to count words
        """
        super().__init__()
        self.url = url
        self.links = []
        self.emails = []

    def handle_data(self, data: str) -> None:
        """
        This method is inherited from the HTMLParser class and is called when the `feed` method is called
        It receives the String data which represents the text on the html page. Then it is handed to this
        class's `collect_emails` method to extract emails from text and save it as an attribute
        :param data: string of data parsed by the feed method
        :return: void
        """
        self.collect_emails(data)

    def handle_starttag(self, tag: str, attrs: list) -> None:
        """
        This method is called by the `feed` method creating a string `tag` and a `list` attrs representing an elements
        tag name and its attributes. Then this is passed to this class's collect_links method to extract the links
        on the current page
        :param tag: string representing the tag name of the current element
        :param attrs: a list containing the names and values of the attributes for the current element
        :return: void
        """
        self.collect_links(tag, attrs)

    def collect_emails(self, data: str) -> None:
        """
        This method parses the text data handed by the handle_data method and uses the re module
        to extract email addresses found on the page
        :param data:
        :return: void
        """
        match = re.search(r"([A-Za-z0-9._-]+@[A-Za-z0-9._-]*\.[a-zA-z]{3})", data)
        if match:
            email = match.groups()[0]
            self.emails.append(email)

    def collect_links(self, tag: str, attrs: list) -> None:
        """
        This method uses the html element data handed to it by the handle_starttag method to collect
        href attribute values from the a tag elements present on the page
        :param tag: string representing the tagname
        :param attrs: a list containing pairs of names and values
        :return: void
        """
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    self.links.append(value)


def main(url: str = None) -> list:
    """
    This is the main method. Using the MyHTMLParser and urlopen method it recieves the data from urlopen method
    and parses it saving all emails to an attribute in the MyHTMLParser called emails
    :return: list of emails
    """
    if url:
        hp = MyHTMLParser(url)
    else:
        hp = MyHTMLParser()
    content = urlopen(hp.url).read().decode()
    hp.feed(content)
    return hp.emails


if __name__ == "__main__":
    print(main())
