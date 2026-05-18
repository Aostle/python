import random

def create_double_color():
    red_balls = random.sample(range(1, 34), 6)
    red_balls.sort() 
    blue_ball = random.randint(1, 16)
    return red_balls, blue_ball

if __name__ == "__main__":
    red, blue = create_double_color()
    print("本期随机双色球号码：")
    print(f"红球：{'  '.join(f'{num:02d}' for num in red)}")
    print(f"蓝球：{blue:02d}")