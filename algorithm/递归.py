def fac(x):
    if x==1:
        return 1;
    else:
        return x*fac(x-1)
print("5的阶乘是:",fac(5))


def countdown(i):
    print (i)
    if(i<=1):
        return
    else:
        countdown(i-1)
print ("倒计时开始:")
countdown(10)
