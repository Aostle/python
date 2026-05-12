
def hcf(x,y):
    smaller = min(x,y)
    for i in range(1,smaller+1):
        if(x%i==0) and (y%i==0):
            hcf =i
    return hcf

def gcd(a,b):
    if a<b:
        a,b = b,a
    if a%b==0:
        return b
    for i in range(b//2+1,0,-1):
        if b%i==0 and a%i==0:
            return i

def gcd2(a,b):
    if a<b:
        a,b = b,a
    if a%b==0:
        return b
    return gcd2(b,a%b)

def gcd3(a,b):
    while b!=0:
        a,b=b,a%b
    return a


def lcm(a,b):
    greater = max(a,b)
    while(True):
        if greater%a==0 and greater%b==0:
            break
        greater+=1
    return greater

def lcm2(a,b):
    if a<b:
        a,b = b,a
    if a%b==0:
        return a
    mul =2
    while a*mul%b!=0:
        mul +=1
    return a*mul

def lcm3(a,b):
    return a*b//gcd3(a,b)

num1 = int(input("请输入正整数:"))
num2 = int(input("请输入正整数:"))
# print("{0},{1}的最大公约数为:{2}".format(num1,num2,gcd3(num1,num2)))
print("{0},{1}的最小公倍数为:{2}".format(num1,num2,lcm3(num1,num2)))