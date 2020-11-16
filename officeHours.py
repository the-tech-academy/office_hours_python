import time
from datetime import datetime
from pytz import timezone
from tkinter import *
import tkinter as tk

win=Tk()

win.title("Office Hour")

portlandOffice = timezone('US/Pacific')
timenow_portland = datetime.now(portlandOffice)
portland_time = timenow_portland.strftime('%I:%M:%S %p ')

newYorkOffice = timezone('US/Eastern')
timenow_newyork = datetime.now(newYorkOffice)
newyork_time = timenow_newyork.strftime('%I:%M:%S  %p')

londonOffice = timezone('Europe/London')
timenow_london = datetime.now(londonOffice)
london_time = timenow_london.strftime('%I:%M:%S  %p')

def portBranch():

    if timenow_portland.hour < 9 or timenow_portland.hour >= 21:
        branch_closed = tk.Label(win, text = "The Portland branch is closed")
        branch_closed.grid(row = 3, column = 2, sticky = "W")
    elif timenow_portland.hour >= 9 or timenow_portland.hour < 21:
        branch_open = tk.Label(win, text = "The Portland branch is open")
        branch_open.grid(row = 3, column = 2, sticky = "W")
    else:
        ("An error has occured")
      

portBranch()

def newYorkBranch():

    if timenow_newyork.hour < 9 or timenow_newyork.hour >= 21:
        branch_closed = tk.Label(win, text = "The New York branch is closed")
        branch_closed.grid(row = 4, column = 2, sticky = "W")
    elif timenow_newyork.hour >= 9 or timenow_newyork.hour < 21:
        branch_open = tk.Label(win, text = "The New York branch is open")
        branch_open.grid(row = 4, column = 2, sticky = "W")
    else:
        ("An error has occured")

newYorkBranch()

def londBranch():

    if timenow_london.hour < 9 or timenow_london.hour >= 21:
        branch_closed = tk.Label(win, text = "The London branch is closed")
        branch_closed.grid(row = 5, column = 2, sticky = "W")
    elif timenow_london.hour >= 9 or timenow_london.hour < 21:
        branch_open = tk.Label(win, text = "The London branch is open")
        branch_open.grid(row = 5, column = 2, sticky = "W")
    else:
        ("An error has occured")

londBranch()

time = datetime.now()

current_time = time.strftime('%I:%M:%S %Z')

current_time_label = tk.Label(win, text = "Current time: ")
current_time_label.grid(row = 0, column = 0, sticky = "W")
timeLabel = tk.Label(win,text=current_time)
timeLabel.grid(row = 0, column = 1)

office_hours_label = tk.Label(win, bg='blue', text="All office hours from: 9:00 am to 9:00, or (0900) (2100)")
office_hours_label.grid(row = 2, columnspan = 1)

portland_label = tk.Label(win, text = "Portland Office: " + portland_time)
portland_label.grid(row = 3, column = 0, sticky = "W")
portland_branch_label = tk.Label(win, text = portBranch())


newyork_label = tk.Label(win, text = "New york Office: " + newyork_time)
newyork_label.grid(row = 4, column = 0, sticky = "W")
newyork_branch_label = tk.Label(win, text = newYorkBranch())



london_label = tk.Label(win, text = "London Office: " + london_time)
london_label.grid(row = 5, column = 0, sticky = "W")
london_branch_label = tk.Label(win, text = londBranch())


win.mainloop()
