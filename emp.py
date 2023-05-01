import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
import pymysql
#import mysql.connector as mysq
import fun
def select():

    root= Tk()
    root.geometry("500x400")
    root.title("Student Enroll")
    root.configure(background="#EC7063")
    root.resizable(False,False)

    def delete():
       # root.destroy()
        root4= Tk()
        root4.geometry("500x450")
        root4.title("Student Enroll")
        root4.configure(background="#EC7063")
        root4.resizable(False,False)
        studentdb_button=Button(root4,text="Student",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),fun.emp_de(1)])
        studentdb_button.place(x=30,y=10)
        studentdb_button=Button(root4,text="insturctor",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),fun.emp_de(2)])
        studentdb_button.place(x=30,y=70)
        studentdb_button=Button(root4,text="courses",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),fun.emp_de(3)])
        studentdb_button.place(x=30,y=130) 

        back_button=Button(root4,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[root4.destroy(),select()])
        back_button.place(x=410,y=15)
    def insert():
        #root.destroy()
        root4= Tk()
        root4.geometry("500x450")
        root4.title("Student Enroll")
        root4.configure(background="#EC7063")
        root4.resizable(False,False)
        studentdb_button=Button(root4,text="Student",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),fun.emp_in(1)])
        studentdb_button.place(x=30,y=10)
        studentdb_button=Button(root4,text="insturctor",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),fun.emp_in(2)])
        studentdb_button.place(x=30,y=70)
        studentdb_button=Button(root4,text="courses",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),fun.emp_in(3)])
        studentdb_button.place(x=30,y=130)

        back_button=Button(root4,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[root4.destroy(),select()])
        back_button.place(x=410,y=15)
    
    def update():
        #root.destroy()
        root4= Tk()
        root4.geometry("500x450")
        root4.title("Student Enroll")
        root4.configure(background="#EC7063")
        root4.resizable(False,False)
        studentdb_button=Button(root4,text="Student",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),fun.emp_up(1)])
        studentdb_button.place(x=30,y=10) 
        studentdb_button=Button(root4,text="insturctor",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),fun.emp_up(2)])
        studentdb_button.place(x=30,y=70)
        studentdb_button=Button(root4,text="courses",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),fun.emp_up(3)])
        studentdb_button.place(x=30,y=130)
        back_button=Button(root4,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[root4.destroy(),select()])
        back_button.place(x=410,y=15)
    def enroll():
        #root.destroy()
        root4= Tk()
        root4.geometry("500x450")
        root4.title("Student Enroll")
        root4.configure(background="#EC7063")
        root4.resizable(False,False)
        studentdb_button=Button(root4,text="insert",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),insert_E()])
        studentdb_button.place(x=30,y=10)
        studentdb_button=Button(root4,text="delete",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),delete_E()])
        studentdb_button.place(x=30,y=70)

        back_button=Button(root4,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[root4.destroy(),select()])
        back_button.place(x=410,y=15)
        def insert_E():
           enrol= tk.Tk()
           enrol.title("Enrolment Window")
           enrol.geometry("500x400")
           enrol.configure(background="#EC7063")
           enrol.resizable(False,False)
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

           back_button=Button(enrol,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[enrol.destroy(),enroll()])
           back_button.place(x=410,y=15)
           
           
    
           enrol.mainloop()
        def delete_E():
           enrol= tk.Tk()
           enrol.title("Enrolment Window")
           enrol.geometry("500x400")
           enrol.configure(background="#EC7063")
           enrol.resizable(False,False)
           ST_ID=tk.Label(enrol,text='Student_ID',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
           ST_ID.place(x=10,y=90)
           st_entry=tk.Entry(enrol,width=30)
           st_entry.place(x=170, y=99)

           cor_ID=tk.Label(enrol,text='Course_ID',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
           cor_ID.place(x=10,y=130)
           cor_entry=tk.Entry(enrol,width=30)
           cor_entry.place(x=170, y=139)
           en_sub=tk.Button(enrol,text='delete',width=10,font=30,fg='#EC7063',bg='#FDEBD0')
           en_sub.place(x=170,y=260)

           back_button=Button(enrol,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[enrol.destroy(),enroll()])
           back_button.place(x=410,y=15)
    
           enrol.mainloop()
    def teach():
        #root.destroy()
        root4= Tk()
        root4.geometry("500x450")
        root4.title("Student Enroll")
        root4.configure(background="#EC7063")
        root4.resizable(False,False)
        studentdb_button=Button(root4,text="insert",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),insert_t()])
        studentdb_button.place(x=30,y=10)
        studentdb_button=Button(root4,text="delete",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root4.destroy(),delete_t()])
        studentdb_button.place(x=30,y=70)

        back_button=Button(root4,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[root4.destroy(),select()])
        back_button.place(x=410,y=15)
        def insert_t():
           enrol= tk.Tk()
           enrol.title("Enrolment Window")
           enrol.geometry("500x400")
           enrol.configure(background="#EC7063")
           enrol.resizable(False,False)
           ins_ID=tk.Label(enrol,text='instructor_ID',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
           ins_ID.place(x=10,y=90)
           ins_entry=tk.Entry(enrol,width=30)
           ins_entry.place(x=190, y=99)

           cor_ID=tk.Label(enrol,text='Course_ID',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
           cor_ID.place(x=10,y=130)
           cor_entry=tk.Entry(enrol,width=30)
           cor_entry.place(x=190, y=139)
           en_sub=tk.Button(enrol,text='Enroll',width=10,font=30,fg='#EC7063',bg='#FDEBD0')
           en_sub.place(x=170,y=260)

           back_button=Button(enrol,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[enrol.destroy(),teach()])
           back_button.place(x=410,y=15)
    
           enrol.mainloop()
        def delete_t():
           enrol= tk.Tk()
           enrol.title("Enrolment Window")
           enrol.geometry("500x400")
           enrol.configure(background="#EC7063")
           enrol.resizable(False,False)
           ins_ID=tk.Label(enrol,text='instructor_ID',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
           ins_ID.place(x=10,y=90)
           ins_entry=tk.Entry(enrol,width=30)
           ins_entry.place(x=190, y=99)

           cor_ID=tk.Label(enrol,text='Course_ID',font=('monospace',20,'bold'),fg='#FDEBD0',bg='#EC7063')
           cor_ID.place(x=10,y=130)
           cor_entry=tk.Entry(enrol,width=30)
           cor_entry.place(x=190, y=139)
           en_sub=tk.Button(enrol,text='delete',width=10,font=30,fg='#EC7063',bg='#FDEBD0')
           en_sub.place(x=170,y=260)

           back_button=Button(enrol,text="Back",width=5,font=("Times", "15"),fg='black',bg='#EC7063',activeforeground="#EC7063",command=lambda:[enrol.destroy(),enroll()])
           back_button.place(x=410,y=15)
    
           enrol.mainloop()
    head=Label(root,text='Select Database',font=("Times", "25", "bold"),fg='white',bg='#EC7063')
    head.place(x=30,y=10)

    in_button=Button(root,text="insert",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root.destroy(),insert()])
    in_button.place(x=50,y=70)
    del_button=Button(root,text="delete",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root.destroy(),delete()])
    del_button.place(x=50,y=130)
    update_button=Button(root,text="update",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root.destroy(),update()])
    update_button.place(x=50,y=190)
    enrol_button=Button(root,text="enrol",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root.destroy(),enroll()])
    enrol_button.place(x=50,y=250)
    teach_button=Button(root,text="TEACH",width=15,font=("Times", "20"),fg='#EC7063',bg='#FDEBD0',command=lambda:[root.destroy(),teach()])
    teach_button.place(x=50,y=310) 


    root.mainloop()

select()