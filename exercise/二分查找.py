
def binarySearch(lst:list,num):

    start = 0
    end = len(lst)-1

    while start<=end:

        mid = (start+end)//2

        if num<lst[mid]:
            end = mid-1

        if num>lst[mid]:
            start = mid+1

        if num == lst[mid]:
            return mid

    return -1

def recursionSearch(lst:list,l,r,num):
    if(l<=r):
        mid = (l+r)//2
        if lst[mid] == num:
            return mid
        if num< lst[mid]:
            return recursionSearch(lst,l,mid-1,num)
        if num> lst[mid]:
            return recursionSearch(lst,mid+1,r,num)
    else:
        return -1

def linearSearch(arr,x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            return i
    return -1


# 测试数组(必须是顺序数组)
arr = [i for i in range(1,10100)]
x = 888

result = linearSearch(arr,x)

if result!=-1:
    print(f'元素{x}在数组中下标为:',result)
else:
    print('元素在数组中不存在!')