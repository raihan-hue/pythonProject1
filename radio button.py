from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='GFG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='MI', variable=v, value=3).pack(anchor=W)

mainloop()