a=input("Enter Any String :- ")
string2=a.upper()
l=len(a)
b=0
for i in range (l):
      if a[i].islower():
            print(i+1,"is in lower case")
      b=b+1
print("\n")
print("Short Form Is")
print(string2[0],end=' ')
for i in range (l):
      if a[i]==" ":
            print(string2[i+1],end=' ')
print("\n",end=' ')
print("Number Of Total Characters:- ",b)
