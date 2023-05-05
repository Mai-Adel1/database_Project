from support import clear_window
from setting import *
import tkinter as tk
from procedures import *
from empsearch import search_win
def emp_win(window,back):
    Label1=tk.Label(text='Select database ',**label_txt)
    Label1.place(x=45,y=15)
    studentdb_button=tk.Button(window,text="Student",**nrom_btn,command=lambda:[clear_window(window),proc_win(window,back,"Student")])
    studentdb_button.place(x=30,y=70)
    studentdb_button=tk.Button(window,text="Insturctor",**nrom_btn,command=lambda:[clear_window(window),proc_win(window,back,"Insturctor")])
    studentdb_button.place(x=30,y=130)
    studentdb_button=tk.Button(window,text="Courses",**nrom_btn,command=lambda:[clear_window(window),proc_win(window,back,"Courses")])
    studentdb_button.place(x=30,y=190) 
    studentdb_button=tk.Button(window,text="Search",**nrom_btn,command=lambda:[clear_window(window),search_win(window)])
    studentdb_button.place(x=600,y=70) 
    back_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),back(window)])
    back_button.place(x=410,y=15)

def proc_win(window,back,name):

    studentdb_button=tk.Button(window,text="Insert",**nrom_btn,command=lambda:[clear_window(window),insert(window,name)])
    studentdb_button.place(x=30,y=70)
    studentdb_button=tk.Button(window,text="Delete",**nrom_btn,command=lambda:[clear_window(window),delete(window,name)])
    studentdb_button.place(x=30,y=190) 
    back_button=tk.Button(window,text="home",**back_btn,command=lambda:[clear_window(window),back(window,name)])
    back_button.place(x=410,y=15)
    if name == "Student" :
        studentdb_button=tk.Button(window,text="Update",**nrom_btn,command=lambda:[clear_window(window),update(window,name)])
        studentdb_button.place(x=30,y=130)
        studentdb_button=tk.Button(window,text="Courses",**nrom_btn,command=lambda:[clear_window(window),std_course_win(window)])
        studentdb_button.place(x=30,y=250)
    
    elif name == "Insturctor":
            studentdb_button=tk.Button(window,text="Update",**nrom_btn,command=lambda:[clear_window(window),update(window,name)])
            studentdb_button.place(x=30,y=130)
            studentdb_button=tk.Button(window,text="Courses",**nrom_btn,command=lambda:[clear_window(window),ins_course_win(window)])
            studentdb_button.place(x=30,y=250)
            studentdb_button=tk.Button(window,text="Add degree",**nrom_btn,command=lambda:[clear_window(window),add_grade(window)])
            studentdb_button.place(x=30,y=310)
