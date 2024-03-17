from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# UI
window = Tk()
window.title("Flash Cards")
window.configure(padx=20, pady=20)

language_label = Label(text="Language")
language_label.grid(column=1, row=1)
word_label = Label(text="word")
word_label.grid(column=1, row=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=3)
right_img =PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=3)



window.mainloop()
