import time
import webbrowser
from Tkinter import *

time2 = time.strftime('%H:%M:%S')

def a_t_set():
    time_set_label.config(text = "Alarm is set for: "+ time_choice_input.get())
def preview():
    webbrowser.open_new_tab(song_url_input.get())

root = Tk()
song_choice_label = Label(root, text = "Song url")
song_choice_label.grid(row= 0)
time_choice_label = Label(root, text = "Alarm time")
time_choice_label.grid(row=1)
song_url_input = Entry(root)
song_url_input.grid(row=0, column=1)
time_choice_input = Entry(root)
time_choice_input.grid(row=1, column=1)
data_input_button = Button(root, text = 'Enter', command = a_t_set)
data_input_button.grid(column=0, row=4)
song_preview_button = Button(root, text = "Preview", command = preview)
song_preview_button.grid(column=1,row =4)
time_set_label = Label(root, text = "Alarm time: ")
time_set_label.grid(row=7, column=0)

time1 = ''
clock = Label(root, font=('times', 20, 'bold'))
clock.grid(columnspan= 2)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(1000, tick)
    while time2 == time_choice_input.get() :
        preview()
        break
tick()

root.mainloop()
