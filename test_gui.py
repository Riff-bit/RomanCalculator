from tkinter import *
from tkinter import ttk

root = Tk()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

w = Label(root, text="Hello Tkinter!").grid(row = 0)


e1 = Entry(root)

e1.grid(row = 0, column = 1)


root.mainloop()