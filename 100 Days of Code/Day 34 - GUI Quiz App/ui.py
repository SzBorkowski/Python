from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.canvas.grid()
        


        self.window.mainloop()