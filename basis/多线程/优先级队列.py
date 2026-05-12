import threading
import queue
import time

# print的默认end为"\n"，但end和print函数不是一起操作的，这就会造成还未来得及打印end就切换到了其他线程去。
# 修改方法可以人为指定换行符，并指定end=‘’ ，
# 如 print(f"print1 now is {n}\n",end='')

class Worker(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.start()  # 执行run()    
    def run(self):
        # 循环，保证接着跑下一个任务        
        while True:
            # 队列为空则退出线程            
            if self.queue.empty():
                break            
            # 获取一个队列数据
            foo = self.queue.get()
            # queueLock.acquire()
            print(self.name + " process " + str(foo)+"\n",end='')
            # queueLock.release()          
            # 延时1s模拟你要做的事情            
            time.sleep(1)
            # 任务完成            
            self.queue.task_done()

# queueLock = threading.Lock()

# 队列
queue = queue.Queue()
# 加入10个任务队列
for i in range(10):
    queue.put(i)
# 开3个线程
for i in range(3):
    threadName = 'Thread' + str(i)
    Worker(threadName, queue)
# 阻塞等到队列中所有的任务都被get并且接受到相应的task_down调用后,代表所有线程执行完毕
queue.join()