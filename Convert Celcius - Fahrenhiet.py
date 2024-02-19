import time
x=3
while x>0:
      print('\n')
      a=float(input("Enter Temperature in FARENHIET (F)="))
      b=float(input("Enter Temperature in CELCIUS (C)="))
      c=(a-32)*5/9
      f=(b*9/5)+32
      print ('FARENHIET to CELCIUS=',c)
      print ('CELCIUS to FARENHIET=',f)
time.sleep(10)
