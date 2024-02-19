def compute(num):
  if num==1:
    return 1
  else:
    return (num+compute(num-1))


#Calling Function
n=int(input("Enter A number"))
for i in range (1,n+1):
  print(i)
print('\n')
print("The Sum of the series from 1...",n,"is",compute(n))
