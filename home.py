import tkinter as tk
from setting import *
from procedures_window import emp_win
from support import clear_window

def home(window):
    
    Label1=tk.Label(text='Welcome to',**wel_label_txt)
    Label1.place(x=40,y=70)
    Label1=tk.Label(text='Student Enroll database',**db_label_txt)
    Label1.place(x=100,y=100)

    emp_btn=tk.Button(text='Continue',**nrom_btn,command=lambda:[clear_window(window),emp_win(window,home)])
    emp_btn.place(x=300,y=200)

def start():
    window=tk.Tk()
    window.geometry(win['geometry'])
    window.title("Student DBMS")
    window.configure(background=win['background'])
    home(window)
    window.mainloop()

    




