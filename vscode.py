import random
i=0
while i <=3:
    print('欢迎加入游戏')
    num4=int(input('输入充值金额:'))
    if num4%2==0:
        print('充值成功')
    else:
        print('充值失败')
        break
    k = 1
    while k<=num4/2:
        ran1=random.randint(1,7)
        ran2=random.randint(1,7)
        print(ran1+ran2)
        ran3 = input('请猜大或小:')
        if ran1+ran2>6 and ran3=='大':
            print('猜对了')
            num4+=2
        elif ran1+ran2<=6 and ran3=='小':
            print('猜对了')
            num4+=2
        else:
            print('猜错了')
        k+=1
    i+=1