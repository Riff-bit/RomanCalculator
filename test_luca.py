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


w = Label(root, textvariable=outputVar, relief="sunken").place(x=350, y=150, width=190)
root.geometry("800x381")

e1 = Entry(root, textvariable=inputVar)
e1.place(x=350, y=120)
e1.focus_set()

b = Button(root, text="umwandeln", width=10, command=umwandeln)
b.place(x=350, y=180)

tkvar = StringVar()

choices = ["Arabisch nach Römisch", "Römisch nach Arabisch"]
tkvar.set(choices[1]) # set the default option

popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.place(x=350, y=90)

label2 = Label(root, text="Umwandeln von:")  #Text hinzugefügt
label2.place(x=200, y=90)                          #Text hinzugefüft

lableentry = Label(root, text="Eingabe:")#Text hinzugefügt
lableentry.place(x=250, y=120)

lableausgabe = Label(root, text="Ausgabe:")
lableausgabe.place(x=250, y=150)

bdelete = Button(root, text="Kapitulation!", width=10, command=delete)
bdelete.place(x=225, y=180)


root.mainloop()

