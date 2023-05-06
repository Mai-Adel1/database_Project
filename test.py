import tkinter as tk
from setting import *
window=tk.Tk()
window.geometry(win['geometry'])
window.title("Student DBMS")
window.configure(background=win['background'])

id_entry=tk.Entry(window,width=30)
id_entry.place(x=250, y=80)
print(id_entry.get())

window.mainloop()