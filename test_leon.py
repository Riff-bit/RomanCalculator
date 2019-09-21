from tkinter import *
from tkinter import ttk
import roman



def umwandeln():
    arab = arabicVar.get()
    direction = tkvar.get()
    if direction == choices[0]:
        romanVar.set(roman.fromArabic(int(arab)))
    elif direction == choices[1]:
        romanVar.set(roman.toArabic(arab))

root = Tk()

arabicVar = StringVar()
romanVar = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=9, row=7, sticky=(N, W, E, S))

w = Label(root, textvariable=romanVar).grid(row=0)
root.geometry("500x500")

e1 = Entry(root, textvariable=arabicVar)
e1.grid(row=1, column=2)
e1.focus_set()

b = Button(root, text="umwandeln", width=10, command=umwandeln)
b.grid(row=7)

tkvar = StringVar()

choices = ["Arabisch nach Römisch", "Römisch nach Arabisch"]
tkvar.set(choices[1]) # set the default option

popupMenu = OptionMenu(root, tkvar, *choices)
Label(root, text="Choose a dish").grid
popupMenu.grid(row=0, column=8,)

root.mainloop()