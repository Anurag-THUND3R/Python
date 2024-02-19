fopen=open("student.txt")
c=0
st=fopen.readlines()
for lines in st:
  if lines[0]=="A":
    c+=1
print("No. of lines starting with 'A' in student.txt file are : ",c)
fopen.close()
