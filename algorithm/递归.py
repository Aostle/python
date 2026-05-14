# 递归求阶乘
def fac(x):
    if x==1:
        return 1;
    else:
        return x*fac(x-1)
print("5的阶乘是:",fac(5))

# 倒计时
def countdown(i):
    print (i)
    if(i<=1):
        return
    else:
        countdown(i-1)
# print ("倒计时开始:")
# countdown(10)

# 定义一个数组变量

arr = [5,3,2,6,1,0]

# sum 函数
def sum(arr):               
    if len(arr) ==0:
        return 0
    else:
        x = arr[0]
        return x + sum(arr[1:])
print("数组求和:",sum(arr))

# 计算列表包含的元素数量

def count(arr):
    if len(arr) ==0:
        return 0
    else:
        return 1+ count(arr[1:])

print("数组size:",count(arr))

#找出列表中最大的数字

def max(arr):

    if len(arr)==0:
        raise ValueError("数组不能为空")
    
    if len(arr)==1:
        return arr[0]
    
    x = arr[0]
    return x if x>max(arr[1:]) else max(arr[1:])
    
print("数组最大值",max(arr))


    
