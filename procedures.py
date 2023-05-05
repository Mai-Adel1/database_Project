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
