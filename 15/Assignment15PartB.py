# Homework 15 Assignment Part B
# Sebastian Campos
# 2022-03-28

import tkinter as tk
import turtle as t
import re
from Assignment15PartA import main as email_scraper


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("750x250")
        self.title("Email Scraper")
        self.frame_one = tk.Frame(
            self,
            bg="yellow",
            bd=12
        )
        self.entry = tk.Entry(
            self.frame_one
        )

        self.btn = tk.Button(
            self,
            text="Collect emails",
            command=lambda entry=self.entry: self.scrape(entry)
        )

    def clean_url(self, url: str) -> str:
        """

        :param url:
        :return:
        """
        if "https://" not in url:
            url = "https://" + url

        if re.search(r"https://.+\.[a-zA-Z]{3}", url):
            return url
        self.raise_invalid_url_popup(url)

    def scrape(self, entry):
        url = self.clean_url(entry.get())
        emails = email_scraper(url)
        print(emails)

    def raise_invalid_url_popup(self, url: str) -> None:
        pop_up = tk.Toplevel(self)
        pop_up.geometry("300x150")
        pop_up.title("Child Window")
        tk.Label(pop_up, text="Hello World!", font=('Mistral 18 bold')).place(x=150, y=80)
        pass

    def build(self: tk.Tk) -> tk.Tk:
        self.entry.pack()
        self.frame_one.pack()
        self.btn.pack()
        return self


if __name__ == "__main__":
    App().build().mainloop()
