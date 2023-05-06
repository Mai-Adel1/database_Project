from support import clear_window
from setting import *
import tkinter as tk
from tkcalendar import DateEntry
from procedures import *
from empsearch import search_win
import home


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
    back_button = tk.Button(window, text="Back", **back_btn ,command=lambda:[clear_window(window),home.home(window)])
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
        studentdb_button = tk.Button(window, text="Courses", **nrom_btn, command=lambda: [clear_window(window), ins_course_win(window,back)])
        studentdb_button.place(x=90, y=290)
        studentdb_button = tk.Button(
            window, text="Add degree", **nrom_btn, command=lambda: [clear_window(window), add_grade(window,back)])
        studentdb_button.place(x=90, y=360)

def insert(window,name):
        values = []
        head=tk.Label(window,text="Insert "+name,**label_txt)
        head.place(x=30,y=15)
        if name == 'Courses':
            l_name= tk.Label(window,text='Name',**form_txt)
            l_name.place(x=50,y=80)

            desc= tk.Label(window,text='Description',**form_txt)
            desc.place(x=50,y=150)

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
    
            gender = tk.StringVar()
            male = tk.Radiobutton(window, text='Male', variable=gender, value="M",**radio_btn )
            male.place(x=260, y=200)
            female = tk.Radiobutton(window, text='Female', variable=gender, value="F", **radio_btn)
            female.place(x=370, y=200)
    

            cal=DateEntry(window,selectmode='day',textvariable=date,date_pattern='yyyy/mm/dd')
            cal.place(x=200, y=200)

            
            insertst_button1=tk.Button(window,text="Insert",**nrom_btn,command=lambda:[db_insert(name,tuple([e_fname.get(),e_lname.get(),gender.get(),cal.get()]))])
            insertst_button1.place(x=25,y=240)
        
        insertback_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),proc_win(window,home,name)])
        insertback_button.place(x=550,y=15)




def update(window,name):
    
        head1=tk.Label(window,text="Update" + name,**label_txt)
        head1.place(x=30,y=10)

        id= tk.Label(window,text='Enter your ID',**form_txt)
        id.place(x=50,y=80)

        id_entry=tk.Entry(window,width=30)
        id_entry.place(x=270, y=90)

        updateback_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),proc_win(window,home,name)])
        updateback_button.place(x=550,y=15)

        q=tk.Label(window,text='choose Field',**form_txt)
        q.place(x=50,y=150)

        choices = tk.IntVar()
        fname_rd = tk.Radiobutton(window, text='First Name', variable=choices, value=1, **radio_btn,command=lambda:[update_field(window,'fname',name,id_entry)])
        fname_rd.place(x=200, y=190)
        lname_rd = tk.Radiobutton(window, text='Last Name', variable=choices, value=2, **radio_btn,command=lambda:[update_field(window,'lname',name,id_entry)])
        lname_rd.place(x=200, y=230)
        age_rd = tk.Radiobutton(window, text='Age', variable=choices, value=3, **radio_btn ,command=lambda:[update_field(window,"dob",name,id_entry)])
        age_rd.place(x=200, y=270)
widgets_list =[]
def update_field(window,filed,name,id):
        value = []
        for widgets in widgets_list:
            widgets.destroy()

        if filed == 'dob':
            birthdate = tk.Label(window,text='Birth Date',**label_txt)
            birthdate.place(x=50,y=400)
            widgets_list.append(birthdate)
            date =tk.StringVar(window)
            cal=DateEntry(window,selectmode='day',textvariable=date,date_pattern='yyyy/mm/dd')
            cal.place(x=200, y=400)
            widgets_list.append(cal)
            value.append(cal)
        else:    
            e_field = tk.Entry(window,width=20)
            e_field.place(x=200,y=400)
            value.append(e_field)
            widgets_list.append(e_field)

            l_field= tk.Label(window,text=filed,**form_txt)
            l_field.place(x=50,y=300)
            widgets_list.append(l_field)
        update_btn=tk.Button(window,text="Update",**nrom_btn,command=lambda:[db_update(name,filed,id.get(),value[-1].get())])
        update_btn.place(x=25,y=150)
        


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
          db_delete(name, int(e_id.get()))
         except ValueError:
           error_label.config(text="please enter int value")

         except Exception as E:
           error_label.config(text=E)
         else:
           error_label.config(text="deletion is done succesfully")

        del_btn=tk.Button(window,text="Delete",**nrom_btn,command=check)
        del_btn.place(x=25,y=150)

def std_course_win(window,back):
    studentdb_button=tk.Button(window,text="Enroll",**nrom_btn,command=lambda:[clear_window(window),enroll_course(window,"Enroll")])
    studentdb_button.place(x=30,y=10)
    studentdb_button=tk.Button(window,text="Drop",**nrom_btn,command=lambda:[clear_window(window),drop_course(window,"Enroll",back)])
    studentdb_button.place(x=30,y=70)

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
    cor_entry.place(x=170, y=139)
    year=tk.Label(window,text='year',**label_txt)
    year.place(x=10,y=170)
    year=tk.Entry(window,width=30)
    year.place(x=170, y=179)
    univ_year=tk.Label(window,text='University year',**label_txt)
    univ_year.place(x=10,y=210)
    univ_year=tk.Entry(window,width=30)
    univ_year.place(x=170, y=219)
    en_sub=tk.Button(window,text='Enroll',**nrom_btn,command=lambda:([db_enroll_course(st_entry.get(),cor_entry.get(),year.get(),univ_year.get())]))
    en_sub.place(x=170,y=260)
    back_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),emp_win(window,home)])
    back_button.place(x=500,y=20)





def drop_course(window,table,back):     
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
            course_id = int(cor_entry.get())
            id= int(st_entry.get())
            db_drop_course('Enroll', course_id,id)
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
    studentdb_button=tk.Button(window,text="Add Course",**nrom_btn,command=lambda:[clear_window(window),insert_t(window,back)])
    studentdb_button.place(x=90,y=80)
    studentdb_button=tk.Button(window,text="Drop Course",**nrom_btn,command=lambda:[clear_window(window),delete_t(window,back)])
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
    cor_entry.place(x=190, y=139)
    en_sub=tk.Button(window,text='Add course',**label_txt,command=lambda:[ db_teach_course(ins_entry.get(),cor_entry.get())])
    en_sub.place(x=170,y=260)
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
            db_drop_course('Teach', co_id, ins_id)
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

    en_sub=tk.Button(window,text='Add Degree',**nrom_btn,command =lambda:[db_degree(ins_entry.get(),degree_entry.get(),univeristy_entry.get(),year.get())])
    en_sub.place(x=170,y=260)

   

    back_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),proc_win(window,home,"Instructor")])
    back_button.place(x=550,y=15)



    