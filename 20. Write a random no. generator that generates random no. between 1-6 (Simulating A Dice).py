import random
y=5
print("Enter 1 to roll a dice")
print("Enter 0 to exit")
while y>0:
          x=int(input("Enter Your choice : "))
          if x==1:
                    print("Number on dice is",random.randrange(1,7))
                    print("\t")
          else:
                    break
          

