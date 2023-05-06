def clear_window(window):
   for widgets in window.winfo_children():
      widgets.destroy()

col_val = {
   "Student":['fname','lname','gender','dob'],
   "Instructor":['fname','lname','gender','dob'],
   "Courses":['name','description'],
   "Enroll":"S_id",
   "Teach":'I_id'
}

join_col = {
   "Student":["Enroll","Enroll.S_id"],
   "Instructor":["Teach","Teach.I_id"]
}
