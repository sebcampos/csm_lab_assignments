# Homework 15 Assignment Part B
# Sebastian Campos
# 2022-03-28
import _tkinter
import tkinter as tk
import random
import time
import re
from Assignment15PartA import main as email_scraper


class App(tk.Tk):
    """
    This App class inherits from the tkinter TK class, creating the main window in the
    center of the screen, labeling it with the title `email scraper` and includes a UI
    enabling the user to enter the url and attempt to scrape it for a list of email
    Attributes:
        frame_one: a tkinter Frame class
        frame_two: a second tkinter Frame class
        emails_widget: Emails Widget class defined with frame_two as the parent
        entry: a tkinter Entry class defined with frame_one as the parent
    """

    def __init__(self):
        """
        The TK class is initialized with a defined geometry, title, and position
        """
        super().__init__()
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        self.geometry('350x450+700+200')
        self.title("Email Scraper")

        self.canvas = LavaLamp(
            self
        )

        self.frame_one = tk.Frame(
            self.canvas,
        )

        self.frame_two = tk.Frame(
            self.canvas,
        )

        self.emails_widget = EmailsWidget(
            self.frame_two
        )

        self.entry = tk.Entry(
            self.frame_one,
            width=15
        )

        self.btn = tk.Button(
            self.frame_one,
            text="Collect emails",
            command=lambda entry=self.entry: self.scrape(entry)
        )

    @staticmethod
    def clean_url(url: str) -> str or bool:
        """
        This method verifies the url before being passed to the email_scraper method
        :param url: a string representation of the url
        :return: the validated url or a False flag to represent invalid url
        """
        if "https://" not in url:
            url = "https://" + url

        if re.search(r"https://.+\.[a-zA-Z]{3}", url):
            return url
        return False

    def display_emails(self, emails: list, url: str) -> None:
        """
        This method takes a list of emails as an argument add displays them on the
        App class's `emails_widget` attribute. It does a check to close the previous search before
        adding another
        :param emails: a list of emails to be displayed
        :param url: the url which was scraped
        :return: void
        """
        if self.emails_widget.is_packed:
            self.emails_widget.remove()
        self.entry.delete(0, tk.END)
        self.emails_widget.add_emails_and_display(emails, url)

    def scrape(self, entry):
        """
        This method is called by the App class's btn attribute which calls a lambda function passing the
        entry widget to this `scrape` method. The text from the entry is retrieved, validated, then used as the
        `url` parameter in the `email_scaper` method. After a successful scrap of the url a list of emails is generated
        and displayed
        :param entry: the Tkinter Entry widget saved as the attribute  `entry`
        :return: void
        """
        url = entry.get()
        valid_url = self.clean_url(url)
        if valid_url:
            try:
                emails = email_scraper(valid_url)
                self.display_emails(emails, valid_url)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.raise_operational_error(e)
        else:
            self.entry.delete(0, tk.END)
            self.raise_invalid_url_popup(url)

    def raise_operational_error(self, e: Exception) -> None:
        """
        If an undefined error occurs during the scrape method
        the error is displayed on a popup on the screen
        :param e: The Exception that was created
        :return: void
        """
        PopUp(self, "Operation Error Unknown", str(e))

    def raise_invalid_url_popup(self, url: str) -> None:
        """
        If the url handed to the scrape method is unable to be validated a popup is displayed on the screen
        telling the user the given url is not valid
        :param url:
        :return:
        """
        PopUp(self, "Invalid Url Error", f"The url: {url} is not valid please try again with a different url")

    def build(self: tk.Tk) -> tk.Tk:
        """
        This method returns an instance of the App class, or modified TK class, after packing all the widgets
        defined by its attributes
        :return:  TK instance
        """
        self.canvas.build_blobs()
        self.canvas.pack(expand=True, fill="both")
        self.frame_one.pack()
        self.frame_two.pack()
        self.entry.pack()
        self.btn.pack()
        self.emails_widget.pack()
        return self


class PopUp(tk.Toplevel):
    """
    This PopUp class inherits from the tkinter TopLevel class and is used
    to create a popup on window with a title and message passed as arguments to
    the constructor
    """

    def __init__(self, parent: App, title: str, text: str) -> None:
        super().__init__(parent)
        self.geometry("500x150+700+300")
        self.title(title)
        tk.Label(
            self,
            text=text,
            font=('Mistral 12 bold')
        ).place(x=5, y=0)


class EmailsWidget(tk.Text):
    """
    This class inherits from the tkinter Text class and is used to display the list of scraped emails
    returned by the email_scraper method in the App class.
    Attributes:
         is_packed: reflects whether the widget exists on the current App window
    """

    def __init__(self, parent, height=20, width=30):
        """
        This method creates a tkinter Text class adding an attribute and two methods
        :param parent: a tkinter widget to be defined as the parent of this widget
        """
        super().__init__(parent, height=height, width=width)
        self.config(state=tk.DISABLED)
        self.is_packed = False

    def add_emails_and_display(self, emails: list, url: str) -> None:
        """
        This method receives the emails list and adds it to the Text/EmailsWidget  using the
        `insert` method then sets the is_packed attribute to True
        :param url: the url of the emails
        :param emails:  a list of scraped emails
        :return: void
        """
        emails = [url + ": "] + emails
        if len(emails) == 1:
            emails.append("No Emails Found at this url")
        self.config(state=tk.NORMAL)
        self.insert(tk.END, "\n".join(emails))
        self.config(state=tk.DISABLED)
        self.pack()
        self.is_packed = True

    def remove(self):
        """
        This method deletes the content in the Text/EmailsWidget using the `delete` method, unpacks the widget, then
        sets the is_packed attribute to False
        :return:
        """
        self.delete("1.0", "end")
        self.pack_forget()
        self.is_packed = False


class LavaLamp(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent)
        self.blobs = []
        self.blob_colors = [
            "purple",
            "red",
            "green",
            "blue"
        ]

    @staticmethod
    def random_x():
        return random.choice([i for i in range(0, 300)])

    @staticmethod
    def random_speed():
        return random.choice(["fast", "slow"])

    @staticmethod
    def random_size():
        return random.choice(["small", "large"])

    def random_coordinates(self):
        size = self.random_size()
        x1 = self.random_x()
        x2 = 500
        y1 = x1 + 100
        y2 = 400
        random_color = random.choice(self.blob_colors)
        speed = self.random_speed()
        if size == "small":
            y1 -= 50
            y2 += 50
        if speed == "slow":
            speed = float("0." + str(random.randrange(1, 9)))
        elif speed == "fast":
            speed = random.randrange(1, 9)
        return x1, x2, y1, y2, random_color, speed

    def build_blobs(self):
        for i in range(500):
            x1, x2, y1, y2, random_color, speed = self.random_coordinates()
            self.blobs.append(
                Blob(self, x1, x2, y1, y2, random_color, speed)
            )


class Blob:
    def __init__(self, canvas: LavaLamp, x1=0, x2=500, y1=100, y2=400, color='blue', velocity=1):
        self.parent_canvas = canvas
        self.max_y1 = 400
        self.circle = canvas.create_oval(x1, x2, y1, y2, fill=color)
        self.yv = -velocity

    def vibe(self):
        self.parent_canvas.move(self.circle, 0, self.yv)
        coordinates = self.parent_canvas.coords(self.circle)
        if coordinates[3] <= 0 or coordinates[1] > self.parent_canvas.winfo_height():
            self.yv = -self.yv


if __name__ == "__main__":
    app = App()
    app.build()
    while True:
        try:
            for blob in app.canvas.blobs:
                blob.vibe()
            app.update()
            time.sleep(0.01)
        except _tkinter.TclError:
            break
