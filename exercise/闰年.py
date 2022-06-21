
while True:
    year = int(input("请输入年份:"))

    print ('闰年' if(year%4==0 and year%100!=0) or year%400==0  else '平年' )

    choice = input("继续y,退出n:")

    if(choice=='n'):
        break

