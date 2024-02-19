import time
import math
a=int(input("ENTER A:-"))
b=int(input("ENTER B:-"))
c=int(input("ENTER C:-"))
if a==math.sqrt(b**2+c**2):
      print ("YES")
elif b==math.sqrt(a**2+c**2):
      print ("YES")
elif c==math.sqrt(b**2+a**2):
      print ("YES")
else:
      print("NO")
time.sleep(12)
      
