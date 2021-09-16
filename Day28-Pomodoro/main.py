from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
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


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    title.config(text="Timer", fg=GREEN)
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        minutes = LONG_BREAK_MIN
        check.config(text=check["text"]+"✔")
        title.config(text="Break", fg=RED)
    elif reps % 8 in [2, 4, 6]:
        check.config(text=check["text"] + "✔")
        minutes = SHORT_BREAK_MIN
        title.config(text="Break", fg=PINK)
    elif reps % 8 in [1, 3, 5, 7]:
        minutes = WORK_MIN
        title.config(text="Work", fg=GREEN)
    count_down(minutes*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def secs_to_mins(num):
    mins = num // 60
    secs = num % 60
    return f"{mins:02d}:{secs:02d}"


def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=secs_to_mins(count))
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# Tomato picture
canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Labels
title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 34, "bold"))
title.grid(column=1, row=0)
check = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14))
check.grid(column=1, row=3, pady=7)

# Buttons
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)


window.mainloop()