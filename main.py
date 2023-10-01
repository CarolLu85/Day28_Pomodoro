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

repos = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global repos
    repos = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_mark.config(text="")
    # i got this one wrong
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repos

    working_mins = WORK_MIN * 60
    short_break_mins = SHORT_BREAK_MIN * 60
    long_break_mins = LONG_BREAK_MIN * 60

    #  i used loop before, but it was wrong, the reason why is that in the count_down() method, there is a "else" statement. inside it
    #  it called the start_timer() method. so no need to double loop it.
    repos += 1
    if repos % 2 != 0:
        count_down(working_mins)
        timer_label.config(text="Working", fg=RED)
    if repos % 2 == 0:
        if repos % 2 == 4:
            count_down(long_break_mins)
            timer_label.config(text="Long Break", fg=PINK)
        else:
            count_down(short_break_mins)
            timer_label.config(text="Short Break", fg=PINK)
    #
    # repos += 1
    # if repos % 8 == 0:
    #     count_down(long_break_mins)
    # elif repos % 2 == 0:
    #     count_down(short_break_mins)
    # else:
    #     count_down(working_mins)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_second = count % 60
    # python dynamic typing
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        # as it already called this start_timer() method, the repos already increased one, so to get this checkmark using if statement,
        # it would test if it % 2 == 0 or not.
        if repos % 2 != 0:
            check_mark.config(text="✔")
        start_timer()
        # or using below codes and below codes might make more sense:
        # marks = ""
        # work_sessions = math.floor(repos/2)
        # for _ in range(work_sessions):
        #     marks += "✔"
        # check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0,font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=4)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=4)

check_mark = Label(fg=GREEN, bg=YELLOW,font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=4)













window.mainloop()