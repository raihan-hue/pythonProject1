from tkinter import *

TkObject = Tk()

label1 = Label(TkObject, text="label 1", bg="red")
label2 = Label(TkObject, text="label 2", bg="darkgreen")
label3 = Label(TkObject, text="label 3", bg="red")

label1.pack()
label2.pack()
label3.pack()

TkObject.mainloop()