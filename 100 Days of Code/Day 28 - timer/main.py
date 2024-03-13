from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECKMARK = "✔"
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title_text.config(text="Timer")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_text.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_text.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_text.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            check_marks.config(text=CHECKMARK * int(REPS / 2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.configure(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Napis "Timer"
title_text = Label()
title_text.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_text.grid(column=1, row=0)

# Ptaszki
check_marks = Label()
check_marks.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=4)

# Przycisk "start"
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

# Przycisk "reset"
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
