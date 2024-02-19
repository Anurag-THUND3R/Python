fopen=open("student.txt")
c=0
st=fopen.readlines()
for lines in st:
  words=lines.split()
  for word in words:
    if word=="the":
      c+=1
print("No. of times 'the' appear in the stident.txt file are : ",c)
