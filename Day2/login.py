import uuid
import sys


def outUsernamePassword():
    username = input('请输入用户名:\n')
    password = input('请输入用户名密码:\n')
    return username, password


def register():
    username, password = outUsernamePassword()
    temp = username + '|' + password
    with open('login.md', 'w') as f:
        f.write(temp)


def login(username, password):
    with open('login.md', 'r') as f:
        for item in f:
            lists = item.split('|')
            if lists[0] == username and lists[1] == password:
                return True
            else:
                print('sorry，您的登录账户错误')


def profile():
    with open('login.md', 'r') as f:
        for item in f:
            lists = item.split('|')
            print('恭喜登录成功，您的账号为:{0}'.format(lists[0]))


def exit():
    sys.exit(1)


def main():
    while True:
        p = int(input('1. 登录  2. 注册 3. 退出 \n'))
        if p == 1:
            username, password = outUsernamePassword()
            isLogin = login(username=username, password=password)
            if isLogin:
                profile()
        elif p == 2:
            register()
        elif p == 3:
            exit()
        else:
            break


if __name__ == '__main__':
    main()