from tkinter import *

# constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
COMPLETED = 0
timer = None


def reset_timer():
    '''reset everything when function is called'''
    global REPS
    global COMPLETED

    window.after_cancel(timer)
    REPS = 0
    COMPLETED = 0
    header_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 38))
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


def start_timer():
    '''
    Timer mechanism - Updates the GUI and sets the timer based on which type of session
    the user is in.
    '''
    global REPS
    global COMPLETED

    REPS += 1
    work_count = int(WORK_MIN * 60)
    short_count = int(SHORT_BREAK_MIN * 60)
    long_count = int(LONG_BREAK_MIN * 60)

    if REPS % 8 == 0:
        header_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 38))
        count_down(long_count)
    elif REPS % 2 == 0:
        header_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 38))
        count_down(short_count)
    else:
        COMPLETED += 1
        header_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 38))
        count_down(work_count)
    

def count_down(count):
    '''
    Countdown mechanism - updates and displays the remaining time and adds checkmarks
    for each completed work session.
    '''
    count_min = count // 60
    count_sec = count % 60
    remaining_time = f'{count_min:02d}:{count_sec:02d}'

    canvas.itemconfig(timer_text, text=remaining_time)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        checkmark_text = "✔" * COMPLETED
        check_label.config(text=checkmark_text)
        start_timer()


# set up GUI
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)

# set up image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# header text
header_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 38))
header_label.grid(column=1, row=0)

# set up start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# set up reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# set up check marks
check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
