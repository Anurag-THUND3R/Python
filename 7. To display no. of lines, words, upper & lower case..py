fopen=open("student.txt")
Upper=Lower=Words=nLines=0
st=fopen.readlines()

for lines in st:
  nLines=len(st)
  words=lines.split()
  for word in words:
    Words+=1
    for letters in word:
      if letters.isupper():
        Upper+=1
      elif letters.islower():
        Lower+=1
print("No. of lines in Student.txt file is : ",nLines)
print("No. of words in Student.txt file is : " ,Words)
print("No. of Upper case Chara. in Student.txt file is : " ,Upper)
print("No. of Lower case Chara. in Student.txt file is : ", Lower)
fopen.close()
