import mysql.connector as con

mycon=con.connect(host="localhost",user="root",
                  passwd="dav",database="class12")

cursor=mycon.cursor()
if mycon.is_connected():
          print("Connection Established")
cursor.execute("select * from student")
data=cursor.fetchall()
for row in data:
          print(row)
