import time
a=int(input("ENTER A:-"))
b=int(input("ENTER B:-"))
c=int(input("ENTER C:-"))
if b<a>c:
      print ("Greatest Integer Is",a)
if a<b>c:
      print ("Greatest Integer Is",b)
if a<c>b:
      print ("Greatest Integer Is",c)
if b>a<c:
      print ("Smallest Integer Is",a)
if a>b<c:
      print ("Smallest Integer Is",b)
if b>c<a:
      print ("Smallest Integer Is",c)
time.sleep(12)
