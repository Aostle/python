
import sys

def fobonacci(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b = b, a+b
        counter+=1

f = fobonacci(10)
print(f)
print(type(f))

# for x in f:
#     print(x,end=" ")

# while True:
#     e = next(f,None)
#     if e!=None:
#         print (e, end=" ")
#     else:
#         break

# while True:
#     try:
#         print(next(f),end=" ")
#     except StopIteration:
#         sys.exit()

print("*"*20)

def func(n):
    print("starting fun yield")
    for i in range(0,n):
        val = yield i        
        print (val)
 
f1 = func(10)

print (next(f1))
print(f1.send(2)) 
f1.send(10)

print("*"*20)

# print (next(f1))

# print (next(f1))


def counter(n):
    while n<10:
        n = n+1
        yield n

for i in counter(0):
    print(i,end=" ")


print("\n")
print("*"*20)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)