a = 20
b = 20

if ( a is b ):
   print ( "1 - a 和 b 引用同一个对象" ) 
else:
   print ( "1 - a 和 b 引用不同的对象" )

if ( id(a) == id(b) ):
   print ( "2 - a 和 b 指向相同的内存地址" )
else:
   print ( "2 - a 和 b 指向不同的内存地址" )

if ( a is not b ):
   print ( "3 - a 和 b 引用不同的对象" )
else:
   print ( "3 - a 和 b 引用同一个对象" )

# 修改变量 b 的值
b = 30
if ( a is b ):
   print ( "4 - a 和 b 引用同一个对象" )
else:
   print ( "4 - a 和 b 引用不同的对象" )

if ( a is not b ):
   print ( "5 - a 和 b 引用不同的对象" )
else:
   print ( "5 - a 和 b 引用同一个对象" )


'''
    python 中的== 用来比较内容是否相等

'''