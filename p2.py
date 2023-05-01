import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image , ImageTk
from PIL import Image, ImageFilter
from tkinter import messagebox as messagebox
import fun

home=tk.Tk()
home.geometry('800x300+300+300')
home.title("Home")
home.configure(background="#EC7063")

Label1=tk.Label(text='Please Choose if you Student OR employee',font=('monospace',25,'bold'),fg='white',bg='#EC7063')
Label1.place(x=45,y=15)


s_b=tk.Button(text='Student',font=('monospace',20,'bold'),fg='#EC7063',bg='#FDEBD0', width='13',command=lambda:[home.destroy(),fun.st_fun()])
s_b.place(x=100,y=100)



e_b=tk.Button(text='employee',font=('monospace',20,'bold'),fg='#EC7063',bg='#FDEBD0', width='13',command=lambda:[home.destroy(),fun.emp_fun()])
e_b.place(x=400,y=100)




home.mainloop()





