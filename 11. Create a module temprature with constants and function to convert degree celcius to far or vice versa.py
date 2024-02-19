#Importing Temprature module and using it
import Temprature
print("1. To convert Degree Celcius to Fahrenheit " "\n"
      "2. To convert Fahrenheit to Degree Celcius")
c=int(input("Enter Your Choice : "))      
print("\t")
if c==1 :
          C=float(input("Enter Temprature in Degree Celcius: "))
          Temprature.c_f(C)
elif c==2 :
          F=float(input("Enter Temprature in Fahrenheit : "))
          Temprature.f_c(F)
else :
          print("Enter a valid number")
