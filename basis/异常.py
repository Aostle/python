import sys
def mye( level ):
    if level < 1:
        raise ValueError("Invalid level!", level) 
        # 触发异常后，后面的代码就不会再执行
        print('Hello World!')

try:
    mye(0)       # 触发异常
except ValueError as e:
    # print(sys.exc_info()[1])
    print(e)
else:
    print("一切正常")

# class Networkerror(RuntimeError):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)

# try:
#     raise Networkerror("Bad hostname")
# except Networkerror as e:
#     print ( e )