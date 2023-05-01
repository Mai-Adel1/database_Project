import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image , ImageTk
from PIL import Image, ImageFilter
from tkinter import messagebox as messagebox
import fun

window=tk.Tk()
window.geometry("500x400")
window.title("student_enroll")
window.configure(background="#EC7063")

# Label=tk.Label(window,text='Are you have Student_ID?',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
# Label.place(x=40,y=5)


k_b=tk.Button(window,text='Show Courses',font=('monospace',20,'bold'),fg='#EC7063',bg='#FDEBD0', width='13')
k_b.place(x=100,y=110)

i_b=tk.Button(window,text='Enroll',font=('monospace',20,'bold'),fg='#EC7063',bg='#FDEBD0', width='13',command=lambda:[window.destroy(),enroll()])
i_b.place(x=100,y=170)

back_button=tk.Button(window,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[window.destroy(),fun.home_fun()])
back_button.place(x=410,y=15)

# c_b=tk.Button(window,text='Show Courses',font=('monospace',20,'bold'),fg='#EC7063',bg='#FDEBD0', width='13')
# c_b.place(x=100,y=230)

def cor_page():
    print("hi")

# def yesFun():
#     window.destroy()
#     enrol= tk.Tk()
#     enrol.title("Enrolment Window")
#     enrol.geometry("500x400")
#     enrol.configure(background="#EC7063")
#     enrol.resizable(False,False)
#     ST_page=tk.Label(enrol,text='Enrollment Window ',font=('monospace',30,'bold'),fg='#FDEBD0',bg='#EC7063')
#     ST_page.place(x=10,y=20)
#     ST_ID=tk.Label(enrol,text='Student_ID',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
#     ST_ID.place(x=10,y=90)
#     st_entry=tk.Entry(enrol,width=30)
#     st_entry.place(x=170, y=99)

#     cor_ID=tk.Label(enrol,text='Course_ID',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
#     cor_ID.place(x=10,y=130)
#     cor_entry=tk.Entry(enrol,width=30)
#     cor_entry.place(x=170, y=139)
    
#     date=tk.Label(enrol,text='Date',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
#     date.place(x=10,y=170)
#     date=tk.Entry(enrol,width=30)
#     date.place(x=170, y=179)

#     year=tk.Label(enrol,text='Year',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
#     year.place(x=10,y=210)
#     year=tk.Entry(enrol,width=30)
#     year.place(x=170, y=219)

#     en_sub=tk.Button(enrol,text='Enroll',width=10,font=30, command=cor_page,fg='#EC7063',bg='#FDEBD0')
#     en_sub.place(x=170,y=260)

#     enrol.mainloop()

# def noFun():
#     window.destroy()
#     student_win= tk.Tk()
#     student_win.title("Student Window")
#     student_win.geometry("500x400")
#     student_win.configure(background="#EC7063")
#     student_win.resizable(False,False)

#     Name=tk.Label(student_win,text='Name',font=('monospace',13,'bold'),fg='#FDEBD0',bg='#EC7063')
#     Name.place(x=10,y=30)
#     Name_entry=tk.Entry(student_win,width=30)
#     Name_entry.place(x=160, y=35)

#     age=tk.Label(student_win,text='age',font=('monospace',13,'bold'),fg='#FDEBD0',bg='#EC7063')
#     age.place(x=10,y=60)
#     age_entry=tk.Entry(student_win,width=30)
#     age_entry.place(x=160, y=65)

    
    
#     id=tk.Label(student_win,text='ID',font=('monospace',13,'bold'),fg='#FDEBD0',bg='#EC7063')
#     id.place(x=10,y=90)
#     id=tk.Entry(student_win,width=30)
#     id.place(x=160, y=95)

#     co=tk.Label(student_win,text='Courses you want',font=('monospace',13,'bold'),fg='#FDEBD0',bg='#EC7063')
#     co.place(x=10,y=120)
#     co=tk.Entry(student_win,width=30)
#     co.place(x=160, y=125)
    
#     en_sub=tk.Button(student_win,text='GO TO Enrollment page',font=30,fg='#EC7063',bg='#FDEBD0')
#     en_sub.place(x=160,y=155)

#     student_win.geometry('400x200+400+300')
#     student_win.mainloop()

def enroll():
   
   ss= tk.Tk()
   ss.title("Enrolment Window")
   ss.geometry("500x400")
   ss.configure(background="#EC7063")
   ss.resizable(False,False)
   Label=tk.Label(ss,text='Are you have Student_ID?',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
   Label.place(x=40,y=5)
   b1= tk.Button(ss, text='YES',width=5,font=30, fg='#EC7063',bg='#FDEBD0',command=lambda:[ss.destroy(),fun.st_fun2(1)])
   b1.place(x=100,y=60)

   b2= tk.Button(ss, text='NO',width=5,font=30,fg='#EC7063',bg='#FDEBD0',command=lambda:[ss.destroy(),fun.st_fun2(0)])
   b2.place(x=200,y=60)

   back_button=Button(ss,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[ss.destroy(),fun.st_fun()])
   back_button.place(x=410,y=15)

window.mainloop()