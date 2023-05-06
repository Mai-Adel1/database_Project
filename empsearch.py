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
                  error_label = tk.Label(window, text="", bg='#EC7063')
                  error_label.place(x=50,y=210)
                  def check():
                      if (field_name == "ID"):
                             try:
                                 if not e_field_srch.get().isdigit:
                                      raise ValueError
                                  
                                 id = int(e_field_srch.get())
                                 rows=search_check(name, field_name,int(e_field_srch.get()))
                                 if rows is None:
                                     raise Exception("there is no data")
                                 if len(rows)==0:
                                     raise Exception("there is no data")
                                      
                                 else:
                                      text = tk.Text(window)
                                      for row in rows:
                                        text.insert(tk.END, str(row) + "\n")
                                      text.place(x=10,y=210)
                             except  ValueError:
                                 
                                 error_label.config(text="please enter int value")
                                 
                             except Exception as E:
                                 
                                 error_label.config(text=E)
                                 
                      else:
                              try:
                                 cc = e_field_srch.get()
                                 if not (cc.isalpha()):
                                    raise ValueError
                                 e_fln = str(e_field_srch.get())
                                 rows = search_check(
                                     name, field_name, str(e_field_srch.get()))
                                 if rows is None:
                                     raise Exception("there is no data")
                                 if len(rows)==0:
                                     
                                     raise Exception("there is no data")
                                 else:
                                     text = tk.Text(window)
                                     for row in rows:
                                          text.insert(tk.END, str(row) + "\n")
                                     text.place(x=10, y=210)
                                    
                              except  ValueError:
                                error_label.config(text="please enter string")
                                
                              except Exception as E:
                                 error_label.config(text=E)
                             
                  
                  search_button=tk.Button(window,text="search",**nrom_btn,command=check)
                  search_button.place(x=10,y=170)
      
