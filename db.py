import pymysql
conn = pymysql.connect(
        host='database-1.cfo6vewprtg5.eu-north-1.rds.amazonaws.com',
        user='admin', 
        password = "0123456789",
        db= "student_enroll"
        )

cur = conn.cursor()





def drop_all_tables():
        cur = conn.cursor()

         # Disable foreign key checks
        cur.execute("SET FOREIGN_KEY_CHECKS=0")

        # Get list of all tables in the database
        cur.execute("SHOW TABLES")
        tables = cur.fetchall()

        # Loop through all tables and drop them
        for table in tables:
            cur.execute(f"DROP TABLE {table[0]}")

        # Re-enable foreign key checks
        cur.execute("SET FOREIGN_KEY_CHECKS=1")

def insert_some_values():

        sql = "INSERT INTO Student (fname, lname, dob, gender) VALUES (%s, %s, %s, %s)"
        val = [
            ('John', 'Doe', '1990-01-01', 'M'),
            ('Jane', 'Doe', '1992-05-05', 'F'),
            ('Bob', 'Smith', '1995-10-10', 'M'),
            ('Alice', 'Johnson', '1998-03-15', 'F')
        ]
        cur.executemany(sql, val)

        # Insert data into the Instructor table
        sql = "INSERT INTO Instructor (fname, lname, gender, dob) VALUES (%s, %s, %s, %s)"
        val = [
            ('Peter', 'Smith', 'M', '1985-01-01'),
            ('Mary', 'Johnson', 'F', '1987-05-05'),
            ('David', 'Lee', 'M', '1990-10-10')
        ]
        cur.executemany(sql, val)

        # Insert data into the Courses table
        sql = "INSERT INTO Courses (name, description) VALUES (%s, %s)"
        val = [
            ('Mathematics', 'Introduction to mathematics'),
            ('Physics', 'Classical mechanics and modern physics'),
            ('Computer Science', 'Programming and algorithms')
        ]
        cur.executemany(sql, val)

        # Insert data into the Enroll table
        sql = "INSERT INTO Enroll (S_id, C_id, year, univ_yr) VALUES (%s, %s, %s, %s)"
        val = [
            (1, 1, 2021, 1),
            (1, 2, 2021, 1),
            (2, 2, 2021, 1),
            (3, 1, 2021, 1),
            (3, 3, 2021, 1),
            (4, 3, 2021, 1)
        ]
        cur.executemany(sql, val)

        # Insert data into the Teach table
        sql = "INSERT INTO Teach (I_id, C_id) VALUES (%s, %s)"
        val = [
            (1, 1),
            (2, 2),
            (3, 3),
            (1, 3)
        ]
        cur.executemany(sql, val)

def create_db():
        sql='''
        CREATE TABLE IF NOT EXISTS Student (
                id int NOT NULL AUTO_INCREMENT,
                fname varchar(255) COLLATE ascii_bin NOT NULL CHECK (fname REGEXP '^[A-Za-z]+$'),
                lname varchar(255) COLLATE ascii_bin NOT NULL CHECK (lname REGEXP '^[A-Za-z]+$'),
                dob date,
                gender char(1),
                PRIMARY KEY (id)
         )
         '''
        cur.execute(sql)

        sql='''
        CREATE TABLE IF NOT EXISTS Instructor (
                id int NOT NULL AUTO_INCREMENT,
                fname varchar(255) COLLATE ascii_bin NOT NULL CHECK (fname REGEXP '^[A-Za-z]+$'),
                lname varchar(255) COLLATE ascii_bin NOT NULL CHECK (lname REGEXP '^[A-Za-z]+$'),
                gender char(1),
                dob date,
                PRIMARY KEY (id)
            )
          '''
        cur.execute(sql)


        sql='''
        CREATE TABLE IF NOT EXISTS Courses (
                id int NOT NULL AUTO_INCREMENT,
                name varchar(255) NOT NULL,
                description LONGTEXT,
                PRIMARY KEY (id)
            )
          '''
        cur.execute(sql)

        sql='''
         CREATE TABLE IF NOT EXISTS Enroll (
                S_id int ,
                C_id int ,
                year int,
                univ_yr int,
                PRIMARY KEY (S_id,C_id),
                FOREIGN KEY (S_id) REFERENCES Student(id),
                FOREIGN KEY (C_id) REFERENCES Courses(id)
              )
           '''
        cur.execute(sql)

        sql='''
        CREATE TABLE IF NOT EXISTS  Teach (
                I_id int ,
                C_id int ,
                PRIMARY KEY (I_id,C_id),
                FOREIGN KEY (I_id) REFERENCES Instructor(id),
                FOREIGN KEY (C_id) REFERENCES Courses(id)
              )
           '''
        cur.execute(sql)

        sql='''
        CREATE TABLE IF NOT EXISTS Degree(
                I_id int ,
                degree varchar(255),
                univ   varchar(255),
                year   int,
                FOREIGN KEY (I_id) REFERENCES Instructor(id)
              )
           '''
        cur.execute(sql)

        table_name = 'Student'
        values = [('John', 'Doe', 'M', '1990-05-01'), ('Jane', 'Doe', 'F', '1995-02-15')]
        sql = f"INSERT INTO {table_name} (fname, lname, gender, dob) VALUES (%s, %s, %s, %s)"
        
        # Execute the SQL statement
        cur.executemany(sql, values)

def show_all_tables():
        cur.execute("SHOW TABLES")    
        tables = cur.fetchall()
        for table in tables:    
                cur.execute("SHOW COLUMNS FROM {}".format(table[0]))    
                # Fetch all the columns from the cursor
                columns = cur.fetchall()     
                # Loop through the columns and print their names
                print(table[0])
                print()
                for column in columns:
                    print(column[0] + "  " + column[1])
                print()
                print('--------------------------')
                print()
       

# show_all_tables()
# create_db()
# drop_all_tables()
# insert_some_values()

cur.close() 
conn.commit()
conn.close()
