import mysql.connector as con

mycon=con.connect(host="localhost",user="root",
                  passwd="dav",database="class12")

cursor=mycon.cursor()
if mycon.is_connected():
          print("Connection Established")

query="create table student (Name varchar(30), Adm_no varchar(10), Class int(3),Section char(1), DOB varchar(20))"
cursor.execute(query)
          
