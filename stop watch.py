import tkinter as tk
r=tk.Tk()
r.title('stop watch')
stop=tk.Button(r, text='stop', width=25, command=r.destroy)
start=tk.Button(r, text='start', width=25, command=r.destroy)
start.pack()
stop.pack()
r.mainloop()