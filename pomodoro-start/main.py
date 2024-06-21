import tkinter
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
REPS = 1
CHECK = ""
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global TIMER
    if TIMER is not None:
        window.after_cancel(TIMER)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_counter, text="00:00")
    check_level.config(text="")
    global REPS
    REPS = 1

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work")
    elif REPS == 2 or REPS == 4 or REPS == 6:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break")
    else:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(minutes):
    min = math.floor(minutes / 60)
    sec = minutes % 60
    if len(str(sec)) == 1:
        sec = "0" + str(sec)

    canvas.itemconfig(timer_counter, text=f"{min}:{sec}")
    if minutes > 0:
        global TIMER
        TIMER = window.after(1000, count_down, minutes - 1)
    else:
        global REPS
        REPS += 1
        start_timer()
        global CHECK
        if REPS % 2 == 0:
            CHECK += "✓"
            check_level.config(text=CHECK)

# ---------------------------- UI SETUP ------------------------------- #
fg = GREEN

window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=fg, bg=YELLOW)
timer_label.config(pady=5)
timer_label.grid(column=1, row=1)

def start():
    start_timer()
start_button = tkinter.Button(text="Start", command=start, bg=YELLOW)
start_button.grid(column=0, row=3)

reset_button = tkinter.Button(text="Reset", command=reset, bg=YELLOW)
reset_button.grid(column=2, row=3)

check_level = tkinter.Label(text=CHECK, font=(FONT_NAME, 15, "bold"), fg=RED, bg=YELLOW)
check_level.grid(column=1, row=4)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_counter = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

window.mainloop()  # checks every second of events on the screen
