import tkinter as tk

class UIs(tk.Label):
    def __init__(self, master=None):
        super().__init__(
            master,
            text="Test",
            fg="black",
            bg="white"
            )
        #self.Label(text="Test", fg="black", bg="white")
        #self.title("tkinterのウインドウ")
class Buttons(tk.Button):
    def __init__(self, master=None):
        super().__init__(
            master,
            width=15,
            text="Test",
            )
class EV(tk.Button):
    def __init__(self, master=None):
        super().__init__(master)
        text_arr = ["aiueo", "iueoa", "ueoai", "eoaiu", "oaiue"]
        self.Button(master, text="Test")
        
