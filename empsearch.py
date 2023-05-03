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
        def fname():
            #   fnamed=Entry(root1,width=180)
            #   fnamed.place(x=10,y=130)
            #   fnamed.destroy()
              fname= Label(root1,text='First name   ',font=("Times", "20"),fg='white',bg='#EC7063')
              fname.place(x=10,y=130)
              e_fname = Entry(root1,width=20)
              e_fname.place(x=160,y=140)
              search_button=Button(root1,text="search",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0')
              search_button.place(x=10,y=170)
        def lname():
            #   fnamed=Entry(root1,width=180)
            #   fnamed.place(x=10,y=130)
            #   fnamed.destroy()
              lname= Label(root1,text='last name    ',font=("Times", "20"),fg='white',bg='#EC7063')
              lname.place(x=10,y=130)
              e_lname = Entry(root1,width=20)
              e_lname.place(x=160,y=140)
              search_button=Button(root1,text="search",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0')
              search_button.place(x=10,y=170)
        def id():
            #   fnamed=Entry(root1,width=180)
            #   fnamed.place(x=10,y=130)
            #   fnamed.destroy()
              id= Label(root1,text='student id   ',font=("Times", "20"),fg='white',bg='#EC7063')
              id.place(x=10,y=130)
              id = Entry(root1,width=20)
              id.place(x=160,y=140)
              search_button=Button(root1,text="search",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0')
              search_button.place(x=10,y=170)   
        def couname():
            #   fnamed=Entry(root1,width=180)
            #   fnamed.place(x=10,y=130)
            #   fnamed.destroy()
              c_n= Label(root1,text='course name',font=("Times", "20"),fg='white',bg='#EC7063')
              c_n.place(x=10,y=130)
              c_n = Entry(root1,width=20)
              c_n.place(x=160,y=140)
              search_button=Button(root1,text="search",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0')
              search_button.place(x=10,y=170)                     
        gender = IntVar()
        radiobutton_1 = Radiobutton(root1, text='stu_id', variable=gender, value=1,command=id,background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_1.place(x=10, y=10)
        radiobutton_2 = Radiobutton(root1, text='stu_fname', variable=gender, value=2,command=fname, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_2.place(x=10, y=40)
        radiobutton_3 = Radiobutton(root1, text='stu_lname', variable=gender, value=3,command=lname, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_3.place(x=10, y=70)
        radiobutton_4 = Radiobutton(root1, text='course_name', variable=gender, value=3,command=couname, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_4.place(x=10, y=100) 

def course_db_control():
        root1= Tk()
        date1=StringVar(root1)
        root1.geometry("500x400")
        root1.title("Student Enroll")
        root1.configure(background="#EC7063")
        root1.resizable(False,False)
        c_n= Label(root1,text='course_name',font=("Times", "20"),fg='white',bg='#EC7063')
        c_n.place(x=10,y=10)
        c_n = Entry(root1,width=20)
        c_n.place(x=160,y=20) 
        search_button=Button(root1,text="search",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0')
        search_button.place(x=10,y=50)                    
def instructor_db_control():
        root1= Tk()
        date1=StringVar(root1)
        root1.geometry("500x400")
        root1.title("Student Enroll")
        root1.configure(background="#EC7063")
        root1.resizable(False,False)
        def fname():
              fname= Label(root1,text='First name   ',font=("Times", "20"),fg='white',bg='#EC7063')
              fname.place(x=10,y=130)
              e_fname = Entry(root1,width=20)
              e_fname.place(x=160,y=140)
              search_button=Button(root1,text="search",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0')
              search_button.place(x=10,y=170)
        def lname():
              lname= Label(root1,text='last name   ',font=("Times", "20"),fg='white',bg='#EC7063')
              lname.place(x=10,y=130)
              e_lname = Entry(root1,width=20)
              e_lname.place(x=160,y=140)
              search_button=Button(root1,text="search",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0')
              search_button.place(x=10,y=170)
        def id():
              id= Label(root1,text='instructor id',font=("Times", "20"),fg='white',bg='#EC7063')
              id.place(x=10,y=130)
              id = Entry(root1,width=20)
              id.place(x=160,y=140)
              search_button=Button(root1,text="search",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0')
              search_button.place(x=10,y=170)   
        def couname():
              c_n= Label(root1,text='course name  ',font=("Times", "20"),fg='white',bg='#EC7063')
              c_n.place(x=10,y=130)
              c_n = Entry(root1,width=20)
              c_n.place(x=160,y=140)
              search_button=Button(root1,text="search",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0')
              search_button.place(x=10,y=170)                     
        gender = IntVar()
        radiobutton_1 = Radiobutton(root1, text='instructor_id', variable=gender, value=1,command=id,background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_1.place(x=10, y=10)
        radiobutton_2 = Radiobutton(root1, text='instructor_fname', variable=gender, value=2,command=fname, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_2.place(x=10, y=40)
        radiobutton_3 = Radiobutton(root1, text='instructor_lname', variable=gender, value=3,command=lname, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_3.place(x=10, y=70)
        radiobutton_4 = Radiobutton(root1, text='course_name', variable=gender, value=3,command=couname, background = "#EC7063",
                    foreground = "#000000", font = ("Times", 15, "bold"))
        radiobutton_4.place(x=10, y=100) 
         