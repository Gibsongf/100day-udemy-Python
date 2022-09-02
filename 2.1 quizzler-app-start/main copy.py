import math

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
rep =0
reset= None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(reset)
    canvas.itemconfig(time,text='00:00')
    timer.config(text='Timer')
    check.config(text='')
    global rep
    rep = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global rep
    rep +=1
    work_sec= WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    
    if rep % 8 ==0:
        timer.config(text='Break',fg=RED)
        count_down(long_sec)
    elif rep % 2 ==0:
        timer.config(text='Break',fg=PINK)
        count_down(short_sec)
    else:
        timer.config(text='Work',fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60 
    if sec < 10:
        sec = f'0{sec}'
    canvas.itemconfig(time,text=f'{min}:{sec}')
    if count > 0:
        global reset
        reset = window.after(1000, count_down, count - 1)
    else:
        start_time()
        if rep % 8 !=0 or rep % 2 !=0:
            if rep==1:
                visto = '✓'
                check.config(text=f'{visto}')
            else:
                visto = '✓'
                check.config(text=f'{visto*(rep-1)}')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('POMODORO')
window.config(padx=100, pady=50, bg=YELLOW)

#Image
photo = PhotoImage(file='tomato.png')
canvas=Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100, 112, image=photo)
time = canvas.create_text(100, 130, text='00:00', fill='white',font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2,row=2)

#Label TIMER
timer = Label(text='Timer',font=(FONT_NAME,45,'bold'),fg=GREEN,bg=YELLOW)
timer.grid(column=2,row=1)

#Buttom Start
start = Button(text='Start',font=(FONT_NAME,15,'bold'),command=start_time)
start.grid(column=1,row=3)

#Buttom Reset
reset=Button(text='Reset',font=(FONT_NAME,15,'bold'),command=reset_timer)
reset.grid(column=3,row=3)

#Label check how many time we did it ✓
check = Label(font=(FONT_NAME,20,'bold'),fg=GREEN,bg=YELLOW)
check.grid(column=2,row=3)








window.mainloop()
