import math
while True:
    print("请输入圆的半径r")
    try:
        r = float(input("请输入半径r:"))

    except ValueError:
        print("请重新输入正确的数字")
    else:
        if r>=0:
            p=math.pi
            square=p*r**2
            print('您所求的圆的面积为：%.4f'%square)
        else:
            print()
        active = input('\n是否继续？(y/n): ')
        if active == 'n':
          break