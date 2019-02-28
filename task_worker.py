import time,sys,queue
from multiprocessing.managers import BaseManager

#创建QueueManager
class QueueManager(BaseManager):
    pass

#由于这个QueueManager从网络中获取，所以只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器，也就是是运行task_master的代码
sever_addr = '127.0.0.1'
print('Connect to sever %s...' % sever_addr)
#端口号和验证码保持一致
m = QueueManager(address=(sever_addr,5000),authkey=b'abc')
#从网络连接
m.connect()
#后去queue对象
task = m.get_task_queue()
result = m.get_result_queue()
#从task队列取任务，把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=10)
        print('Run task %d*%d' % (n,n))
        r = '%d * %d = %d' % (n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty')
#处理结果
print('worker exit')
