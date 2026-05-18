import random

def get_daletou():
    # 前区5个 1~35
    front = sorted(random.sample(range(1, 36), 5))
    # 后区2个 1~12
    back = sorted(random.sample(range(1, 13), 2))
    return front, back

# 单注生成
if __name__ == "__main__":
    qian, hou = get_daletou()
    print("随机大乐透号码")
    print(f"前区：{'  '.join(f'{n:02d}' for n in qian)}")
    print(f"后区：{'  '.join(f'{n:02d}' for n in hou)}")