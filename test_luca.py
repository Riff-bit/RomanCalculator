from tkinter import *
from tkinter import ttk
import roman



def umwandeln():
    arab = arabicVar.get()
    direction = tkvar.get()
    if direction == choices[0]:
        romanVar.set(roman.fromArabic(int(arab)))
    elif direction == choices[1]:
        result = roman.toArabic(arab)
        if result > 0:
            romanVar.set(result)
        else:
            romanVar.set("Immutabilis!")

root = Tk()
root.title("Umrechner Römisch / Arabisch")

arabicVar = StringVar()
romanVar = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=9, row=7, sticky=(N, W, E, S))

w = Label(root, textvariable=romanVar).grid(row=2, column=3, sticky = W)
root.geometry("500x500")

e1 = Entry(root, textvariable=arabicVar)
e1.grid(row=1, column=3)
e1.focus_set()

b = Button(root, text="umwandeln", width=10, command=umwandeln)
b.grid(row=3, column=4)

tkvar = StringVar()

choices = ["Arabisch nach Römisch", "Römisch nach Arabisch"]
tkvar.set(choices[1]) # set the default option

popupMenu = OptionMenu(root, tkvar, *choices)

popupMenu.grid(row=0, column=3,)

label2 = Label(root, text="Umwandeln von:")  #Text hinzugefügt
label2.grid(row=0, column=2)                          #Text hinzugefüft

lableentry = Label(root, text="Eingabe:")#Text hinzugefügt
lableentry.grid(row=1, column=2)

lableausgabe = Label(root, text="Ausgabe")
lableausgabe.grid(row=2, column=2)

lableleer = Label(root, text="      ")
lableleer.grid(row=0)
root.mainloop()