import os

# os.rename("demo.txt","demo2.txt")

# os.remove("demo2.txt")


# os.mkdir("newDir")

# os.chdir("newDir")


# print (os.getcwd())


# os.rmdir("newDir")


try:
    fp = open("demo.txt","w")
    fp.write("这是一个测试文件")
except IOError:
    print("文件不存在或读取失败")
else:
    print("文件写入成功")
    fp.close()

# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
with open("demo.txt") as f:
    for line in f:
        print(line, end="")




