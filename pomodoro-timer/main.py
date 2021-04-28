from tkinter import *
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#DB524D"
GREEN = "#468E91"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None
paused = False
temp_count = 0
skipped = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    start_button.config(text="Start", command=start_timer)
    global reps
    global paused
    global temp_count
    temp_count = 0
    paused = False
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    global paused
    global skipped
    # Work-(Sound)break-(sound)work-(sound)break-work-break-work-long break
    start_button.config(text="Stop", command=stop_timer)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if paused:
        # count down saved sec
        count_down(temp_count)
        paused = False
    else:
        reps += 1
        if reps % 8 == 0:
            count_down(long_break_sec)
            timer_label.config(text="Break", fg=RED)
        elif reps % 2 == 1:
            count_down(work_sec)
            timer_label.config(text="Work", fg=GREEN)
        else:
            count_down(short_break_sec)
            timer_label.config(text="Break", fg=PINK)
        if reps != 1 and not skipped:
            playsound("alarm.wav")

    skipped = False


def stop_timer():
    window.after_cancel(timer)
    global reps
    reps -= 1
    global paused
    paused = True
    start_button.config(text="Start", command=start_timer)


def skip_timer():
    global paused
    global reps
    global skipped
    if paused:
        paused = False
        reps += 1
    skipped = True
    window.after_cancel(timer)
    start_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global temp_count
    temp_count = count
    count_min = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.resizable(width=False, height=False)
window.iconbitmap("tomato_icon.ico")
window.config(padx=20, bg=YELLOW)

canvas = Canvas(width=250, height=240, bg=YELLOW, highlightthickness=0)
# A way to read through file and get hold of particular file location, you need absolute or relative path if it's in
# different location
tomato_img = PhotoImage(file="tomato.png")
tomato_img = tomato_img.subsample(3, 3)
canvas.create_image(125, 120, image=tomato_img)
timer_text = canvas.create_text(125, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer text
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)
# Check mark
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=4)

# start button
start_button = Button(text="Start", command=start_timer, fg="white", font=(FONT_NAME, 12, "bold"), bg=RED, width=5,
                      relief=GROOVE)
start_button.grid(column=0, row=3)
# reset button
reset_button = Button(text="Reset", command=reset_timer, fg="white", font=(FONT_NAME, 12, "bold"), bg=RED,
                      relief=GROOVE)
reset_button.grid(column=2, row=3)

skip_button = Button(text="Skip", command=skip_timer, fg="white", font=(FONT_NAME, 12, "bold"), bg=RED,
                     relief=GROOVE)
skip_button.grid(column=1, row=3)

window.mainloop()
