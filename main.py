import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        count_down(work_time)
        reps += 1
        text_timer_label.config(text="Work", fg=GREEN)
        checkmark.config(text="✓")
    elif reps == 1 or reps == 3 or reps == 5:
        count_down(short_break)
        reps += 1
        text_timer_label.config(text="Short Break", fg=PINK)
        checkmark.config(text="")
    elif reps == 7:
        count_down(long_break)
        reps += 1
        text_timer_label.config(text="Long Break", fg=RED)
        checkmark.config(text="")


def count_down(count):
    minute = math.floor(count/60)
    second = count % 60
    if second == 0:
        second = "00"
    elif second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


def reset():
    window.after_cancel(timer)
    text_timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=205, height=225, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, fill="white", font=(FONT_NAME, 20, "bold"), text="00.00")
canvas.grid(row=1, column=1)


text_timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
text_timer_label.grid(row=0, column=1)

start_button = Button(text="Start", width=8, bg=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

start_button = Button(text="Reset", width=8, bg=GREEN, highlightthickness=0, command=reset)
start_button.grid(row=2, column=2)

checkmark = Label(bg=YELLOW, fg=GREEN, font=("Arial", 12, "bold"))
checkmark.grid(row=3, column=1)

window.mainloop()
