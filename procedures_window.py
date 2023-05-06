from support import clear_window
from setting import *
import tkinter as tk
from tkcalendar import DateEntry
from procedures import *
from empsearch import search_win


def emp_win(window, back):
    Label1 = tk.Label(text='Select database ', **label_txt)
    Label1.place(x=70, y=15+100)
    studentdb_button = tk.Button(window, text="Student", **nrom_btn, command=lambda: [
                                 clear_window(window), proc_win(window, back, "Student")])
    studentdb_button.place(x=70, y=70+140)
    studentdb_button = tk.Button(window, text="Insturctor", **nrom_btn, command=lambda: [
                                 clear_window(window), proc_win(window, back, "Instructor")])
    studentdb_button.place(x=70, y=130+140)
    studentdb_button = tk.Button(window, text="Courses", **nrom_btn, command=lambda: [
                                 clear_window(window), proc_win(window, back, "Courses")])
    studentdb_button.place(x=70, y=190+140)
    studentdb_button = tk.Button(window, text="Search", **nrom_btn,
                                 command=lambda: [clear_window(window), search_win(window)])
    studentdb_button.place(x=580, y=130+140)
    back_button = tk.Button(window, text="Back", **back_btn,
                            command=lambda: [clear_window(window), back(window)])
    back_button.place(x=320,y=500)


def proc_win(window, back, name):

    studentdb_button = tk.Button(window, text="Insert", **nrom_btn,
                                 command=lambda: [clear_window(window), insert(window, name)])
    studentdb_button.place(x=320, y=70)
    studentdb_button = tk.Button(window, text="Delete", **nrom_btn,
                                 command=lambda: [clear_window(window), delete(window, name)])
    studentdb_button.place(x=320, y=190)
    back_button = tk.Button(window, text="home", **back_btn,
                            command=lambda: [clear_window(window), back(window, name)])
    back_button.place(x=320,y=500)
    if name == "Student":
        studentdb_button = tk.Button(window, text="Update", **nrom_btn,
                                     command=lambda: [clear_window(window), update(window, name)])
        studentdb_button.place(x=320, y=130)
        studentdb_button = tk.Button(window, text="Courses", **nrom_btn,
                                     command=lambda: [clear_window(window), std_course_win(window)])
        studentdb_button.place(x=320, y=250)

    elif name == "Instructor":
        studentdb_button = tk.Button(window, text="Update", **nrom_btn,
                                     command=lambda: [clear_window(window), update(window, name)])
        studentdb_button.place(x=320, y=130)
        studentdb_button = tk.Button(window, text="Courses", **nrom_btn, command=lambda: [
            clear_window(window), ins_course_win(window)])
        studentdb_button.place(x=320, y=250)
        studentdb_button = tk.Button(
            window, text="Add degree", **nrom_btn, command=lambda: [clear_window(window), add_grade(window)])
        studentdb_button.place(x=320, y=310)

def insert(window,name):
        
        head=tk.Label(window,text="Insert "+name,**label_txt)
        head.place(x=330,y=100)
        if name == 'Courses':
            fname= tk.Label(window,text='Name',**label_txt)
            fname.place(x=50,y=70)

            fname= tk.Label(window,text='Description',**label_txt)
            fname.place(x=50,y=150)

            e_name = tk.Entry(window,width=20)
            e_name.place(x=320,y=70)

            e_cdesc = tk.Text(window,width=50,height=5)
            e_cdesc.place(x=320,y=150)
            
        else:        
            
            fname= tk.Label(window,text='First name',**label_txt)
            fname.place(x=50+220,y=70+100)

            lname = tk.Label(window,text='Last name',**label_txt)
            lname.place(x=50+220,y=110+100)
    
            gender = tk.Label(window,text='Gender',**label_txt)
            gender.place(x=50+220,y=150+100)
            date =tk.StringVar(window)
            birthdate = tk.Label(window,text='Birth Date',**label_txt)
            birthdate.place(x=50+220,y=190+100)
    
            e_fname = tk.Entry(window,width=20)
            e_fname.place(x=200+220,y=75+100)
    
            e_lname = tk.Entry(window,width=20)
            e_lname.place(x=200+220,y=115+100)
    
            gender = tk.IntVar()
            radiobutton_1 = tk.Radiobutton(window, text='Male', variable=gender, value=1,**radio_btn )
            radiobutton_1.place(x=200+220, y=160+90)
            radiobutton_2 = tk.Radiobutton(window, text='Female', variable=gender, value=2, **radio_btn)
            radiobutton_2.place(x=280+220, y=160+90)
    
            cal=DateEntry(window,selectmode='day',textvariable=date)
            cal.place(x=200+220, y=195+100)
    
        insertst_button1=tk.Button(window,text="Insert",**nrom_btn)
        insertst_button1.place(x=320,y=500)

def update(window,name):
        flag = False
        head1=tk.Label(window,text="Update" + name,**label_txt)
        head1.place(x=330,y=100)

        id= tk.Label(window,text='Enter your ID',**label_txt)
        id.place(x=50+180,y=70+100)

        id_entry=tk.Entry(window,width=30)
        id_entry.place(x=200+180, y=75+100)

        q=tk.Label(window,text='choose Field',**label_txt)
        q.place(x=50+180,y=330-40)

        choices = tk.IntVar()
        fname_rd = tk.Radiobutton(window, text='First Name', variable=choices, value=1, **radio_btn,command=lambda:[update_field(window,'First Name')])
        fname_rd.place(x=200+180, y=190+100-40)
        lname_rd = tk.Radiobutton(window, text='Last Name', variable=choices, value=2, **radio_btn,command=lambda:[update_field(window,'Last Name')])
        lname_rd.place(x=200+180, y=230+100-40)
        age_rd = tk.Radiobutton(window, text='Age', variable=choices, value=3, **radio_btn ,command=lambda:[update_field(window,"Age")])
        age_rd.place(x=200+180, y=270+100-40)
widgets_list =[]
def update_field(window,filed):
        
        for widgets in widgets_list:
            widgets.destroy()

        if filed == 'Age':
            birthdate = tk.Label(window,text='Birth Date',**label_txt)
            birthdate.place(x=50+180,y=400)
            widgets_list.append(birthdate)
            date =tk.StringVar(window)
            cal=DateEntry(window,selectmode='day',textvariable=date)
            cal.place(x=380, y=400)
            widgets_list.append(cal)
        else:    
            e_field = tk.Entry(window,width=20)
            e_field.place(x=380,y=400)
            widgets_list.append(e_field)

            l_field= tk.Label(window,text=filed,**label_txt)
            l_field.place(x=50+180,y=400)
            widgets_list.append(l_field)
        update_btn=tk.Button(window,text="Update",**nrom_btn)
        update_btn.place(x=320,y=500)




def delete(window ,name):
        head=tk.Label(window,text='Delete' + name,**label_txt)
        head.place(x=330,y=100)

        id= tk.Label(window,text=name+' ID',**label_txt)
        id.place(x=50+180,y=70+190)
        e_id = tk.Entry(window,width=20)
        e_id.place(x=200+180, y=70+190)
        error_label = tk.Label(window, text="", bg='#EC7063')
        error_label.place(x=200+180, y=100+190)
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
        del_btn.place(x=320,y=500)

def std_course_win(window):
    studentdb_button=tk.Button(window,text="insert",**nrom_btn,command=lambda:[clear_window(window),enroll_course(window)])
    studentdb_button.place(x=320,y=10+200)
    studentdb_button=tk.Button(window,text="delete",**nrom_btn,command=lambda:[clear_window(window),delete_course(window)])
    studentdb_button.place(x=320,y=70+200)
        
def enroll_course(window):
   ST_ID=tk.Label(window,text='Student ID',**label_txt)
   ST_ID.place(x=10+220,y=90+80)
   st_entry=tk.Entry(window,width=30)
   st_entry.place(x=170+220, y=99+80)
   cor_ID=tk.Label(window,text='Course ID',**label_txt)
   cor_ID.place(x=10+220,y=130+80)
   cor_entry=tk.Entry(window,width=30)
   cor_entry.place(x=170+220, y=139+80)
   date=tk.Label(window,text='Date',**label_txt)
   date.place(x=10+220,y=170+80)
   date=tk.Entry(window,width=30)
   date.place(x=170+220, y=179+80)
   year=tk.Label(window,text='Year',**label_txt)
   year.place(x=10+220,y=210+80)
   year=tk.Entry(window,width=30)
   year.place(x=170+220, y=219+80)
   en_sub=tk.Button(window,text='Enroll',**nrom_btn)
   en_sub.place(x=170+160,y=500)




def delete_course(window):     
    ST_ID=tk.Label(window,text='Student ID',**nrom_btn)
    ST_ID.place(x=10+220,y=90+80)
    st_entry=tk.Entry(window,width=30)
    st_entry.place(x=170+220, y=99+75)

    cor_ID=tk.Label(window,text='Course ID',**label_txt)
    cor_ID.place(x=10+220,y=130+80)
    cor_entry=tk.Entry(window,width=30)
    cor_entry.place(x=170+220, y=139+75)
    error_label = tk.Label(window, text="", bg='#EC7063')
    error_label.place(x=170+220, y=139+100)

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
    en_sub.place(x=320,y=500)

def ins_course_win(window):
    studentdb_button=tk.Button(window,text="insert",**nrom_btn,command=lambda:[clear_window(window),insert_t(window)])
    studentdb_button.place(x=320,y=10+200)
    studentdb_button=tk.Button(window,text="delete",**nrom_btn,command=lambda:[clear_window(window),delete_t(window)])
    studentdb_button.place(x=320,y=70+200)
    
def insert_t(window):
   ins_ID=tk.Label(window,text='instructor ID',**label_txt)
   ins_ID.place(x=10+220,y=130+80)
   ins_entry=tk.Entry(window,width=30)
   ins_entry.place(x=170+220, y=139+80)
   cor_ID=tk.Label(window,text='Course ID',**label_txt)
   cor_ID.place(x=10+220,y=170+80)
   cor_entry=tk.Entry(window,width=30)
   cor_entry.place(x=170+220, y=179+80)
   en_sub=tk.Button(window,text='Enroll',**label_txt)
   en_sub.place(x=320,y=500)


def delete_t(window):
   ins_ID=tk.Label(window,text='instructor ID',**label_txt)
   ins_ID.place(x=10+220,y=90+80)
   ins_entry=tk.Entry(window,width=30)
   ins_entry.place(x=170+220, y=99+75)
   cor_ID=tk.Label(window,text='Course ID',**label_txt)
   cor_ID.place(x=10+220,y=130+80)
   cor_entry=tk.Entry(window,width=30)
   cor_entry.place(x=170+220, y=139+75)
   error_label = tk.Label(window, text="", bg='#EC7063')
   error_label.place(x=170+220, y=139+100)

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
   en_sub.place(x=320,y=500)

def add_grade(window):
    ins_ID=tk.Label(window,text='ID',**label_txt)
    ins_ID.place(x=10+220,y=90+80)

    ins_entry=tk.Entry(window,width=30)
    ins_entry.place(x=170+220, y=99+80)

    degree=tk.Label(window,text='Degree',**label_txt)
    degree.place(x=10+220,y=130+80)

    degree_entry=tk.Entry(window,width=30)
    degree_entry.place(x=170+220, y=139+80)

    univeristy=tk.Label(window,text='University',**label_txt)
    univeristy.place(x=10+220,y=170+80)

    univeristy_entry=tk.Entry(window,width=30)
    univeristy_entry.place(x=170+220, y=179+80)

    year=tk.Label(window,text='year',**label_txt)
    year.place(x=10+220,y=210+80)
    
    year=tk.Entry(window,width=30)
    year.place(x=170+220, y=219+80)
#################################################################################

    