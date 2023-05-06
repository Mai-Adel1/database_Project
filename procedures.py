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

def db_update(table,column,id,value):
   print("tablle name   {}".format(table))
   print("field         {}".format(column))
   print("id            {}".format(id))
   print("value         {}".format(value))

sql ='''
UPDATE {}
SET {} = {}
WHERE condition
'''

cursor = conn.cursor()

# Show all tables in the database
cursor.execute("SHOW TABLES")

# Fetch all the tables from the cursor
tables = cursor.fetchall()

# Loop through the tables and print their names
for table in tables:

   cursor.execute("SHOW COLUMNS FROM {}".format(table[0]))

   # Fetch all the columns from the cursor
   columns = cursor.fetchall()

   # Loop through the columns and print their names
   print(table[0])
   print()
   for column in columns:
       print(column[0] + "  " + column[1])
   print()
   print('--------------------------')
   print()
# Close the cursor and the database connection
cursor.close()
conn.close()