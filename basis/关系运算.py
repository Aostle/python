#输入球队实力

'''
a = int(input("a球队的实力:"))
b = int(input("b球队的实力:"))
c = int(input("c球队的实力:"))
d = int(input("d球队的实力:"))

avsb = (a>b)*3+(a==b)
avsc = (a>c)*3+(a==c)
avsd = (a>d)*3+(a==d)


score= avsb+avsc+avsd

print("a球队总成绩为:%d" %score)

'''




#输入成绩
curriculum1 = int(input("请输入第一门成绩:"))
curriculum2 = int(input("请输入第二门成绩:"))
curriculum3 = int(input("请输入第三门成绩:"))

scores = [curriculum1,curriculum2,curriculum3]

total=0
for score in scores:
    if(score<60):
        total += 0
    elif(60<=score<90):
        total += 1
    else:
        total += 2

print("总成绩为:%d"%total)    


