

import tkinter as tk

app_win = tk.Tk()

back_gnd = tk.Canvas(app_win)
back_gnd.pack(expand=True, fill='both')

back_gnd_image = tk.PhotoImage(file="image.gif")
back_gnd.create_image(0, 0, anchor='nw', image=back_gnd_image)

button = tk.Button(None, text="Button", bd=1, highlightthickness=0)
back_gnd.create_window(20,20, window=button, anchor='nw')

screen_wight = app_win.winfo_screenmmwidth()
print(screen_wight)
screen_hight = app_win.winfo_screenheight()
print(screen_hight)

app_win.mainloop()

