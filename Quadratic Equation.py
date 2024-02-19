import math
lo=1
while lo>0:
      a=int(input ("Enter Coificient of X^2 [a]="))
      b=int(input("Enter Coificient of X [b]="))
      c=int(input("Enter Constant [c]="))
      d= (b**2)-(4*a*c)
      if d>=0:
            X1=(-b+math.sqrt(d))/2*a
            X2=(-b-math.sqrt(d))/2*a
            print ("1st Solution of Equation=", X1 )
            print ("2nd Solution of Equation=", X2)
      else:
            print("Roots are Imaginary")
      print("-"*70)

      
      
