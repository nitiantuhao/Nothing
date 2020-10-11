import os
def Register():#注册系统
    username = input('输入用户名')
    password = input('输入密码')
    passwordok = input('确认密码')
    if password==passwordok:
        with open(r'C:\Users\dell\PycharmProjects\untitled\图书馆书籍管理系统\name.txt','w')as syor:
            syor.write('{} {}\n'.format(username,password))
            print('注册成功')
    else:
        print('两次密码不一致')
        choose()
def log_in():#登陆判断
    username=input('输入用户名')
    password=input('输入密码')
    with open(r'C:\Users\dell\PycharmProjects\untitled\图书馆书籍管理系统\name.txt')as syor2:
        user_pass=('{} {}\n'.format(username,password))
        while True:
            real=syor2.readline()
            if real==user_pass:
                print('登陆成功')
                break
            else:
                print('登陆失败')
                break
def choose():
    print('登陆\注册')
    result=input('请选择:')
    if result=='登陆':
        log_in()
    else:
        Register()
choose()




