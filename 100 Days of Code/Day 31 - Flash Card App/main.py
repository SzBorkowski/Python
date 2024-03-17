from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# UI
window = Tk()
window.title("Flash Cards")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=front_img)
canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)

# Reading values
data = pandas.read_csv("wordbank.csv")


window.mainloop()
