import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkcalendar import DateEntry
from PIL import Image , ImageTk
from PIL import Image, ImageFilter
from tkinter import messagebox as messagebox
import fun
def student_db_control():
        root1= Tk()
        root1.geometry("500x400")
        root1.title("Student Enroll")
        root1.configure(background="#EC7063")
        root1.resizable(False,False)
        

        head1=Label(root1,text='Student Database',font=("Times", "25", "bold"),fg='white',bg='#EC7063')
        head1.place(x=30,y=10)

        id= Label(root1,text='Student ID',font=("Times", "20"),fg='white',bg='#EC7063')
        id.place(x=50,y=70)
        e_id = Entry(root1,width=20)
        e_id.place(x=50,y=100)
        insertst_button1=Button(root1,text="Delete",width=8,font=("Times", "15"),fg='#EC7063',bg='#FDEBD0')
        insertst_button1.place(x=25,y=150)

        back_button=Button(root1,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[root1.destroy(),fun.emp_fun()])
        back_button.place(x=410,y=15)

       


def course_db_control():
       
        root2= Tk()
        #data2=StringVar(root2)
        root2.geometry("500x400")
        root2.title("Student Enroll")
        root2.configure(background="#EC7063")
        root2.resizable(False,False)
        

        head1=Label(root2,text='Courses Database',font=("Times", "25", "bold"),fg='white',bg='#EC7063')
        head1.place(x=30,y=10)

        c_id= Label(root2,text='Course id',font=("Times", "20"),fg='white',bg='#EC7063')
        c_id.place(x=50,y=70)
        e_cid = Entry(root2,width=25)
        e_cid.place(x=50,y=100)


        det_button2=Button(root2,text="delete",width=8,font=("Times", "15"),fg='#EC7063',bg='#FDEBD0')
        det_button2.place(x=25,y=290)

        back_button=Button(root2,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[root2.destroy(),fun.emp_fun()])
        back_button.place(x=410,y=15)
      


def instructor_db_control():
        
        root3= Tk()
        root3.geometry("500x450")
        root3.title("Student Enroll")
        root3.configure(background="#EC7063")
        root3.resizable(False,False)
        

        head1=Label(root3,text='Instructor Database',font=("Times", "25", "bold"),fg='white',bg='#EC7063')
        head1.place(x=30,y=10)

        id= Label(root3,text='Instructor ID',font=("Times", "20"),fg='white',bg='#EC7063')
        id.place(x=50,y=70)

        
        e_id = Entry(root3,width=20)
        e_id.place(x=50,y=110)

        

        delst_button3=Button(root3,text="Delete",width=8,font=("Times", "15"),fg='#EC7063',bg='#FDEBD0')
        delst_button3.place(x=25,y=290)

        back_button=Button(root3,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[root3.destroy(),fun.emp_fun()])
        back_button.place(x=410,y=15)
