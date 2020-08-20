from multiprocessing import Process
def a1():
    for i in range(4):
        print('任务1')
def a2():
    for i in range(4):
        print('任务2')
if __name__=='__main__':
    p=Process(target=a1,args=(1,))
    p.start()
    p1=Process(target=a2)
    p1.start()