from support import clear_window
from setting import *
import tkinter as tk
from tkcalendar import DateEntry
from procedures import *
from empsearch import search_win
import home

def contains_number(string):
    return any(char.isdigit() for char in string)

def emp_win(window, back):
    Label1 = tk.Label(text='Select database ', **label_txt)
    Label1.place(x=45, y=15)
    studentdb_button = tk.Button(window, text="Student", **nrom_btn, command=lambda: [
                                 clear_window(window), proc_win(window, back, "Student")])
    studentdb_button.place(x=30, y=70)
    studentdb_button = tk.Button(window, text="Insturctor", **nrom_btn, command=lambda: [
                                 clear_window(window), proc_win(window, back, "Instructor")])
    studentdb_button.place(x=30, y=130)
    studentdb_button = tk.Button(window, text="Courses", **nrom_btn, command=lambda: [
                                 clear_window(window), proc_win(window, back, "Courses")])
    studentdb_button.place(x=30, y=190)
    studentdb_button = tk.Button(window, text="Search", **nrom_btn,
                                 command=lambda: [clear_window(window), search_win(window)])
    studentdb_button.place(x=600, y=70)
    back_button = tk.Button(window, text="Back", **back_btn
                            ,command=lambda:[clear_window(window),home(window)])
    back_button.place(x=410, y=15)


def proc_win(window, back, name):

    studentdb_button = tk.Button(window, text="Insert", **nrom_btn,
                                 command=lambda: [clear_window(window), insert(window, name)])
    studentdb_button.place(x=30, y=70)
    studentdb_button = tk.Button(window, text="Delete", **nrom_btn,
                                 command=lambda: [clear_window(window), delete(window, name)])
    studentdb_button.place(x=30, y=190)
    back_button = tk.Button(window, text="home", **back_btn,
                            command=lambda: [clear_window(window), back(window)])
    back_button.place(x=410, y=15)
    if name == "Student":
        studentdb_button = tk.Button(window, text="Update", **nrom_btn,
                                     command=lambda: [clear_window(window), update(window, name)])
        studentdb_button.place(x=30, y=130)
        studentdb_button = tk.Button(window, text="Courses", **nrom_btn,
                                     command=lambda: [clear_window(window), std_course_win(window)])
        studentdb_button.place(x=30, y=250)

    elif name == "Instructor":
        studentdb_button = tk.Button(window, text="Update", **nrom_btn,
                                     command=lambda: [clear_window(window), update(window, name)])
        studentdb_button.place(x=30, y=130)
        studentdb_button = tk.Button(window, text="Courses", **nrom_btn, command=lambda: [
            clear_window(window), ins_course_win(window)])
        studentdb_button.place(x=30, y=250)
        studentdb_button = tk.Button(
            window, text="Add degree", **nrom_btn, command=lambda: [clear_window(window), add_grade(window)])
        studentdb_button.place(x=30, y=310)

def insert(window,name):
        
        head=tk.Label(window,text="Insert "+name,**label_txt)
        head.place(x=30,y=10)
        if name == 'Courses':
            fname= tk.Label(window,text='Name',**label_txt)
            fname.place(x=50,y=70)

            fname= tk.Label(window,text='Description',**label_txt)
            fname.place(x=50,y=150)

            e_name = tk.Entry(window,width=20)
            e_name.place(x=200,y=70)

            e_cdesc = tk.Text(window,width=50,height=5)
            e_cdesc.place(x=200,y=150)
            
        else:        
            
            fname= tk.Label(window,text='First name',**label_txt)
            fname.place(x=50,y=70)

            lname = tk.Label(window,text='Last name',**label_txt)
            lname.place(x=50,y=110)
    
            gender = tk.Label(window,text='Gender',**label_txt)
            gender.place(x=50,y=150)
            date =tk.StringVar(window)
            birthdate = tk.Label(window,text='Birth Date',**label_txt)
            birthdate.place(x=50,y=190)
    
            e_fname = tk.Entry(window,width=20)
            e_fname.place(x=200,y=80)
    
            e_lname = tk.Entry(window,width=20)
            e_lname.place(x=200,y=120)
    
            gender = tk.IntVar()
            radiobutton_1 = tk.Radiobutton(window, text='Male', variable=gender, value=1,**radio_btn )
            radiobutton_1.place(x=200, y=160)
            radiobutton_2 = tk.Radiobutton(window, text='Female', variable=gender, value=2, **radio_btn)
            radiobutton_2.place(x=280, y=160)
    
            cal=DateEntry(window,selectmode='day',textvariable=date)
            cal.place(x=200, y=200)
        
        error_label = tk.Label(window, text="", bg='#EC7063')
        error_label.place(x=50,y=270)
        def check():
            if name == 'Courses':
                try:
                        name_c = e_name.get()
                        desc_c = e_cdesc.get("1.0","end-1c")
                        insert_error_hand_courses(name,name_c,desc_c)
                        if contains_number(name_c):
                           raise ValueError("Please enter a string value")
                except ValueError as e:
                        error_label.config(text=e)
                except Exception as e:
                        error_label.config(text=e)
                else:
                        error_label.config(text="insertion is done successfully")
            else:
                try:
                 fname_si = e_fname.get()
                 lname_si = e_lname.get()
                 birth_si = cal.get_date()
                 gend_si = gender
                 insert_error_hand_si(name,fname_si,lname_si,birth_si,gend_si)
                 if contains_number(fname_si) or contains_number(lname_si) :
                           raise ValueError("Please enter a string value")
                except ValueError as e:
                 error_label.config(text=e)
                except Exception as E:
                  error_label.config(text=E)
                else:
                  error_label.config(text="insertion is done succesfully")
    
        insertst_button1=tk.Button(window,text="Insert",**nrom_btn,command=check)
        insertst_button1.place(x=25,y=240)
        insertback_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),proc_win(window,home,name)])
        insertback_button.place(x=400,y=20)



def update(window,name):
        flag = False
        head1=tk.Label(window,text="Update" + name,**label_txt)
        head1.place(x=30,y=10)

        id= tk.Label(window,text='Enter your ID',**label_txt)
        id.place(x=50,y=70)

        id_entry=tk.Entry(window,width=30)
        id_entry.place(x=250, y=80)

        updateback_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),proc_win(window,home,name)])
        updateback_button.place(x=500,y=20)

        q=tk.Label(window,text='choose Field',**label_txt)
        q.place(x=50,y=150)

        choices = tk.IntVar()
        fname_rd = tk.Radiobutton(window, text='First Name', variable=choices, value=1, **radio_btn,command=lambda:[update_field(window,'First Name')])
        fname_rd.place(x=200, y=190)
        lname_rd = tk.Radiobutton(window, text='Last Name', variable=choices, value=2, **radio_btn,command=lambda:[update_field(window,'Last Name')])
        lname_rd.place(x=200, y=230)
        age_rd = tk.Radiobutton(window, text='Age', variable=choices, value=3, **radio_btn ,command=lambda:[update_field(window,"Age")])
        age_rd.place(x=200, y=270)
widgets_list =[]
def update_field(window,filed):
        
        for widgets in widgets_list:
            widgets.destroy()

        if filed == 'Age':
            birthdate = tk.Label(window,text='Birth Date',**label_txt)
            birthdate.place(x=50,y=400)
            widgets_list.append(birthdate)
            date =tk.StringVar(window)
            cal=DateEntry(window,selectmode='day',textvariable=date)
            cal.place(x=200, y=400)
            widgets_list.append(cal)
        else:    
            e_field = tk.Entry(window,width=20)
            e_field.place(x=200,y=400)
            widgets_list.append(e_field)

            l_field= tk.Label(window,text=filed,**label_txt)
            l_field.place(x=50,y=400)
            widgets_list.append(l_field)
        update_btn=tk.Button(window,text="Delete",**nrom_btn)
        update_btn.place(x=25,y=150)
        



def delete(window ,name):
        head=tk.Label(window,text='Delete' + name,**label_txt)
        head.place(x=30,y=10)

        id= tk.Label(window,text=name+' ID',**label_txt)
        id.place(x=50,y=70)
        e_id = tk.Entry(window,width=20)
        e_id.place(x=50,y=100)
        deleteback_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),proc_win(window,home,name)])
        deleteback_button.place(x=500,y=20)
        error_label = tk.Label(window, text="", bg='#EC7063')
        error_label.place(x=50,y=130)
        def check():
         try:
          ce = int(e_id.get())
          delt_error_hand(name, ce)
         except ValueError:
           error_label.config(text="please enter int value")

         except Exception as E:
           error_label.config(text=E)
         else:
           error_label.config(text="deletion is done succesfully")

        del_btn=tk.Button(window,text="Delete",**nrom_btn,command=check)
        del_btn.place(x=25,y=150)

def std_course_win(window):
    studentdb_button=tk.Button(window,text="insert",**nrom_btn,command=lambda:[clear_window(window),enroll_course(window)])
    studentdb_button.place(x=30,y=10)
    studentdb_button=tk.Button(window,text="delete",**nrom_btn,command=lambda:[clear_window(window),delete_course(window)])
    studentdb_button.place(x=30,y=70)

    back_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),emp_win(window,home)])
    back_button.place(x=500,y=20)
        

def enroll_course(window):
    ST_ID=tk.Label(window,text='Student ID',**label_txt)
    ST_ID.place(x=10,y=90)
    st_entry=tk.Entry(window,width=30)
    st_entry.place(x=170, y=99)
    cor_ID=tk.Label(window,text='Course ID',**label_txt)
    cor_ID.place(x=10,y=130)
    cor_entry=tk.Entry(window,width=30)
    cor_entry.place(x=170, y=139)
    date=tk.Label(window,text='Date',**label_txt)
    date.place(x=10,y=170)
    date=tk.Entry(window,width=30)
    date.place(x=170, y=179)
    year=tk.Label(window,text='Year',**label_txt)
    year.place(x=10,y=210)
    year=tk.Entry(window,width=30)
    year.place(x=170, y=219)
    

    error_label = tk.Label(window, text="", bg='#EC7063')
    error_label.place(x=50,y=290)
   
    def check():
        try:
         studentID = int(st_entry.get())
         courseID = int(cor_entry.get())
         Date = int(date.get())  
         Year = int(year.get())

         insert_error_hand_enroll('Enroll', studentID,courseID,Date,Year)       

        except ValueError:
           error_label.config(text="please enter int value")

        except Exception as E:
           error_label.config(text=E)
        else:
           error_label.config(text="Enrollmaent is done succesfully")

    en_sub=tk.Button(window,text='Enroll',**nrom_btn,command=check)
    en_sub.place(x=170,y=260)
    back_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),emp_win(window,home)])
    back_button.place(x=500,y=20)




def delete_course(window):     
    ST_ID=tk.Label(window,text='Student ID',**nrom_btn)
    ST_ID.place(x=10,y=90)
    st_entry=tk.Entry(window,width=30)
    st_entry.place(x=170, y=99)

    cor_ID=tk.Label(window,text='Course ID',**label_txt)
    cor_ID.place(x=10,y=130)
    cor_entry=tk.Entry(window,width=30)
    cor_entry.place(x=170, y=139)
    error_label = tk.Label(window, text="", bg='#EC7063')
    error_label.place(x=50, y=130)
    back_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),emp_win(window,home)])
    back_button.place(x=500,y=20)

    def check():
        try:
          co_id = int(cor_entry.get())
          st_id= int(st_entry.get())
          delt_error_hand_enroll('Enroll', co_id,st_id)
        except ValueError:
           error_label.config(text="please enter int value")

        except Exception as E:
           error_label.config(text=E)
        else:
           error_label.config(text="deletion is done succesfully")
    en_sub=tk.Button(window,text='delete',**nrom_btn,command=check)
    en_sub.place(x=170,y=260)

def ins_course_win(window):
    studentdb_button=tk.Button(window,text="insert",**nrom_btn,command=lambda:[clear_window(window),insert_t(window)])
    studentdb_button.place(x=30,y=10)
    studentdb_button=tk.Button(window,text="delete",**nrom_btn,command=lambda:[clear_window(window),delete_t(window)])
    studentdb_button.place(x=30,y=70)
    back_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),emp_win(window,home)])
    back_button.place(x=500,y=20)
    
def insert_t(window):
    ins_ID=tk.Label(window,text='instructor ID',**label_txt)
    ins_ID.place(x=10,y=90)
    ins_entry=tk.Entry(window,width=30)
    ins_entry.place(x=190, y=99)
    cor_ID=tk.Label(window,text='Course ID',**label_txt)
    cor_ID.place(x=10,y=130)
    cor_entry=tk.Entry(window,width=30)
    cor_entry.place(x=190, y=139)

    error_label = tk.Label(window, text="", bg='#EC7063')
    error_label.place(x=50,y=290)
   
    def check():
        try:
         instructorID = int(ins_entry.get())
         courseID = int(cor_entry.get())
         

         insert_error_hand_enroll_teach('Teach', instructorID, courseID)       

        except ValueError:
           error_label.config(text="please enter int value")

        except Exception as E:
           error_label.config(text=E)
        else:
           error_label.config(text="Enrollmaent is done succesfully")

    en_sub=tk.Button(window,text='Enroll',**label_txt,command=check)
    en_sub.place(x=170,y=260)
    back_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),emp_win(window,home)])
    back_button.place(x=500,y=20)


def delete_t(window):
    ins_ID=tk.Label(window,text='instructor ID',**label_txt)
    ins_ID.place(x=10,y=90)
    ins_entry=tk.Entry(window,width=30)
    ins_entry.place(x=190, y=99)
    cor_ID=tk.Label(window,text='Course ID',**label_txt)
    cor_ID.place(x=10,y=130)
    cor_entry=tk.Entry(window,width=30)
    cor_entry.place(x=190, y=139)
    error_label = tk.Label(window, text="", bg='#EC7063')
    error_label.place(x=50, y=150)
    back_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),emp_win(window,home)])
    back_button.place(x=500,y=20)

    def check():
        try:
            co_id = int(cor_entry.get())
            ins_id = int(ins_entry.get())
            delt_error_hand_enroll('Teach', co_id, ins_id)
        except ValueError:
            error_label.config(text="please enter int value")

        except Exception as E:
            error_label.config(text=E)
        else:
            error_label.config(text="deletion is done succesfully")
    en_sub=tk.Button(window,text='delete',**nrom_btn,command=check)
    en_sub.place(x=170,y=260)

def add_grade(window):
    ins_ID=tk.Label(window,text='ID',**label_txt)
    ins_ID.place(x=10,y=90)

    ins_entry=tk.Entry(window,width=30)
    ins_entry.place(x=190, y=90)

    degree=tk.Label(window,text='Degree',**label_txt)
    degree.place(x=10,y=130)

    degree_entry=tk.Entry(window,width=30)
    degree_entry.place(x=190, y=130)

    univeristy=tk.Label(window,text='University',**label_txt)
    univeristy.place(x=10,y=170)

    univeristy_entry=tk.Entry(window,width=30)
    univeristy_entry.place(x=190, y=170)

    year=tk.Label(window,text='year',**label_txt)
    year.place(x=10,y=210)
    
    year=tk.Entry(window,width=30)
    year.place(x=190, y=210)

    back_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),emp_win(window,home)])
    back_button.place(x=500,y=20)
#################################################################################

    