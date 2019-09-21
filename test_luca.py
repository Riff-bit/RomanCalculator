from tkinter import *
from tkinter import ttk
import roman

def delete():
    inputVar.set("")
    outputVar.set("")

def umwandeln():
    arab = inputVar.get()
    direction = tkvar.get()
    if direction == choices[0]:
        outputVar.set(roman.fromArabic(int(arab)))
    elif direction == choices[1]:
        result = roman.toArabic(arab)
        if result > 0:
            outputVar.set(result)
        else:
            outputVar.set("Immutabilis!")

root = Tk()
root.title("Umrechner Römisch / Arabisch")


bg_image = PhotoImage(file="bg-image.gif")
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

inputVar = StringVar()
outputVar = StringVar()

w = Label(root, textvariable=outputVar).grid(row=2, column=3, sticky = W)
root.geometry("800x381")

e1 = Entry(root, textvariable=inputVar)
e1.grid(row=1, column=3)
e1.focus_set()

b = Button(root, text="umwandeln", width=10, command=umwandeln)
b.grid(row=3, column=4)

tkvar = StringVar()

choices = ["Arabisch nach Römisch", "Römisch nach Arabisch"]
tkvar.set(choices[1]) # set the default option

popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.grid(row=0, column=3, pady='20')

label2 = Label(root, text="Umwandeln von:")  #Text hinzugefügt
label2.grid(row=0, column=2)                          #Text hinzugefüft

lableentry = Label(root, text="Eingabe:")#Text hinzugefügt
lableentry.grid(row=1, column=2)

lableausgabe = Label(root, text="Ausgabe")
lableausgabe.grid(row=2, column=2)

bdelete = Button(root, text="Kapitulation!", width=10, command=delete)
bdelete.grid(row=3, column=3, sticky=E)


root.mainloop()

