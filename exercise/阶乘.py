def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    return 1

# print(factorial(100))

# 递归到1000 会栈内存溢出 


import math
print(math.factorial(100))



# 输出九九乘法表
print("*"*20,"九九乘法表","*"*20)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={:<2d}'.format(j,i,j*i),end=" ")
#     print()


# 推导式简写
print( '\n'.join(' '.join('{}*{}={:<2d}'.format(y,x,y*x) for y in range(1,x+1))  for x in range(1,10))) 