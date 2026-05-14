def quickSort(arr):

    if(len(arr)<2):
        return arr
    # 基准值
    pivot = arr[0]

    small_subArr = [i for i in arr[1:] if i<=pivot] 
    big_subArr = [i for i in arr[1:] if i>pivot]

    return quickSort(small_subArr)+[pivot]+quickSort(big_subArr)

print("排序后的数组:",quickSort([5,3,6,2,10])) 
    