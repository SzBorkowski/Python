from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
pass_entry = Entry(width=34)
pass_entry.grid(column=1, row=3)

# Buttons
pass_gen_button = Button(text="Generate Password")
pass_gen_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
