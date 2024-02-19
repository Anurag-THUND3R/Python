
#Importing circle module and using it
import Circle
print("1. To find the Area of ciricle" "\n"
      "2. To find the Circumference of ciricle ")
c=int(input("Enter Your Choice : "))      
print("\t")
if c==1 :
      r=float(input("Enter radius of Circle : "))
      Circle.Area(r)
elif c==2 :
      r=float(input("Enter radius of Circle : "))
      Circle.Circumference(r)
else :
      print("Enter a valid number")
