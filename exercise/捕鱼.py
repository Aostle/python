
def main():
    fish =1
    while True:
        total , enough = fish,True
        for _ in range(4):
            if(total-1)%4==0:
                total=(total-1)//4*3
            else:
                enough = False
                break
        if enough:
            print(f'至少有{fish}条鱼')
            break
        fish+=1

if __name__ == '__main__':
    main()
