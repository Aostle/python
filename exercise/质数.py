import math
# 用户输入数字
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))


def isprime(num):
    # 质数大于 1
    if num > 1:
        # 找到其平方根（ √ ），减少算法时间
        square_num = math.floor( num ** 0.5 )
        # 查找其因子
        for i in range(2, (square_num+1)): #将平凡根加1是为了能取到平方根那个值
            if (num % i) == 0:
                # print(num, "是合数")
                # print(i, "乘于", num // i, "是", num)
                return False
        else:
            # print(num, "是质数")
            return True
            # 如果输入的数字小于或等于 1，不是质数
    else:
        # print(num, "既不是质数，也不是合数")
        return False


for i in range(lower,upper):
    if isprime(i):
       print(i,end=" ")