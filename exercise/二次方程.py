
import cmath
a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

d = b**2-4*a*c

s1= (-b + cmath.sqrt(d) )/(2*a)
s2= (-b - cmath.sqrt(d) )/(2*a)

print("结果为{0:.3f}和{1:.3f}".format(s1,s2))

