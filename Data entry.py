import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("data entry form")

frame = tkinter.Frame(window)
frame.pack()

# saving user info
user_info_frame =tkinter.LabelFrame(frame, text="user informasion")
user_info_frame.grid(row= 0, column=0, pady=20, ipady=20)

first_name_label = tkinter.Label(user_info_frame, text="first name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="last name")
last_name_label.grid(row=0, column=1)

first_name_label = tkinter.Entry(user_info_frame)
last_name_label = tkinter.Entry(user_info_frame)
first_name_label.grid(row=1, column=0)
last_name_label.grid(row=1, column=1)

title = tkinter.label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["apa", "Mr". "Ms", "Dr",])
window.mainloop()