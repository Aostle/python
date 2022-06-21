
num1 = int(input("请输入班级1的数量:")) 
class1 = set()
for i in range(0,num1):
    name = input("请输入第%d位学生姓名:"%(i+1))
    class1.add(name)


num2 = int(input("请输入班级2的数量:")) 
class2 = set()
for i in range(0,num2):
    name = input("请输入第%d位学生姓名:"%(i+1))
    class2.add(name)

sum = class1 & class2

print("重名学生:")
for name in sum:
    print(name,end=" ")

diff = class2.difference(class1)
print("\n只存在于2班的名字:")
for name in diff:
    print(name,end=" ")
    