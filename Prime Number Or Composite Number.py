x=3
while x>0:
      print("\6")
      a=int(input("Enter Any Number :- "))
      c=0
      for i in range (1,a+1):
            if a%i==0:
                  c=c+1
      if c==2:
            print (a,"Is A Prime Number")
      else:
            print (a,"Is A Composite Number")
