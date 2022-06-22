num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()


a = 10
def test():
    a= 33
    a = a + 1
    print(a)
test()
print(a)