
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image , ImageTk
from PIL import Image, ImageFilter
from tkinter import messagebox as messagebox



def cor_page():
    print("hi")


def st_fun():
    import p1

def home_fun():
    import p2

def emp_fun():
    import emp

def st_fun2(x):
    import p3
    if x == 1 :
      p3.yesFun()
    elif x==0:
      p3.noFun()    

def emp_in(x):
   import empins
   if x==1:
     empins.student_db_control() 
   elif x==2:
      empins.instructor_db_control()
   elif x==3:
       empins.course_db_control()

def emp_de(x):
   import empde
   if x==1:
      empde.student_db_control() 
   elif x==2:
      empde.instructor_db_control()
   elif x==3:
      empde.course_db_control()

def emp_up(x):
   import empup
   if x==1:
      empup.student_db_control() 
   elif x==2:
      empup.instructor_db_control()
   elif x==3:
      empup.course_db_control()
   

def fn_fun():
      
      f= Tk()
      f.title("update Student'first name")
      f.geometry("400x200")
      f.configure(background="#EC7063")
      f.resizable(False,False)
      fl=tk.Label(f,text='First Name',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
      fl.place(x=40,y=10)
      fn_entry=tk.Entry(f,width=40)
      fn_entry.place(x=120,y=50)
      b1f= tk.Button(f, text='Update',width=16,font=30, fg='#EC7063',bg='#FDEBD0')
      b1f.place(x=120,y=100)
      f.mainloop()



def ln_fun():
   l= Tk()
   l.title("Update Student'last name")
   l.geometry("400x200")
   l.configure(background="#EC7063")
   ll=tk.Label(l,text='Last Name',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
   ll.place(x=40,y=10)
   l.resizable(False,False)
   ln_entry=tk.Entry(l,width=30)
   ln_entry.place(x=120,y=50)
   b1l= tk.Button(l, text='Update',width=16,font=30, fg='#EC7063',bg='#FDEBD0')
   b1l.place(x=120,y=100)



def age_fun():
   a= Tk()
   a.title("Update Student'age")
   a.geometry("400x200")
   a.configure(background="#EC7063")
   al=tk.Label(a,text='age',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
   al.place(x=40,y=10)
   a.resizable(False,False)
   a_entry=tk.Entry(a,width=30)
   a_entry.place(x=120,y=50)
   b1a= tk.Button(a, text='Update',width=16,font=30, fg='#EC7063',bg='#FDEBD0')
   b1a.place(x=120,y=100)
   



def gen_fun():
   g= Tk()
   g.title("Update Student'gender")
   g.geometry("400x200")
   g.configure(background="#EC7063")
   gl=tk.Label(g,text='Gender',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
   gl.place(x=40,y=10)
   g.resizable(False,False)
   g_entry=tk.Entry(g,width=30)
   g_entry.place(x=120,y=50)
   b1g= tk.Button(g, text='Update',width=16,font=30, fg='#EC7063',bg='#FDEBD0')
   b1g.place(x=120,y=100)
   

   ##########3@@@@@@@@@@@@@@@@@@@@@@@@@@22

def fni_fun():
   f= Tk()
   f.title("update instractor'first name")
   f.geometry("400x200")
   f.configure(background="#EC7063")
   f.resizable(False,False)
   fl=tk.Label(f,text='First Name',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
   fl.place(x=40,y=10)
   fn_entry=tk.Entry(f,width=40)
   fn_entry.place(x=120,y=50)
   b1f= tk.Button(f, text='Update',width=16,font=30, fg='#EC7063',bg='#FDEBD0')
   b1f.place(x=120,y=100)
   f.mainloop()



def lni_fun():
   l= Tk()
   l.title("Update instractor'last name")
   l.geometry("400x200")
   l.configure(background="#EC7063")
   ll=tk.Label(l,text='Last Name',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
   ll.place(x=40,y=10)
   l.resizable(False,False)
   ln_entry=tk.Entry(l,width=30)
   ln_entry.place(x=120,y=50)
   b1l= tk.Button(l, text='Update',width=16,font=30, fg='#EC7063',bg='#FDEBD0')
   b1l.place(x=120,y=100)



def agei_fun():
   a= Tk()
   a.title("Update instractor'age")
   a.geometry("400x200")
   a.configure(background="#EC7063")
   al=tk.Label(a,text='age',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
   al.place(x=40,y=10)
   a.resizable(False,False)
   a_entry=tk.Entry(a,width=30)
   a_entry.place(x=120,y=50)
   b1a= tk.Button(a, text='Update',width=16,font=30, fg='#EC7063',bg='#FDEBD0')
   b1a.place(x=120,y=100)
   



def geni_fun():
   g= Tk()
   g.title("Update instractor'gender")
   g.geometry("400x200")
   g.configure(background="#EC7063")
   gl=tk.Label(g,text='Gender',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
   gl.place(x=40,y=10)
   g.resizable(False,False)
   g_entry=tk.Entry(g,width=30)
   g_entry.place(x=120,y=50)
   b1g= tk.Button(g, text='Update',width=16,font=30, fg='#EC7063',bg='#FDEBD0')
   b1g.place(x=120,y=100)
   

   ##############################3

def cn_fun():

   f= Tk()
   f.title("update Course Name")
   f.geometry("400x200")
   f.configure(background="#EC7063")
   f.resizable(False,False)
   fl=tk.Label(f,text='Course Name',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
   fl.place(x=40,y=10)
   fn_entry=tk.Entry(f,width=40)
   fn_entry.place(x=120,y=50)
   b1f= tk.Button(f, text='Update',width=16,font=30, fg='#EC7063',bg='#FDEBD0')
   b1f.place(x=120,y=100)
   f.mainloop()



def cid_fun():
   l= Tk()
   l.title("Update Course ID")
   l.geometry("400x200")
   l.configure(background="#EC7063")
   ll=tk.Label(l,text='Course ID',font=('monospace',20,'bold'),fg='white',bg='#EC7063')
   ll.place(x=40,y=10)
   l.resizable(False,False)
   ln_entry=tk.Entry(l,width=30)
   ln_entry.place(x=120,y=50)
   b1l= tk.Button(l, text='Update',width=16,font=30, fg='#EC7063',bg='#FDEBD0')
   b1l.place(x=120,y=100)
#############################################################################################
def emp_search(x):
   import empsearch
   if x==2:
     empsearch.student_db_control() 
   elif x==3:
      empsearch.instructor_db_control()
   elif x==4:
      empsearch.course_db_control()
