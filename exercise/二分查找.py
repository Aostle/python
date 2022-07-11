
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

def recursionSearch(lst:list,num):
    
    pass


# 测试数组(必须是顺序数组)
arr = [2, 3, 10, 14, 40]
x = 40

result = binarySearch(arr,x)

if result!=-1:
    print(f'元素{x}在数组中下标为:',result)
else:
    print('元素在数组中不存在!')