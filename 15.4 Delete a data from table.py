import mysql.connector as con

mycon=con.connect(host="localhost",user="root",
                  passwd="dav",database="class12")

cursor=mycon.cursor()
if mycon.is_connected():
          print("Connection Established")
x=int(input("Enter how many recorde you want to delete ?"))
for i in range(1,x+1):
          name=input("Enter name of student to delete: ")
          query="DELETE from student where name=Bhavesh Jain"
cursor.execute(query)
