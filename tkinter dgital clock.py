import sys
from tkinter import *
import time

def DCclock():
    curr_time= time.strftime("%H:%M:%S")
    clock.config(text=curr_time)
    clock.after(100,DCclock)

window=Tk()
window.title('Digital Clock')

message= Label(window, font=("Times new roman",100,"italic"), text="Time", fg="red", bg = "light blue")
message.grid(row=0,column=0)
clock= Label(window, font=("Century Gothic",150,"bold"),fg="black", bg = "light grey")
clock.grid(row=1,column=0)
DCclock()
mainloop()