import mysql.connector as con

mycon=con.connect(host="localhost",user="root",
                  passwd="dav",database="class12")

cursor=mycon.cursor()
if mycon.is_connected():
          print("Connection Established")
x=int(input("Enter number of records you want to enter"))
for i in range (1,x+1):
          name=input("Enter Student's name: ")
          adno=input("Enter Admission Number: ")
          cls=int(input("Enter Class: "))
          sec=input("Enter Section: ")
          dob=input("Enter Date Of Birth: ")
          query="insert into student(Name,Adm_no,Class,Section,DOB) values ('{}','{}','{}','{}','{}')".format(name,adno,cls,sec,dob)
          cursor.execute(query)
          print("Record Succesfully Entered")
mycon.commit()
