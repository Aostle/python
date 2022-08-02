import threading
 
xuewei_account = dict()
xuewei_account['amount'] = 100
 
 
# amount为负数即是转出金额
def transfer(money):
    for i in range(100000):
        xuewei_account['amount'] = xuewei_account['amount'] + money
 
 
# 创建400个任务重复给学委账户转账
threads = []
for i in range(200):
    t1 = threading.Thread(target=lambda: transfer(-1))
    threads.append(t1)
    t2 = threading.Thread(target=lambda: transfer(1))
    threads.append(t2)

print('开启线程数:%s' %len(threads))

for t in threads:
    t.start()
for t in threads:
    t.join()
 
print("-" * 16)
print("活跃线程数:", threading.active_count())
print("活跃线程:", threading.current_thread().name)
print("学委账户余额：", xuewei_account)