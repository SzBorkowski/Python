from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Labels
miles = Label(text="Miles")
miles.grid(column=2, row=0)

equals = Label(text="is equal to")
equals.grid(column=0, row=1)

number = 0
miles_number = Label(text=number)
miles_number.grid(column=1, row=1)

kms = Label(text="Kms")
kms.grid(column=2, row=1)

# Entry
input = Entry(width=10)
input.get()
input.grid(column=1, row=0)

# Button
def convert():
    number = float(input.get())
    km = number * 1.609
    miles_number.config(text=f"{km}")


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
