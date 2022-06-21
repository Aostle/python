 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-

print('==============string测试===================')
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

x ='a'
y ='b'
print(x,end=",")
print(y,end="\n")



from sys import argv,path  #  导入特定的成员
 
#print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


#print(print.__doc__)
print('==============number测试===================')

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d),sep=" ")
print(isinstance(a,int)) 

print('===============list测试==================')

def reverseWords(input):
    '''倒叙输出'''
     
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
 
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1]
 
    # 重新组合字符串
    output = ' '.join(inputWords)
     
    return output
 
if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(reverseWords.__doc__)
    print(rw)


print('===============set测试==================')

# set
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素    



print('================dictionary测试=================')

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

print('================运算符=================')
a = 60;
print(a<<2)

a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
if( a and b):
    print("表达式都为true")

if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")

a = 20
b = 30
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")



print("*"*20)

a = 10
def test():    
    b = a + 1     
    print(b)
test()


for i in range(1,10):
    print(i,end=",")
print("\n")
for i in range(10,1,-1):
    print(i,end=",")





