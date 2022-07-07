def reversal(lst,n):
    return lst[n:]+lst[:n]

def reversal2(lst:list,n):
    for i in range(n):
        lst.append(lst.pop(0))
    return lst

def swapHeadTail(lst:list):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

def swapPositions(lst,index1,index2):
    index1-=1
    index2-=1
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

arr = [1,2,3,4,5,6,7]
print(swapPositions(arr,1,3))

arr = [1,2,3,4,5,6,7]
print(arr[::-1])
# print([i for i in reversed(arr)])

# arr.sort(reverse=True)
# print(arr)

print(arr.count(1)>0)


def arraySum(lst,size):
    if(size==0):
        return 0
    else:
        return lst[size-1]+arraySum(lst,size-1)
print(arraySum(arr,len(arr)))


from functools import reduce

print(reduce(lambda x,y:x*y,arr))


list1 = [10, 20, 4, 45, 99]
 
list1.sort()
 
print("最小元素为:", *list1[:1])


