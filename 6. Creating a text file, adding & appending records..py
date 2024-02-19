createapp=int(input("To create a student.txt file and add data, Enter 1""\n"
                    "or To append data in student.txt file, Enter 2" "\n"))
if createapp==1:
  filecre= open("Student.txt","w")
  n=int(input("How many records you want to enter? "))
  for i in range(0,n):
    Name=input("Enter Name:")
    Class=input("Enter Class:")
    rec=Name+str(Class)
    filecre.write(rec)
  print("The records have been written in Student.txt file") 
  filecre.close()
elif createapp==2:
  fileapp= open("Student.txt","a")
  x=int(input("How many records you want to Append? "))
  for i in range(0,x):
    NameA=input("Enter Name:")
    ClassA=input("Enter Class:")
    Rec=NameA+str(ClassA)
    fileapp.write(Rec)
  print("The records have been appended in Student.txt file") 
  fileapp.close()
  
else:
  print("You have entered incorrect choice")
