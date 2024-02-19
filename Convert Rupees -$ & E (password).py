import time
pas=input("Enter Password")
for pa in range (1,6):
      if "dollar and rupees"==pas:
            x=3
            while x>0:
                  print('\n')
                  a=int(input("Enter Rupees (Rs.)="))
                  d=a/68.67
                  p=a/90.68
                  print("Dollar ($)=", d)
                  print("Pound (E)=", p)
for pa in range (1,6):
      if "dollar and rupees"!=pas:
            print ("Wrong Password")
time.sleep(12)
