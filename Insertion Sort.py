def insertionsort(arr):
      for i in range(1,len(arr)):
            key=arr[i]
            j=i-1
            while j>=0 and key<arr[j]:
                  arr[j+1]=arr[j]
                  j-=1
            arr[j+1]=key

arr=eval(input("Enter an array : "))
insertionsort(arr)
sort=[]
print("Sorted Array is : ")
for i in range(len(arr)):
      sort.append(arr[i])
print(sort)
