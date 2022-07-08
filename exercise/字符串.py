test_str = "Runoob"
new_str = test_str.replace(test_str[3], "", 1)
print(new_str)


def ff(str,num):
    return str[:num] + str[num+1:];
print(ff(test_str,1))


def check(string, sub_str): 
    if sub_str in string:
        print("存在")
    if (string.find(sub_str) == -1): 
        print("不存在！") 
    else: 
        print("存在！") 
        
string = "www.runoob.com"
sub_str ="runoob"
check(string, sub_str)


import re
def findurl(str):
    url =  re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',str)
    return url

str = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print('urls: ', findurl(str))