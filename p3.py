import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image , ImageTk
from PIL import Image, ImageFilter
from tkinter import messagebox as messagebox
import fun
import p1

def yesFun():
    enrol= tk.Tk()
    enrol.title("Enrolment Window")
    enrol.geometry("500x400")
    enrol.configure(background="#EC7063")
    enrol.resizable(False,False)
    ST_page=tk.Label(enrol,text='Enrollment Window ',font=('monospace',30,'bold'),fg='#FDEBD0',bg='#EC7063')
    ST_page.place(x=10,y=20)
    ST_ID=tk.Label(enrol,text='Student_ID',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
    ST_ID.place(x=10,y=90)
    st_entry=tk.Entry(enrol,width=30)
    st_entry.place(x=170, y=99)

    cor_ID=tk.Label(enrol,text='Course_ID',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
    cor_ID.place(x=10,y=130)
    cor_entry=tk.Entry(enrol,width=30)
    cor_entry.place(x=170, y=139)
    
    date=tk.Label(enrol,text='Date',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
    date.place(x=10,y=170)
    date=tk.Entry(enrol,width=30)
    date.place(x=170, y=179)

    year=tk.Label(enrol,text='Year',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
    year.place(x=10,y=210)
    year=tk.Entry(enrol,width=30)
    year.place(x=170, y=219)

    en_sub=tk.Button(enrol,text='Enroll',width=10,font=30,fg='#EC7063',bg='#FDEBD0')
    en_sub.place(x=170,y=260)

    back_button=tk.Button(enrol,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[enrol.destroy(),p1.enroll()])
    back_button.place(x=410,y=15)
    
    enrol.mainloop()

def noFun():
    student_win= tk.Tk()
    student_win.title("Student Window")
    student_win.geometry("500x400")
    student_win.configure(background="#EC7063")

    fName=tk.Label(student_win,text='First Name',font=('monospace',13,'bold'),fg='#FDEBD0',bg='#EC7063')
    fName.place(x=10,y=30)
    fName_entry=tk.Entry(student_win,width=30)
    fName_entry.place(x=160, y=35)
    
    lName=tk.Label(student_win,text='Last Name',font=('monospace',13,'bold'),fg='#FDEBD0',bg='#EC7063')
    lName.place(x=10,y=60)
    lName_entry=tk.Entry(student_win,width=30)
    lName_entry.place(x=160, y=65)
    
    age=tk.Label(student_win,text='age',font=('monospace',13,'bold'),fg='#FDEBD0',bg='#EC7063')
    age.place(x=10,y=90)
    age_entry=tk.Entry(student_win,width=30)
    age_entry.place(x=160, y=95)
    
    gender = Label(student_win,text='Gender',font=("Times", "20"),fg='white',bg='#EC7063')
    gender.place(x=10,y=125)
    gender = IntVar()
    radiobutton_1 = Radiobutton(student_win, text='Male', variable=gender, value=1, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
    radiobutton_1.place(x=160, y=125)
    radiobutton_2 = Radiobutton(student_win, text='Female', variable=gender, value=2, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
    radiobutton_2.place(x=250, y=125)
    
    en_sub=tk.Button(student_win,text='GO TO Enrollment page',font=30,fg='#EC7063',bg='#FDEBD0')
    en_sub.place(x=160,y=160)

    back_button=tk.Button(student_win,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[student_win.destroy(),p1.enroll()])
    back_button.place(x=410,y=15)

    #student_win.geometry('400x200+400+300')
    student_win.mainloop()
