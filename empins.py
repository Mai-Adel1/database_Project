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
        date1=StringVar(root1)
        root1.geometry("500x400")
        root1.title("Student Enroll")
        root1.configure(background="#EC7063")
        root1.resizable(False,False)
        

        head1=Label(root1,text='Student Database',font=("Times", "25", "bold"),fg='white',bg='#EC7063')
        head1.place(x=30,y=10)

        id= Label(root1,text='Student ID',font=("Times", "20"),fg='white',bg='#EC7063')
        id.place(x=50,y=70)

        fname= Label(root1,text='First name',font=("Times", "20"),fg='white',bg='#EC7063')
        fname.place(x=50,y=110)

        lname = Label(root1,text='Last name',font=("Times", "20"),fg='white',bg='#EC7063')
        lname.place(x=50,y=150)

        gender = Label(root1,text='Gender',font=("Times", "20"),fg='white',bg='#EC7063')
        gender.place(x=50,y=190)

        birthdate = Label(root1,text='Birth Date',font=("Times", "20"),fg='white',bg='#EC7063')
        birthdate.place(x=50,y=230)

        e_id = Entry(root1,width=20)
        e_id.place(x=200,y=80)

        e_fname = Entry(root1,width=20)
        e_fname.place(x=200,y=120)

        e_lname = Entry(root1,width=20)
        e_lname.place(x=200,y=160)

        gender = IntVar()
        radiobutton_1 = Radiobutton(root1, text='Male', variable=gender, value=1, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_1.place(x=200, y=195)
        radiobutton_2 = Radiobutton(root1, text='Female', variable=gender, value=2, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_2.place(x=280, y=195)

        cal=DateEntry(root1,selectmode='day',textvariable=date1)
        cal.place(x=200, y=240)

        insertst_button1=Button(root1,text="Insert",width=8,font=("Times", "15"),fg='#EC7063',bg='#FDEBD0')
        insertst_button1.place(x=25,y=290)

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

        c_name= Label(root2,text='Course name',font=("Times", "20"),fg='white',bg='#EC7063')
        c_name.place(x=50,y=70)

        c_desc= Label(root2,text='Course description',font=("Times", "20"),fg='white',bg='#EC7063')
        c_desc.place(x=50,y=110)

        e_cname = Entry(root2,width=25)
        e_cname.place(x=230,y=80)

        e_cdesc = Text(root2,width=50,height=5)
        e_cdesc.place(x=50,y=150)

        insertst_button2=Button(root2,text="Insert",width=8,font=("Times", "15"),fg='#EC7063',bg='#FDEBD0')
        insertst_button2.place(x=25,y=290)

        back_button=Button(root2,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[root2.destroy(),fun.emp_fun()])
        back_button.place(x=410,y=15)

        
      


def instructor_db_control():
        
        root3= Tk()
        date2=StringVar(root3)
        root3.geometry("500x450")
        root3.title("Student Enroll")
        root3.configure(background="#EC7063")
        root3.resizable(False,False)
        

        head1=Label(root3,text='Instructor Database',font=("Times", "25", "bold"),fg='white',bg='#EC7063')
        head1.place(x=30,y=10)

        id= Label(root3,text='Instructor ID',font=("Times", "20"),fg='white',bg='#EC7063')
        id.place(x=50,y=70)

        fname= Label(root3,text='First name',font=("Times", "20"),fg='white',bg='#EC7063')
        fname.place(x=50,y=110)

        lname = Label(root3,text='Last name',font=("Times", "20"),fg='white',bg='#EC7063')
        lname.place(x=50,y=150)

        gender = Label(root3,text='Gender',font=("Times", "20"),fg='white',bg='#EC7063')
        gender.place(x=50,y=190)

        birthdate = Label(root3,text='Birth Date',font=("Times", "20"),fg='white',bg='#EC7063')
        birthdate.place(x=50,y=230)

        status = Label(root3,text='Status',font=("Times", "20"),fg='white',bg='#EC7063')
        status.place(x=50,y=270)

        e_id = Entry(root3,width=20)
        e_id.place(x=200,y=80)

        e_fname = Entry(root3,width=20)
        e_fname.place(x=200,y=120)

        e_lname = Entry(root3,width=20)
        e_lname.place(x=200,y=160)

        gender = IntVar()
        radiobutton_1 = Radiobutton(root3, text='Male', variable=gender, value=1, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_1.place(x=200, y=195)
        radiobutton_2 = Radiobutton(root3, text='Female', variable=gender, value=2, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_2.place(x=280, y=195)

        cal=DateEntry(root3,selectmode='day',textvariable=date2)
        cal.place(x=200, y=240)

        e_cdesc = Text(root3,width=35,height=5)
        e_cdesc.place(x=200,y=270)

        insertst_button3=Button(root3,text="Insert",width=8,font=("Times", "15"),fg='#EC7063',bg='#FDEBD0')
        insertst_button3.place(x=25,y=380)

        back_button=Button(root3,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[root3.destroy(),fun.emp_fun()])
        back_button.place(x=410,y=15)

       