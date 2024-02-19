def binarysearch(alist, item):
    first=0
    last=len(alist)-1
    while first<=last:
        midpoint=int((first+last)/2)
        if item==alist[midpoint]:
          return midpoint
        elif item<alist[midpoint]:
          last=midpoint-1
        else:
          first=midpoint+1
    else:
      return-1


list1=eval(input("Enter a List"))
item0=int(input("Enter a item to search"))
res=binarysearch(list1, item0)
if res >= 0:
  print(item0,"Found at index",res)
else:
  print("Sorry! Item dose not exist")
