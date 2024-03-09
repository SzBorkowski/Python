import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()

def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1, 2, 3, 4)
