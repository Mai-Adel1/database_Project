import tkinter as tk
from setting import *
from support import clear_window
import home
import procedures_window 

def search_win(window):
      show_course_btn=tk.Button(window,text='Students',**nrom_btn,command=lambda:[clear_window(window),search(window,"Students")])
      show_course_btn.place(x=100,y=110)

      enroll_btn=tk.Button(window,text='Instructors',**nrom_btn,command=lambda:[clear_window(window),search(window,"Instructors")])
      enroll_btn.place(x=100,y=170)

      back_button=tk.Button(window,text="Courses",**nrom_btn,command=lambda:[clear_window(window),search(window,"Courses")])
      back_button.place(x=100,y=230)

      back_button=tk.Button(window,text="Select all",**nrom_btn,command=lambda:[clear_window(window),search(window,"Courses")])
      back_button.place(x=100,y=290)

      setback_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),procedures_window.emp_win(window,home)])
      setback_button.place(x=400,y=20)

widgets_list =[]
def search(window,name):
      if name == "Courses":
            field_search = tk.IntVar(window)
            id = tk.Radiobutton(window, text=name + ' ID', variable=field_search, value=1,command=lambda:[field(window,"ID",name)], **radio_btn)
            id.place(x=10, y=10)
            name = tk.Radiobutton(window, text=name + ' Name', variable=field_search, value=2,command=lambda:[field(window,"Name",name)], **radio_btn)
            name.place(x=10, y=40)
            
            insertback_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),search_win(window)])
            insertback_button.place(x=400,y=20)
      else:
            field_search = tk.IntVar(window)
            id = tk.Radiobutton(window, text=name + ' ID', variable=field_search, value=1,command=lambda:[field(window,"ID",name)], **radio_btn)
            id.place(x=10, y=10)
            fname = tk.Radiobutton(window, text=name + ' First Name', variable=field_search, value=2,command=lambda:[field(window,"First Name",name)], **radio_btn)
            fname.place(x=10, y=40)
            lname = tk.Radiobutton(window, text=name + ' Last Name', variable=field_search, value=3,command=lambda:[field(window,"Last Name",name)], **radio_btn)
            lname.place(x=10, y=70)
            course_name = tk.Radiobutton(window, text=name + ' Course Name', variable=field_search, value=4,command=lambda:[field(window,"Course Name",name)], **radio_btn)
            course_name.place(x=10, y=100) 

            insertback_button=tk.Button(window,text="Back",**nrom_btn,command=lambda:[clear_window(window),search_win(window)])
            insertback_button.place(x=400,y=20)
      def field(window,field_name,name):
                  for widgets in widgets_list:
                        widgets.destroy()
                        
                  field_srch= tk.Label(window,text=field_name,**label_txt)
                  field_srch.place(x=10,y=130)
                  widgets_list.append(field_srch)

                  e_field_srch = tk.Entry(window,width=20)
                  e_field_srch.place(x=160,y=140)
                  widgets_list.append(e_field_srch)

                  search_button=tk.Button(window,text="search",**nrom_btn)
                  search_button.place(x=10,y=170)


      