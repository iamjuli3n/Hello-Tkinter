"""A better Hello World for Tkinter"""
import tkinter as tk
from tkinter import ttk

class HelloView(tk.Frame):
    """A friendly little module"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hello")
        name_label = ttk.Label(self, text="Name:")        
        name_entry = ttk.Entry(self, textvariable=self.name)
        ch_button = ttk.Button(self, text="Greet", command=self.on_change)
        hello_label = ttk.Label(self, textvariable=self.hello_string)  # Corrected line
        # Add the widgets to the layout
        name_label.pack()
        name_entry.pack()
        ch_button.pack()
        hello_label.pack()

    def on_change(self):
        self.hello_string.set(f"Hello, {self.name.get()}!")

if __name__ == "__main__":
    root = tk.Tk()
    view = HelloView(root)
    view.pack()
    root.mainloop()
