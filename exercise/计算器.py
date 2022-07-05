class oper:
    oper = ''
    func = ''

    
    def __init__(self,oper):
        self.oper = oper.strip()

    def opers(self,num1,num2):
        switcher = {
            "+":"add",
            "-":"substract",
            "*":"multiply",
            "/":"divide"
        }
        func =  switcher.get(self.oper,"default")
        if func == 'default':
            print("error....")
            exit()
        num1 = float(num1)
        num2 = float(num2)
        func = getattr(self,func)
        return func(num1,num2)

    def add(self,num1,num2):
        return num1+num2

    def subtract(self,num1,num2):
        return num1-num2
    
    def multiply(self,num1,num2):
        return num1*num2

    def divide(self,num1,num2):
        return num1/num2

import re

nums=input("请输入：")
numsObj=re.search(r'(\d+)(.*?)(\d+)',nums,re.M)
if numsObj:
    num1=numsObj.group(1)
    fuhao=numsObj.group(2)
    num2=numsObj.group(3)
    operObj=oper(fuhao)
    res=operObj.opers(num1,num2)
    print('运算结果{}'.format(res))
else:
    print("输入错误，{}".format(nums))

    

    

    