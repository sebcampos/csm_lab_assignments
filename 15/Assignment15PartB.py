# Homework 15 Assignment Part B
# Sebastian Campos
# 2022-03-28

import tkinter as tk
import datetime
import os
from Assignment15PartA import main as email_scraper


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x150")
        self.title("Email Scraper")

    def scrape(self, entry):
        url = entry.get()
        print(url)
        emails = email_scraper(url)
        print(emails)

    def build(self):
        frame = tk.Frame(self, bg="yellow", bd=12)
        frame.pack()
        entry = tk.Entry(frame)
        entry.pack()
        btn = tk.Button(
            self,
            text="Collect emails",
            command=lambda txt=entry: self.scrape(entry)
        )
        btn.pack()
        return self


if __name__ == "__main__":
    App().build().mainloop()
