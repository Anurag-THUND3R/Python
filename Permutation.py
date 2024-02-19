x=3
while x>1:
      print("\n")
      a=int(input("Enter Value Of 'n' :- "))
      b=int(input("Enter Value Of 'r' :- "))
      c=(a-b)
      f=1
      fa=1
      fac=1
      for i in range (1,a+1):
            f=f*i
      for j in range (1,c+1):
            fa=fa*j
      for k in range (1,b+1):
            fac=fac*k
      p=int(f/fa)
      combi=int(p/fac)
      print ("Permutation =",int(p))
      print ("Combination =",int(combi))
            
