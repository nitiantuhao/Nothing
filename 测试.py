#format应用
movie = '你的名字'
ticket = 30.9
count = 40
message = '''
电影名:{}
票价:{}
人数:{}
''' .format(movie,ticket,count)
print(message)

age = 18
print('小明{}岁'. format(age))


#占位符应用
movie =input('输入电影名称:')
ticket =input('输入票价:')
count =input('输入人数:')
ticket=int(ticket)
count=int(count)
money=ticket*count
message='''
电影名称:%s
票价:%.0f
人数;%d
总票房:%.0f'''%(movie,ticket,count,money)
print(message)

#if语句应用
name=input('请输入姓名:')
age=input('请输入年龄:')
gender=input('请输入您的性别')
if name=='jasmine' and age>'18'and gender=='女':
    print('登陆成功,确认您的信息,姓名:{},年龄:{}岁,性别{}'.format(name,age,gender))
    see=input('确实是否正确:')
    if see=='正确':
        print('')
print('')
#随机数猜测小游戏
import random #调用随机数模块
ran=random.randint(1,10) #产生随机数,并赋值给ran
print(ran)#作弊用的，即输出随机数
ran1=int(input('输出猜测数'))#将猜测随机数输入,ps:int为将输入数转为整型否
if ran==ran1: #如果对了将从这输出
    print('猜对了')
else:    #如果错了将从这输出
    print('猜错了')
#随机数猜测小游戏2.0
for i in range(3):
    import random  # 调用随机数模块
    ran = random.randint(1, 10)  # 产生随机数,并赋值给ran
    print(ran)  # 作弊用的，即输出随机数
    ran1 = int(input('输出猜测数'))  # 将猜测随机数输入,ps:int为将输入数转为整型否
    if ran == ran1:  # 如果对了将从这输出
        print('猜对了')
        break#若猜对了将结束循环,break起结束作用
    else:  # 如果错了将从这输出
        print('猜错了')
#随机数猜测小游戏3.0
i=0
while i<=2:
    import random  # 调用随机数模块
    ran = random.randint(1, 10)  # 产生随机数,并赋值给ran
    print(ran)  # 作弊用的，即输出随机数
    ran1 = int(input('输出猜测数'))  # 将猜测随机数输入,ps:int为将输入数转为整型否
    if ran == ran1:  # 如果对了将从这输出
        print('猜对了')
        break#若猜对了将结束循环,break起结束作用
    else:  # 如果错了将从这输出
        print('猜错了')
#分数分类系统,虽然是垃圾
score=int(input('输入分数:'))
if score<= 100 and score>=90:
    print('优+')
elif score<90 and score>=80:
    print('优-')
elif score<80 and score>=70:
    print('良')
elif score<70 and score>=60:
    print('差')
elif score<60 and score>=0:
    print('未及格')
elif score > 100:
    print('您输入的数字大于100')
#for循环应用
name=input('输入玩家姓名:')
num1=int(input('请输入馒头数量:'))
num=int(input('设定那个是毒馒头:'))
for i in range(num1):
    if i+1==num:
        print('毒馒头')
    else:
        print('{}正在吃,第{}个馒头'.format(name,i+1))
print('{}吃饱了,一共吃了了{}个馒头'.format(name,num1-1))
#用户登录系统
for i in range(3):
    name=input('输入用户名:')
    password=input('请输入密码:')
    if name=='jasmine' and password=='123456':
        print('')
        break
    else:
        print('密码或用户名有误')
#用户登录系统二型
for i in range(3):
    name=input('输入用户名:')
    password=input('请输入密码:')
    if name=='jasmine' and password=='123456':
        print('欢迎指挥官')
        break
    else:
        print('密码或用户名有误')
else:#防止出现输入正确后，也跳出此界面
    print('账户已经被冻结')
#需注意不能改为print('账户已被冻结'),就算输对了，也还是会出'现账户已被冻结'
#关于取倍数的可用思路
#方式1
i=1
while i<=30:
    if i%3==0:
        print(i)
    i += 1
#方法2
i=3
while i<=27:
    i+=3
    print(i)
#关于取在一定范围内去两个整数倍数的代码参考思路
i=1
while i<=30:
    if i%3==0 and i%5==0:
        print(i)
    i+=1
#累计加值求和
sum=0
i=1
while i<=20:
    sum+=i
    i+=1
print(sum)
#
i=1
while i<=7:
    print('*'*i)
    i+=1
print('打印完成')
#三角形生成器
hight=int(input('输入三角形高度:'))
for i in range(1,hight+1):
    print('*'*i)
print('打印完成')
#通用三角形生成器
ceng=1
while ceng<=5:
    count=1
    while count<=ceng:
        print('*',end='')
        count+=1
    ceng+=1
    print()
#九九乘法表(大成之作)
ceng=1
while ceng<=9:
    hang=1
    while hang<=ceng:
        print('{}x{}={}'.format(hang,ceng,ceng*hang),end=' ')
        hang+=1
    ceng+=1
    print()
#骰子游戏1.1
import random
i=0
while i<3:
    name=input('输入姓名:')
    if name=='jasmine':
        print('欢迎加入游戏')
        ran1=random.randint(1,7)
        ran2=random.randint(1,7)
        print(ran1+ran2)
        ran3 = input('请猜大或小:')
        if ran1+ran2>6 and ran3=='大':
            print('猜对了')
            break
        else:
            print('猜错了')
    else:
        print('用户名错误,请重新输入')
    i+=1
else:
    print('您的账户已被冻结')
#骰子游戏1.2
import random
i=0
while i<3:
    name=input('输入姓名:')
    if name=='1':
        print('欢迎加入游戏')
        k=0
        while k<=1:
            ran1=random.randint(1,7)
            ran2=random.randint(1,7)
            print(ran1+ran2)
            ran3 = input('请猜大或小:')
            if ran1+ran2>6 and ran3=='大':
                print('猜对了')
                break
            else:
                print('猜错了')
    else:
        print('用户名错误,请重新输入')
    i+=1
else:
    print('您的账户已被冻结')
#骰子游戏2.0(大改)
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
#骰子游戏2.1
import random
i=0
while i <=1:
    print('欢迎加入游戏')
    num4=int(input('输入充值金额:'))
    if num4%100==0:
        print('充值成功')
    else:
        print('充值失败')
        break
    k = 1
    num5=num4/100*30
    while k<=num5/2:
        print('您还有{}次机会'.format(num5/2))
        ran1=random.randint(1,7)
        ran2=random.randint(1,7)
        print(ran1+ran2)
        ran3 = input('请猜大或小:')
        if ran1+ran2>6 and ran3=='大':
            print('猜对了')
            num5+=2
        elif ran1+ran2<=6 and ran3=='小':
            print('猜对了')
            num5+=2
        else:
            print('猜错了')
            num5-=2
        k+=1
    i+=1
else:
    print('游戏结束')
#骰子游戏2.2
import random
i=0
while i <=1:
    print('欢迎加入游戏')
    num4=int(input('输入充值金额:'))
    if num4%100==0:
        print('充值成功')
    else:
        print('充值失败')
    i+=1
    k = 1
    num5 = num4 / 100 * 30
    while k<=num5/2:
        print('您还有{}次机会'.format(num5/2))
        ran1=random.randint(1,6)
        ran2=random.randint(1,6)
        print(ran1+ran2)
        ran3 = input('请猜大或小:')
        if (ran1+ran2>6 and ran3=='大')or(ran1+ran2<=6 and ran3=='小'):
            print('猜对了')
            num5+=2
        else:
            print('猜错了')
            num5-=2
        k+=0
else:
    print('游戏结束')
#随机验证码和验证码确认的应用与验证
import random
k='agaBeggReaGgigiJihhhUfAscasvfbnweoieyfgqpo'
j=len(k)
code=''
for i in range(4):
    s=random.randint(1,j-1)
    e=k[s]
    code+=e
print(code)
user_code=input('输入验证码')
if user_code.lower()==code.lower():#lower作用:将等号两边转为小写
    print('验证成功')
else:
    print('输入有误')
#格式识别验证与应用1.0
filmneme=input('输入图片地址:')
name=filmneme.rfind('\\')#找出文件名前门\位置
print(name)
name1=filmneme[name+1:]#将文件名提出来
print(name1)
if name1.endswith('png') or name1.endswith('jpg'):
    print('上传成功')
else:
    print('上传失败')
#‪D:\p站\cos\dlc_cos\coser401_15.jpg
#格式识别验证与应用1.1
i=0
while i<=2:
    filmneme=input('输入图片地址:')
    name=filmneme.rfind('\\')#找出文件名前门\位置
    print(name)
    name1=filmneme[name+1:]#将文件名提出来
    print(name1)
    if name1.endswith('png') or name1.endswith('jpg'):
        print('上传成功')
        break
    else:
        print('上传失败')
    i+=1
else:
    print('连续上传三次错误已被冻结')
#‪D:\p站\cos\dlc_cos\coser401_15.jpg
#格式识别验证与应用(无限版)
while True:
    filmneme = input('输入图片地址:')
    name = filmneme.rfind('\\')  # 找出文件名前门\位置
    print(name)
    name1 = filmneme[name + 1:]  # 将文件名提出来
    print(name1)
    if name1.endswith('png') or name1.endswith('jpg'):
        print('上传成功')
        break
    else:
        print('上传失败')

# ‪D:\p站\cos\dlc_cos\coser401_15.jpg
#加法累加循环自动识别验证与应用
sum=0
i=0
while  i<=2:
    num1=input('输入数字:')
    if num1.isdigit():
        num1=int(num1)
        sum+=num1#
        i+=1
        print('第{}个'.format(i))
    else:
        print('输入有问题')
print(sum)
#关于从一个字符串删除另一个同字符串相同内容并输出的验证与应用
num1=input('输入第一个字符串:')                 #They are students
num2=input('输入第二个字符串:') #aeiou
num3=''
for i in num1:#循环拓展与range()相似，i每次从num1中取一个字符，直到取完
    if i not in num2:#如果i里面没有num2的内容就向下输出
        num3+=i#输出到这与num3结合
print(num3)#循环结束输出
#关于从一个字符串删除另一个同字符串相同内容并输出的验证与应用的另一种思路
num1=input('输入第一个字符串:')                 #They are students
num2=input('输入第二个字符串:') #aeiou

for i in num1:#循环拓展与range()相似，i每次从num1中取一个字符，直到取完
    if i  in num2:#如果num2中字符串与i等则，向下输出
       num1=num1.replace(i,'')#接受输出,replace将一二两个相同部分字符替换成空字符
print(num1)#循环结束输出
#关于从一个字符串删除另一个同字符串相同内容并输出的验证与应用的另一种思路二
num1=input('输入第一个字符串:') #They are students
num2=input('输入第二个字符串:') #aeiouyy
num3=''
for i in num2:#循环拓展与range()相似，i每次从num1中取一个字符，直到取完
    if i not in num3:
        num3+=i#可以去除重复字母
print(num3)
for i in num3:
    num1=num1.replace(i,'')
print(num1)
#关于识别大小写与识别单词是否有连续相同字母的验证与应用
word=input('输入单词')#HEHLLO
for i in range(len(word)):
    if word[i]<'A' or word[i]>'Z':#进行大小写排查
        print('不喜欢,不是大写')
        break
    else:
        if i<len(word)-1 and word[i]==word[i+1]:
            print('不喜欢,有叠词')
else:
    print('喜欢')
#无题
s=''
while True:
    username=input('用户名:')
    password=input('密码:')
    email=input('邮箱:')

    username=username[0:20]
    password=password[0:20]
    email=email[0:20]

    meg='{}\t{}\t{}\n'.format(username,password,email)
    if username.lower()=='q'or password.lower()=='q'or email.lower()=='q':
        print('已结束输入')
        break
    s += meg
print(s)
#关于集合及其函数的随机数生成排序删重，及输入数字判断其是否存在集合并且删除的实验与运用
import random
s1=set()
k1=[]
for i in range(10):
    num1=random.randint(1,20)
    k1.append(num1)
s1=set(k1)#将列表转成集合且删除重复元素并进行排序
print(s1)
num1=int(input('输入数字:'))
s1.discard(num1)#注:使用discard无需赋值变量，可直接由print输出
print(s1)
#关于集合及其函数的随机数生成排序删重，及输入数字判断其是否存在集合并且删除的实验与运用的第二种思路
import random
set1=set()
for i in range(10):
    ran=random.randint(1,20)
    set1.add(ran)
print(set1)#set自带删重排序
num1=int(input('输入数字:'))#注:必须使用int
set1.discard(num1)
print(set1)
#嵌套函所与调用
c=88
def A():
    global c
    c=77
    a=99
    print(c)
    def B():
        global c
        nonlocal a
        a-=19
        c-=17
        b=88
        print(a,b,c)
    B()
A()
print(c)
#生成器私有化与装饰器@property
class student:
    def __init__(self,age):
        self.__age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if age>10:
            self.__age=age
        else:
            print('worss')
    # def getAge(self,age):
    #     return
s=student(18)
print(s.age)
s.age=20
print(s.age)
#__init__与普通方法的验证与应用
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
#
