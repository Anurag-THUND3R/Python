import time
p=int(input("ENTER, PRINCIPAL :- "))
r=int(input("ENTER, RATE OF INTREST :- "))
t=int(input("ENTER, TIME :- "))
si=p*r*t/100
a=si+p
print("\n")
print ("SIMPLE INTREST :- ",si)
print ("AMOUNT :- ",a)
time.sleep(10)
