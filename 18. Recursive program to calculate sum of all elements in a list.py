def sumOfList(alist,size):
          if (size==0):
                    return 0
          else:
                    return alist[size-1]+sumOfList(alist,size-1)

#Calling Program#
inlist=eval(input("Enter a list"))
total=sumOfList(inlist,len(inlist))
print("Sum of all elements in Given list : ",total)
