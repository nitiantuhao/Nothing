class Wages_management():
    def __init__(self):
        self.wagess=0
    def worker_wages(self,hour):
        time_salaer=100
        self.wagess=time_salaer*hour
        return self.wagess
    def salesman_wages(self,sales):
        self.wagess=sales*0.2
        return self.wagess
    def manager_wages(self):
        print('今月工资:12000')
        print('请查收')
    def sales_manager_wages(self,sales):
        self.wagess=sales*0.3
        return self.wagess
print('1.工人\n2.销售员\n3.经理\n4.销售经理\n')
while True:
    mgs = input('清选择:')
    if mgs=='1':
        h=int(input('输入工作时长:'))
        w=Wages_management()
        print('您的工资是:',w.worker_wages(h))
        continue
    elif mgs=='2':
        x=int(input('输入销售额:'))
        w = Wages_management()
        print('您的工资是',w.sales_manager_wages(x))
        continue
    elif mgs=='3':
        w = Wages_management()
        w.manager_wages()
        continue
    elif mgs=='4':
        xs=int(input('输入销售额:'))
        w = Wages_management()
        print(w.sales_manager_wages(xs))
        continue
