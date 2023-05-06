import tkinter as tk
from setting import *
from support import clear_window
import home
import procedures_window 

def search_win(window):
      Label1 = tk.Label(text='Select DataBase for search', **label_txt)
      Label1.place(x=30, y=15)

      show_course_btn=tk.Button(window,text='Students',**nrom_btn,command=lambda:[clear_window(window),search(window,"Students")])
      show_course_btn.place(x=90,y=80)

      enroll_btn=tk.Button(window,text='Instructors',**nrom_btn,command=lambda:[clear_window(window),search(window,"Instructors")])
      enroll_btn.place(x=90,y=150)

      back_button=tk.Button(window,text="Courses",**nrom_btn,command=lambda:[clear_window(window),search(window,"Courses")])
      back_button.place(x=90,y=220)

      back_button=tk.Button(window,text="Select all",**nrom_btn,command=lambda:[clear_window(window),search(window,"Courses")])
      back_button.place(x=90,y=290)

      setback_button=tk.Button(window,text="Back",**back_btn,command=lambda:[clear_window(window),procedures_window.emp_win(window,home)])
      setback_button.place(x=550,y=15)

widgets_list =[]
def search(window,name):
      if name == "Courses":
            field_search = tk.IntVar(window)
            Label2 = tk.Label(text='Choose field you want to search about:', **label_txt)
            Label2.place(x=30, y=15)
            id = tk.Radiobutton(window, text=name + ' ID', variable=field_search, value=1,command=lambda:[field(window,"ID",name)], **radio_btn)
            id.place(x=60, y=120)
            name = tk.Radiobutton(window, text=name + ' Name', variable=field_search, value=2,command=lambda:[field(window,"Name",name)], **radio_btn)
            name.place(x=320, y=120)
            
            insertback_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),search_win(window)])
            insertback_button.place(x=550,y=400)
      else:
            Label3 = tk.Label(text='Choose field you want to search about:', **label_txt)
            Label3.place(x=50, y=25)
            field_search = tk.IntVar(window)
            id = tk.Radiobutton(window, text=name + ' ID', variable=field_search, value=1,command=lambda:[field(window,"ID",name)], **radio_btn)
            id.place(x=350, y=130)
            fname = tk.Radiobutton(window, text=name + ' First Name', variable=field_search, value=2,command=lambda:[field(window,"First Name",name)], **radio_btn)
            fname.place(x=350, y=190)
            lname = tk.Radiobutton(window, text=name + ' Last Name', variable=field_search, value=3,command=lambda:[field(window,"Last Name",name)], **radio_btn)
            lname.place(x=350, y=250)
            course_name = tk.Radiobutton(window, text=name + ' Course Name', variable=field_search, value=4,command=lambda:[field(window,"Course Name",name)], **radio_btn)
            course_name.place(x=350, y=310) 

            insertback_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),search_win(window)])
            insertback_button.place(x=550,y=400)
      def field(window,field_name,name):
                  for widgets in widgets_list:
                        widgets.destroy()
                        
                  field_srch= tk.Label(window,text=field_name,**label_txt)
                  field_srch.place(x=10,y=360)
                  widgets_list.append(field_srch)

                  e_field_srch = tk.Entry(window,width=20)
                  e_field_srch.place(x=230,y=375)
                  widgets_list.append(e_field_srch)

                  search_button=tk.Button(window,text="Search",**nrom_btn)
                  search_button.place(x=360,y=400)


      