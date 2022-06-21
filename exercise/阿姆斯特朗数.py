# 一个n位正整数等于其各位数字的n次方之和 : 153 = 1^3 + 5^3 +3^3

from cmath import e
from msilib.schema import Error


def isMathed(num):
    #判断是否为阿姆斯特朗数
    n = len(str(num))
    sum  = 0
    temp = num
    while temp > 0:
        digit = temp%10
        sum+=digit**n
        temp //=10
    if(num==sum):
        # print("it's mathed!")
        return True
    else:
        # print("miss mathed!")
        return False

#循环输入数字判断:
# while True:
#     try:
#         num = int(input("请输入一个正整数:"))
#         isMathed(num)
#     except ValueError as e:
#         print("发生异常:{0}".format(e.args))
#         break
#     else:
#         print("继续输入",end="\n")

#输出1到1000范围内的阿姆斯特朗数
for i in range(1,1000):
    if isMathed(i):
        print(i,end=" ")






    




