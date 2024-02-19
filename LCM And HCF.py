un=3
while un>0:
      a= int(input("Enter First Number"))
      b= int(input("Enter Second Number"))
      p=(a*b)
      l=[]
      for i in range (1,p+1):
            x=a*i
            for j in range (1,p+1):
                  y=b*j
                  if x==y:
                        l.append(x)
      lcm=min(l)
      hcf=(p/(lcm))
      print("LCM Of",a,",",b,"=",lcm)
      print("HCF Of",a,",",b,"=",hcf)
