# fp = open('demo.txt','w')
# print('文件名:',fp.name)
# print('是否关闭:',fp.closed)
# print('访问模式:',fp.mode)


# fp.write("www.twle.cn\nHello")
# fp.close()

# 打开文件


fp = open("demo.txt","r+")
str = fp.read(12)
print("读取到的字符串是:",str)

# 查找当前位置

position = fp.tell()
print("当前文件位置:",position)

# 把指针再次定位到文件开头

position = fp.seek(0,0)
str = fp.read(10)
print("重新读取字符串:",str)

# 关闭打开的文件

fp.close()


