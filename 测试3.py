# s=input('1.存款 2.取款 3.转账 4.显示当前账户信息:')
class bandcard:
    def __init__(self):   #
        self.moneys = 5000
        print('当前余额',self.moneys)
    def savemoney(self,money):
        self.moneys=(self.moneys-money)
        print('取款成功现余额为',self.moneys)
    def getmoney(self,money):
        self.moneys = (self.moneys + money)
        print('存款成功现余额为', self.moneys)
    def transfer(self):
        pass
print(' 1.存款\n 2.取款\n 3.显示当前账户信息\n 4.结束\n')

while True:
    s = input('请选择:')
    if s=='1':
        p=bandcard()
        p.savemoney(int(input('输入取款金额')))
        continue
    elif s=='2':
        p=bandcard()
        p.getmoney(int(input('输入存款金额')))
        continue
    elif s=='3':
        p=bandcard()
        continue
    elif s=='4':
        break



