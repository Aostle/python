# 苹果,桃子,香蕉,梨子  (5,6,3,4),输入要购买的水果种类和数量,计算购买总价

# price = {"苹果":5,"香蕉":3,"桃子":6,"梨子":4}

price = dict()
price["苹果"]=5
price["桃子"]=6
price["香蕉"]=3
price["梨子"]=4

print("今日水果价格:")
for fruit in price:
    print("%s %d元/斤"%(fruit,price[fruit]))

#输入购买水果的种类数:
'''
sum_price =0
n = int(input("请输入购买水果的种类数:"))
for i in range(0,n):
    fruit = input("请输入购买的水果%d名称:"%(i+1))
    num  = int(input("请输入购买的水果%d的数量:"%(i+1)))
    if fruit in price:
        sum_price+=price[fruit]*num;

print("总购买价格为:%d"%sum_price)

'''




#计算谁的总成绩最高 

score = {"小明":[85,96,88],"小红":[72,80,91],"小亮":[83,69,75]}

best_name =""
best_score =0
for name in score:
    list = score[name]
    total = 0
    for i in list:
        total+=i
    print("%s总成绩为:%d"%(name,total))
    if(total>best_score):
        best_name = name
        best_score = total


print("成绩最好的是:%s"%best_name)







