import datetime,sys,math

print(datetime.datetime.now(),'Hello World!')
print(sys.path)
print(dir(math))

str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义



my_list = ['简单编程', 'www.twle.cn']
my_list2 = ['简单编程2', 'www.twle.cn2']
print("网站名：{0[0]}, 地址 {1[1]}".format(my_list,my_list2))  # "0" 是可选的



