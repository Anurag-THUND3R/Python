import time
import math
a=int(input("ENTER FIRST SIDE:-"))
b=int(input("ENTER SECOND SIDE:-"))
c=int(input("ENTER THIRD SIDE:-"))
s=(a+b+c)/2
ar=s*(s-a)*(s-b)*(s-c)
if ar>=0:
      x=math.sqrt(ar)
      print("AREA=",x)
else:
      print("Triangle With This Dimension Is Not Possible") 
time.sleep(12)
