def dictionairy():  
 
    # 声明字典
    key_value ={}     
 
    # 初始化
    key_value[2] = 56       
    key_value[1] = 2 
    key_value[5] = 12 
    key_value[4] = 24
    key_value[6] = 18      
    key_value[3] = 323 

    print ("按key排序:") 
    for i in sorted (key_value) : 
        print ((i, key_value[i]), end =" ") 
    
    print('\n')
 
    print ("按值(value)排序:")   
    print(sorted(key_value.items(), key = lambda kv:(kv[1]))) 

dictionairy()


def Merge(dict1, dict2): 
    res = { **dict1,**dict2} 
    return res 
      
# 两个字典
dict1 = {'a': 10, 'b': 8} 
dict2 = {'b': 6, 'c': 4} 
dict3 = Merge(dict1, dict2) 
print(dict3)