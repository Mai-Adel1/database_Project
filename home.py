import tkinter as tk
from setting import *
from procedures_window import emp_win
from support import clear_window

def home(window):
    
    Label1=tk.Label(text='Welcome',**wel_label_txt)
<<<<<<< HEAD
    Label1.place(x=200,y=100)
=======
    Label1.place(x=345,y=100)
>>>>>>> 26c72ff60a2ff406982a40de356b6e6a44c5e17c

    emp_btn=tk.Button(text='Continue',**nrom_btn,command=lambda:[clear_window(window),emp_win(window,home)])
    emp_btn.place(x=320,y=500)

def start():
    window=tk.Tk()
    window.geometry(win['geometry'])
    window.title("Student DBMS")
    window.configure(background=win['background'])
    home(window)
    window.mainloop()

    




