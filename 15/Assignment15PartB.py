# Homework 15 Assignment Part B
# Sebastian Campos
# 2022-03-28

import tkinter as tk
import datetime
from Assignment15PartA import MyHTMLParser


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.parser = MyHTMLParser()
        self.tree = {"root": []}

    def __str__(self):
        string = "App Tree\n\nRoot:\n"
        level = 1
        for dictionary in self.tree["root"]:
            string += ('\t'*level)+f"{dictionary['name']}"
            size_of_next_element = len(self.tree['root'][dictionary])
            while size_of_next_element != 0:
                level += 1
                string += ('\t'*level)+f"{}"


    def __repr__(self):
        return str(self)

    def add_widget(self, parent_name, name, widget):
        exists = self.add_to_tree_and_check_if_exists(parent_name, name, widget)
        if exists:
            self.tree[name][-1].pack()
            return
        widget.pack()

    def get_root_widget_names(self):
        return [name for name, _ in self.tree["root"]]

    def add_to_tree_and_check_if_exists(self, parent_name, name, widget):
        if parent_name in self.get_root_widget_names():
            self.tree["root"][parent_name].append({f"{name}": widget})
            return True
        self.tree["root"][parent_name] = [{f"{name}": widget}]
        return False

    def build(self):
        self.add_widget("input box", tk.Entry(self))


if __name__ == "__main__":
    app = App()
    app.build()
    print(app)
    app.mainloop()
