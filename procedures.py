import pymysql
conn = pymysql.connect(
    host='database-1.cfo6vewprtg5.eu-north-1.rds.amazonaws.com',
    user='admin',
    password="0123456789",
    db="student_enroll")
cur = conn.cursor()

def delt_error_hand_enroll(name, co_id, stAndIns_id):
   if name == "Enroll":
       SAndI_id = "S_id"
   elif name == "Teach":
       SAndI_id = "I_id"

   sql = '''DELETE FROM {} WHERE {}= %s and {}= %s''' .format(
       name, SAndI_id, "C_id")
   cur.execute(sql, (stAndIns_id, co_id))
   conn.commit()
   conn.close()


def delt_error_hand(table_name, id):
   if (table_name == "Student"):
      coulm = "Studentid"
   elif table_name == "Instructor":
      coulm = "I_id"
   else:
      coulm = "C_id"
   sql = '''DELETE FROM {} WHERE {}= %s''' .format(table_name, coulm)
   cur.execute(sql, (id))
   conn.commit()
   conn.close()

def insert_error_hand_courses(table_name,course_name,course_desc):
   column1 = "C_Name"
   column2 = "C_desc"

   sql = '''INSERT INTO {} ({}, {}) VALUES (%s, %s)''' .format(table_name, column1,column2)
   cur.execute(sql, (course_name,course_desc))
   conn.commit()
   conn.close()

def insert_error_hand_si(table_name,f_name,l_name,birth,gender):
   if gender == 1:
      gender='Male'
   else:
      gender='Female'
   
   if (table_name == "Student"):
      column1 = "FirstName"
      column2 = "LastName"
      column3 = "Age"
   else:
      column1 = "fname"
      column2 = "lname"
      column3 = "DOB"

   column4 = "gender"
   
   sql = '''INSERT INTO {} ({}, {}, {}, {}) VALUES (%s, %s, %s, %s)''' .format(table_name, column1,column2,column3,column4)
   cur.execute(sql, (f_name,l_name,birth,gender))
   conn.commit()
   id = cur.lastrowid
   print(id)
   conn.close()

def insert_error_hand_enroll(table_name,st_id,course_id,date,year):

   sql = '''INSERT INTO {} ({}, {}, {}, {}) VALUES (%s, %s, %s, %s)''' .format(table_name, 'S_id','C_id','DOE','school_yr')
   cur.execute(sql, (st_id,course_id,date,year))
   conn.commit()
   conn.close()

def insert_error_hand_enroll_teach(table_name,inst_id,cour_id):

   sql = '''INSERT INTO {} ({}, {}) VALUES (%s, %s) ''' .format(table_name, 'I_id','C_id')
   cur.execute(sql, (inst_id,cour_id))
   conn.commit()
   conn.close()

def insert_error_hand_degree(table_name,inst_id,deg,univer,year):

   sql = '''INSERT INTO {} ({}, {}, {}, {}) VALUES (%s, %s,%s, %s) ''' .format(table_name, 'I_id','degree','univ','year')
   cur.execute(sql, (inst_id,deg,univer,year))
   conn.commit()
   conn.close()
def search_check(table_name,feild_name,e_feild_entry):
   if(feild_name=="ID"):
      if(table_name=="Student"):
        sql = '''
                 select * FROM {} 
                 left JOIN Enroll ON {}.Studentid = Enroll.S_id 
                 left JOIN Courses ON  Enroll.C_id = Courses.C_id 
                 WHERE {}.Studentid = %s''' .format(table_name,table_name,table_name)
        cur.execute(sql % e_feild_entry)
        rows=cur.fetchall()
        return rows
      elif (table_name == "Instructor"):
          sql = '''
                 select * FROM {}
                 left JOIN Teach ON {}.I_id = Teach.I_id
                 left JOIN Courses ON  Teach.C_id = Courses.C_id
                 WHERE {}.I_id = %s''' .format(table_name, table_name, table_name)
          cur.execute(sql % e_feild_entry)
          rows = cur.fetchall()
          return rows
      elif table_name=="Courses":
               sql = '''
                 select * FROM Courses
                 JOIN Enroll ON Courses.C_id = Enroll.C_id
                 JOIN Student ON  Enroll.S_id= Studentid
                 JOIN Teach ON Courses.C_id = Teach.C_id
                 JOIN Instructor ON Teach.I_id= Instructor.I_id
                 where Courses.C_id = %s
                '''
               cur.execute(sql % e_feild_entry)
               rows = cur.fetchall() 
               return rows
       
   else:
      if (table_name == "Student"):
       if (feild_name == "First Name"):
        sql = '''
                select * FROM {}
                left JOIN Enroll ON {}.Studentid = Enroll.S_id
                left JOIN Courses ON  Enroll.C_id = Courses.C_id
                WHERE {}.FirstName = "{}" ''' .format(table_name, table_name, table_name, e_feild_entry)
        cur.execute(sql)
        rows=cur.fetchall()
        return rows
       else:
          sql = '''
               select * FROM {}
               left JOIN Enroll ON {}.Studentid = Enroll.S_id
               left JOIN Courses ON  Enroll.C_id = Courses.C_id
               WHERE {}.LastName= "{}" ''' .format(table_name, table_name, table_name, e_feild_entry)
          cur.execute(sql)
          rows = cur.fetchall()
          return rows
      elif (table_name == "Instructor"):
           if (feild_name == "First Name"):
            sql = '''
        select * FROM {}
        left JOIN Teach ON {}.I_id = Teach.I_id
        left JOIN Courses ON  Teach.C_id = Courses.C_id
        WHERE {}.fname = "{}" ''' .format(table_name, table_name, table_name, e_feild_entry)
            cur.execute(sql)
            rows = cur.fetchall()
            return rows
           else:
             sql = '''
        select * FROM {}
        left JOIN Teach ON {}.I_id = Teach.I_id
        left JOIN Courses ON  Teach.C_id = Courses.C_id
        WHERE {}.lname= "{}" ''' .format(table_name,table_name,table_name,e_feild_entry)
             cur.execute(sql)
             rows = cur.fetchall()
             return rows   
      
      else:
         sql = '''
                 select * FROM Courses
                 JOIN Enroll ON Courses.C_id = Enroll.C_id
                 JOIN Student ON  Enroll.S_id= Studentid
                 JOIN Teach ON Courses.C_id = Teach.C_id
                 JOIN Instructor ON Teach.I_id= Instructor.I_id
                 where Courses.C_Name = "{}"
                '''.format(e_feild_entry)
         cur.execute(sql)
         rows = cur.fetchall()   
        
