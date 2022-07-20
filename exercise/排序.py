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
    for j in range(i,n):
      if arr[j]<arr[i]:
        arr[i],arr[j] = arr[j],arr[i]

arr = [12, 11, 13, 5, 6] 

selectionSort(arr)

for i in range(len(arr)):
    print(arr[i])



            
        
        