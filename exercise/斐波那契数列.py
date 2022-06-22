# 循环输出
def fib(n):
    count = 0
    a,b = 0,1
    while(count<n):
        print(a,end=" ")
        a,b= b ,a+b
        count+=1
    print()

fib(10)

# 递归输出(大规模的计算占用资源较多, 导致运算慢甚至卡死)

def fib2(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    if(n>2):
        return fib2(n-2)+fib2(n-1)

for i in range(1,11):
    print(fib2(i),end=" ")

print()

# 利用通项公式计算
N = 10
for i in range(0,N):
        print(int((5**0.5/5)*(((1+5**0.5)/2)**i - ((1-5**0.5)/2)**i)),end=" ")









