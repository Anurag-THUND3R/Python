def bubbleSort(arr):
      n=len(arr)
      for i in range(n):
            for j in range(0,n-i-1):
                  if arr[j]>arr[j+1]:
                        arr[j],arr[j+1]=arr[j+1],arr[j]

arr=eval(input("Enter an array : "))
bubbleSort(arr)
sort=[]
print("Sorted Array is : ")
for i in range(len(arr)):
      sort.append(arr[i])
print(sort)
