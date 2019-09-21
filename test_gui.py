from tkinter import *
from tkinter import ttk
import roman

def umwandeln():
    arab = arabicVar.get()
    print(arab, type(arab))
    romanVar.set(roman.fromArabic(int(arab)))

root = Tk()

arabicVar = StringVar()
romanVar = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

w = Label(root, textvariable=romanVar).grid(row=0)

e1 = Entry(root, textvariable=arabicVar)
e1.grid(row=0, column=1)
e1.focus_set()

b = Button(root, text="umwandeln", width=10, command=umwandeln)
b.grid(row=2)

root.mainloop()