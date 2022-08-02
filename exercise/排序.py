def insertionSort(arr):
    for i in range(1,len(arr)):
      key = arr[i]
      j = i-1
      while j>=0 and key<arr[j]:
        arr[j+1] = arr[j]
        j-=1
      arr[j+1] = key

def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(0,len(arr)-1-i):
      if(arr[j]>arr[j+1]):
        arr[j],arr[j+1] = arr[j+1],arr[j]
  
def selectionSort(arr):
  n = len(arr)
  for i in range(n):
    minIndex = i
    for j in range(i,n):
      if arr[j]<arr[minIndex]:
        minIndex = j
    arr[i],arr[minIndex] = arr[minIndex],arr[i]


def quickSort(arr,left,right):
  if left >right:
    return
  i ,j= left,right
  base = arr[left]
  while i<j:
    #因为基准数取得最左边, 所以右边的探测指针需要先行
    while i<j and arr[j]>=base:
      j-=1

    while i<j and arr[i]<=base:
      i+=1
    
    if(i<j):
      arr[i],arr[j] = arr[j],arr[i]
  
  arr[left],arr[i] = arr[i],arr[left]
  quickSort(arr,left,j-1)
  quickSort(arr,j+1,right)


arr = [11,24,5,32,50,34,54,76] 

quickSort(arr,0,len(arr)-1)
#bubbleSort(arr)

for i in range(len(arr)):
    print(arr[i])



            
        
        