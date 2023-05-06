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
    Label1 = tk.Label(text='Select DataBase ', **label_txt)
    Label1.place(x=30, y=15)
    studentdb_button = tk.Button(window, text="Student", **nrom_btn, command=lambda: [
                                 clear_window(window), proc_win(window, back, "Student")])
    studentdb_button.place(x=90, y=80)
    studentdb_button = tk.Button(window, text="Insturctor", **nrom_btn, command=lambda: [
                                 clear_window(window), proc_win(window, back, "Instructor")])
    studentdb_button.place(x=90, y=150)
    studentdb_button = tk.Button(window, text="Courses", **nrom_btn, command=lambda: [
                                 clear_window(window), proc_win(window, back, "Courses")])
    studentdb_button.place(x=90, y=220)
    studentdb_button = tk.Button(window, text="Search", **nrom_btn,
                                 command=lambda: [clear_window(window), search_win(window)])
    studentdb_button.place(x=550, y=80)
    back_button = tk.Button(window, text="Back", **back_btn
                            ,command=lambda:[clear_window(window),home.home(window)])
    back_button.place(x=550, y=15)


def proc_win(window, back, name):
    Label1 = tk.Label(text=name + ' DataBase', **label_txt)
    Label1.place(x=30, y=15)

    studentdb_button = tk.Button(window, text="Insert", **nrom_btn,
                                 command=lambda: [clear_window(window), insert(window, name)])
    # studentdb_button.place(x=30, y=70)
    studentdb_button.place(x=90, y=80)
    studentdb_button = tk.Button(window, text="Delete", **nrom_btn,
                                 command=lambda: [clear_window(window), delete(window, name)])
    studentdb_button.place(x=90, y=150)
    back_button = tk.Button(window, text="home", **back_btn,
                            command=lambda: [clear_window(window), home.home(window)])
    back_button.place(x=550, y=15)
    back_button = tk.Button(window, text="Back", **back_btn
                            ,command=lambda:[clear_window(window),emp_win(window,home)])
    back_button.place(x=630, y=15)
    if name == "Student":
        studentdb_button = tk.Button(window, text="Update", **nrom_btn,
                                     command=lambda: [clear_window(window), update(window, name)])
        studentdb_button.place(x=90, y=220)
        studentdb_button = tk.Button(window, text="Courses", **nrom_btn,
                                     command=lambda: [clear_window(window), std_course_win(window,back)])
        studentdb_button.place(x=90, y=290)

    elif name == "Instructor":
        studentdb_button = tk.Button(window, text="Update", **nrom_btn,
                                     command=lambda: [clear_window(window), update(window, name)])
        studentdb_button.place(x=90, y=220)
        studentdb_button = tk.Button(window, text="Courses", **nrom_btn, command=lambda: [
            clear_window(window), ins_course_win(window,back)])
        studentdb_button.place(x=90, y=290)
        studentdb_button = tk.Button(
            window, text="Add degree", **nrom_btn, command=lambda: [clear_window(window), add_grade(window,back)])
        studentdb_button.place(x=90, y=360)

def insert(window,name):
        
        head=tk.Label(window,text="Insert "+name,**label_txt)
        head.place(x=30,y=15)
        if name == 'Courses':
            fname= tk.Label(window,text='Name',**form_txt)
            fname.place(x=50,y=80)

            fname= tk.Label(window,text='Description',**form_txt)
            fname.place(x=50,y=150)

            e_name = tk.Entry(window,width=20)
            e_name.place(x=200,y=90)

            e_cdesc = tk.Text(window,width=50,height=5)
            e_cdesc.place(x=200,y=160)
            
        else:        
            
            fname= tk.Label(window,text='First name',**form_txt)
            fname.place(x=50,y=70)

            lname = tk.Label(window,text='Last name',**form_txt)
            lname.place(x=50,y=130)
    
            gender = tk.Label(window,text='Gender',**form_txt)
            gender.place(x=50,y=190)
            date =tk.StringVar(window)
            birthdate = tk.Label(window,text='Birth Date',**form_txt)
            birthdate.place(x=50,y=250)
    
            e_fname = tk.Entry(window,width=30)
            e_fname.place(x=260,y=90)
    
            e_lname = tk.Entry(window,width=30)
            e_lname.place(x=260,y=140)
    
            gender = tk.IntVar()
            radiobutton_1 = tk.Radiobutton(window, text='Male', variable=gender, value=1,**radio_btn )
            radiobutton_1.place(x=260, y=200)
            radiobutton_2 = tk.Radiobutton(window, text='Female', variable=gender, value=2, **radio_btn)
            radiobutton_2.place(x=370, y=200)
    
            cal=DateEntry(window,selectmode='day',textvariable=date)
            cal.place(x=260, y=260)
        
        error_label = tk.Label(window, text="", bg='#EC7063')
        error_label.place(x=50,y=380)
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
        insertst_button1.place(x=25,y=320)
        insertback_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),proc_win(window,home,name)])
        insertback_button.place(x=550,y=15)



def update(window,name):
        flag = False
        head1=tk.Label(window,text="Update " + name,**label_txt)
        head1.place(x=30,y=15)

        id= tk.Label(window,text='Enter your ID',**form_txt)
        id.place(x=50,y=80)

        id_entry=tk.Entry(window,width=30)
        id_entry.place(x=270, y=90)

        updateback_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),proc_win(window,home,name)])
        updateback_button.place(x=550,y=15)

        q=tk.Label(window,text='choose Field',**form_txt)
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
            birthdate = tk.Label(window,text='Birth Date',**form_txt)
            birthdate.place(x=50,y=300)
            widgets_list.append(birthdate)
            date =tk.StringVar(window)
            cal=DateEntry(window,selectmode='day',textvariable=date)
            cal.place(x=200, y=310)
            widgets_list.append(cal)
        else:    
            e_field = tk.Entry(window,width=20)
            e_field.place(x=200,y=310)
            widgets_list.append(e_field)

            l_field= tk.Label(window,text=filed,**form_txt)
            l_field.place(x=50,y=300)
            widgets_list.append(l_field)

        update_btn=tk.Button(window,text="Update",**nrom_btn)
        update_btn.place(x=50,y=350)
        



def delete(window ,name):
        head=tk.Label(window,text='Delete ' + name,**label_txt)
        head.place(x=30,y=10)

        id= tk.Label(window,text=name+' ID',**form_txt)
        id.place(x=50,y=80)
        e_id = tk.Entry(window,width=20)
        e_id.place(x=220,y=90)
        deleteback_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),proc_win(window,home,name)])
        deleteback_button.place(x=550,y=15)
        error_label = tk.Label(window, text="", bg='#EC7063')
        error_label.place(x=50,y=210)
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

def std_course_win(window,back):
    Label1 = tk.Label(text='Student Courses', **label_txt)
    Label1.place(x=30, y=15)
    studentdb_button=tk.Button(window,text="insert",**nrom_btn,command=lambda:[clear_window(window),enroll_course(window,back)])
    studentdb_button.place(x=90,y=80)
    studentdb_button=tk.Button(window,text="delete",**nrom_btn,command=lambda:[clear_window(window),delete_course(window,back)])
    studentdb_button.place(x=90,y=150)

    back_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),proc_win(window,back,"Student")])
    back_button.place(x=550,y=15)
        

def enroll_course(window,back):
    Label1 = tk.Label(text='Enroll Courses', **label_txt)
    Label1.place(x=30, y=15)
    ST_ID=tk.Label(window,text='Student ID',**form_txt)
    ST_ID.place(x=50,y=80)
    st_entry=tk.Entry(window,width=30)
    st_entry.place(x=200, y=90)
    cor_ID=tk.Label(window,text='Course ID',**form_txt)
    cor_ID.place(x=50,y=150)
    cor_entry=tk.Entry(window,width=30)
    cor_entry.place(x=200, y=160)
    date=tk.Label(window,text='Date',**form_txt)
    date.place(x=50,y=220)
    date=tk.Entry(window,width=30)
    date.place(x=200, y=230)
    year=tk.Label(window,text='Year',**form_txt)
    year.place(x=50,y=290)
    year=tk.Entry(window,width=30)
    year.place(x=200, y=300)
    

    error_label = tk.Label(window, text="", bg='#EC7063')
    error_label.place(x=50,y=410)
   
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
    en_sub.place(x=50,y=350)
    back_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),std_course_win(window,back)])
    back_button.place(x=550,y=15)




def delete_course(window,back):
    Label1 = tk.Label(text='Delete Course', **label_txt)
    Label1.place(x=30, y=15)     
    ST_ID=tk.Label(window,text='Student ID',**form_txt)
    ST_ID.place(x=50,y=80)
    st_entry=tk.Entry(window,width=30)
    st_entry.place(x=200, y=90)

    cor_ID=tk.Label(window,text='Course ID',**form_txt)
    cor_ID.place(x=50,y=150)
    cor_entry=tk.Entry(window,width=30)
    cor_entry.place(x=200, y=160)
    error_label = tk.Label(window, text="", bg='#EC7063')
    error_label.place(x=50, y=280)
    back_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),std_course_win(window,back)])
    back_button.place(x=550,y=15)

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
    en_sub.place(x=50,y=220)

def ins_course_win(window,back):
    Label1 = tk.Label(text='Instructor Courses', **label_txt)
    Label1.place(x=30, y=15) 
    studentdb_button=tk.Button(window,text="insert",**nrom_btn,command=lambda:[clear_window(window),insert_t(window,back)])
    studentdb_button.place(x=90,y=80)
    studentdb_button=tk.Button(window,text="delete",**nrom_btn,command=lambda:[clear_window(window),delete_t(window,back)])
    studentdb_button.place(x=90,y=150)
    back_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),proc_win(window,back,"Instructor")])
    back_button.place(x=550,y=15)
    
def insert_t(window,back):
    Label1 = tk.Label(text='Insert Instructor Courses', **label_txt)
    Label1.place(x=30, y=15)
    ins_ID=tk.Label(window,text='instructor ID',**form_txt)
    ins_ID.place(x=50,y=80)
    ins_entry=tk.Entry(window,width=30)
    ins_entry.place(x=220, y=90)
    cor_ID=tk.Label(window,text='Course ID',**form_txt)
    cor_ID.place(x=50,y=150)
    cor_entry=tk.Entry(window,width=30)
    cor_entry.place(x=220, y=160)

    error_label = tk.Label(window, text="", bg='#EC7063')
    error_label.place(x=50,y=280)
   
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

    en_sub=tk.Button(window,text='Enroll',**nrom_btn,command=check)
    en_sub.place(x=50,y=220)
    back_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),ins_course_win(window,back)])
    back_button.place(x=550,y=15)


def delete_t(window,back):
    Label1 = tk.Label(text='Delete Instructor Courses', **label_txt)
    Label1.place(x=30, y=15)
    ins_ID=tk.Label(window,text='instructor ID',**form_txt)
    ins_ID.place(x=50,y=80)
    ins_entry=tk.Entry(window,width=30)
    ins_entry.place(x=220, y=90)
    cor_ID=tk.Label(window,text='Course ID',**form_txt)
    cor_ID.place(x=50,y=150)
    cor_entry=tk.Entry(window,width=30)
    cor_entry.place(x=220, y=160)
    error_label = tk.Label(window, text="", bg='#EC7063')
    error_label.place(x=50, y=280)
    back_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),ins_course_win(window,back)])
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
    en_sub.place(x=50,y=220)

def add_grade(window,back):
    Label1 = tk.Label(text='Instructor Degree', **label_txt)
    Label1.place(x=30, y=15)
    ins_ID=tk.Label(window,text='Instuctor ID',**form_txt)
    ins_ID.place(x=50,y=80)

    ins_entry=tk.Entry(window,width=30)
    ins_entry.place(x=220, y=90)

    degree=tk.Label(window,text='Degree',**form_txt)
    degree.place(x=50,y=150)

    degree_entry=tk.Entry(window,width=30)
    degree_entry.place(x=220, y=160)

    univeristy=tk.Label(window,text='University',**form_txt)
    univeristy.place(x=50,y=220)

    univeristy_entry=tk.Entry(window,width=30)
    univeristy_entry.place(x=220, y=230)

    year=tk.Label(window,text='year',**form_txt)
    year.place(x=50,y=290)
    
    year=tk.Entry(window,width=30)
    year.place(x=220, y=300)

    en_sub=tk.Button(window,text='Add',**nrom_btn)
    en_sub.place(x=50,y=360)

    back_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),proc_win(window,home,"Instructor")])
    back_button.place(x=550,y=15)
#################################################################################

    