import time
import gevent
from gevent import monkey
monkey.patch_all()#起自动切换作用[猴子补丁]
def a():#协程A
    for i in range(4):
        print('A'+str(i))
        time.sleep(0.5)
def b():#协程B
    for i in range(4):
        print('B'+str(i))
        time.sleep(0.5)
def c():#协程C
    for i in range(4):
        print('C'+str(i))
        time.sleep(0.5)
if __name__ == '__main__':
    g1=gevent.spawn(a)#调用协程
    g2=gevent.spawn(b)#调用协程
    g3=gevent.spawn(c)#调用协程
    g1.join()#堵塞出口，完成才能下一步
    g2.join()#堵塞出口，完成才能下一步
    g3.join()#堵塞出口，完成才能下一步
    print('end')
