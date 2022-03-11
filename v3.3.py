import requests,os,time,sys,curses
def DownloadFile2(mp3_url, save_url,file_name):
    try:
        if mp3_url is None or save_url is None or file_name is None:
            print('参数错误')
            time.sleep(3)
            return None
        folder = os.path.exists(save_url)
        if not folder:
            os.makedirs(save_url)
        res = requests.get(mp3_url,stream=True) 
        total_size = int(int(res.headers["Content-Length"])/1024+0.5)

        file_path = os.path.join(save_url, file_name)
        from tqdm import tqdm
        with open(file_path, 'wb') as fd:
            print('开始下载文件：{},当前文件大小：{}KB'.format(file_name,total_size))
            for chunk in tqdm(iterable=res.iter_content(1024),total=total_size,unit='k',desc=None):
                fd.write(chunk)
            print(file_name+' 下载完成！')
            time.sleep(5)
            os.system('cls')
    except:
        print("程序错误")
        time.sleep(3)
        os.system('cls')




def sign():
    import getpass,hashlib
    name = input("请输入您的用户名")
    mimaq = getpass.getpass('输入密码:')
    mimaw = getpass.getpass('再次输入密码:')
    if(mimaq == mimaw):         
                 q1 = open("name.password","w")
                 q2 = open("mima.password","w")
                 e = hashlib.md5()
                 e.update(name.encode("utf8"))
                 xx1 = e.hexdigest()
                 m = hashlib.md5()
                 m.update(mimaq.encode("utf8"))
                 xx = m.hexdigest()
                 q1.write(xx1)
                 q2.write(xx)
                 q1.close()
                 q2.close()
                 print("注册成功!")
                 time.sleep(5)
                 os.system('cls')
                 q1 = open("信息.xinxi", "w")
                 time.sleep(5)
                 os.system('cls')
    else:
        print("两次输入密码错误，退出程序")
        time.sleep(5)
        exit()

              

def write():
    q2 = open("信息.xinxi", "a")
    xinxi = input("加入信息")
    xin = xinxi +'\n'
    q2.write(xin)
    q2.close()
    print("写入成功")
def write():
    q2 = open("信息.xinxi", "a")
    xinxi = input("加入信息")
    xin = xinxi +'\n'
    q2.write(xin)
    q2.close()
    print("写入成功")
def read():
    cho = input("请选择: 1.信息 2.石头剪刀布战绩")
    if cho == "1":
        w1 = open("信息.xinxi", "r")
        g = w1.read()
        w1.close()
        print(g)
        return 0
    elif cho == "2":
            try:
                r1 = open("win.xinxi", "r")
                q = r1.read()
                r1.close()
                print(q)
                return 0
            except:
                print("您未进行石头剪刀布游戏")
                return 0 
def stone():
    w = "打平"
    e = "电脑赢"
    r = "你赢"
    for i in range(1000):
        import random
        print("石头1，剪刀2，布3")
        a = random.choice(("石头", "剪刀", "布"))
        b = input("请出拳")
        b = int(b)
        if (a == "石头"):
            if (b == 1):
                print(w)
                w = "打平\n"
                r2 = open("win.xinxi", "a")
                r2.write(w)
                r2.close()
            elif (b == 2):
                print(e)
                e = "电脑赢\n"
                p = open("win.xinxi", "a")
                p.write(e)
                p.close()

            elif (b == 3):
                print(r)
                r = "你赢\n"
                q2 = open("win.xinxi", "a")
                q2.write(r)
                q2.close()
            else:
                print("输入错误")
                time.sleep(5)
                os.system('cls')
                return 0
        elif (a == "剪刀"):
            if (b == 1):
                print(r)
                r = "你赢\n"
                l2 = open("win.xinxi", "a")
                l2.write(r)
                l2.close()
            elif (b == 2):
                print(w)
                w = "打平\n"
                n2 = open("win.xinxi", "a")
                n2.write(w)
                n2.close()
            elif (b == 3):
                print(e)
                e = "电脑赢\n"
                g2 = open("win.xinxi", "a")
                g2.write(e)
                g2.close()
            else:
                print("输入错误")
                time.sleep(5)
                os.system('cls')
                return 0
        elif (a == "布"):
            if (b == 1):
                print(e)
                e = "电脑赢\n"
                u2 = open("win.xinxi", "a")
                u2.write(e)
                u2.close()
            elif (b == 2):
                print(r)

                r = "你赢\n"
                q2 = open("win.xinxi", "a")
                q2.write(r)
                q2.close()
         
            elif (b == 3):
                print(w)
                w = "打平\n"
                y2 = open("win.xinxi", "a")
                y2.write(w)
                y2.close()
            else:
                print("输入错误")
                time.sleep(5)
                os.system('cls')
                return 0

def draw():
    import turtle
    import random
    t = turtle.Pen()
    s = random.randint(50, 100)
    t.forward(s)
    a = random.randint(90, 360)
    t.left(a)
    s = random.randint(50, 100)
    t.forward(s)
    a = random.randint(90, 360)
    t.left(a)
    s = random.randint(50, 100)
    t.forward(s)
def sui():
    import random
    w = random.randint(1, 100)
    while 1:
        b = input("请输入100-1的整数:")
        b = int(b)
        if (b == w):
            print("恭喜你答对了!,5秒后退出")
            time.sleep(5)
            os.system('cls')
            break
        elif (b > w):
            print("大了！")
        elif (b < w):
            print("小了！")
def clock():
    import os
    import time
    while True:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        time.sleep(1)
        os.system('cls')
def sin():
    import getpass,hashlib
    q1 = open("信息.xinxi", "w")
    f1 = open("name.password","r")
    f2=open("mima.password","r")
    n = f1.read()
    s = f2.read()
    f1.close()
    f2.close()
    name = input("请输入用户名:")
    mima = getpass.getpass("请输入密码:")
    e = hashlib.md5()
    e.update(name.encode("utf8"))
    xx1 = e.hexdigest()
    m = hashlib.md5()
    m.update(mima.encode("utf8"))
    xx = m.hexdigest()
    if(n == xx1):
        if(s == xx):
            print("登录成功")
            for i in range(30000):
                d = input('选择应用\n1.写入信息\n2.读取信息\n3.石头剪刀布\n4.随机画图\n5.数字炸弹\n6.退出\n7.时钟\n8.下载文件\n9.about')
                global write
                global read
                global stone
                global draw
                global sui
                if d == '1':
                    write()
                elif d == '2':
                    read()
                elif d == '3':
                    stone()
                elif d == '4':
                    draw()
                elif d == '5':
                    sui()
                elif d == '6':
                    exit()
                elif d == '7':
                    clock()
                elif d == '8':
                    mp3_url = input("urls:")
                    save_url='./d/'
                    file_name =  os.path.basename(mp3_url)
                    DownloadFile2(mp3_url,save_url, file_name)
                elif d == '9':
                    import os
                    os.system('cls')
                    print('=====CSOS=====\n')
                    print("hello")
                    print("by wangchess333.com '博说技术'\n")
                    print("\n\nrelease:v3.0")
                    print('=====CSOS=====')
                    time.sleep(10)
                else:
                    return 0


            else:
                print("密码错误")
        else:
            print("用户名错误")
    print("三次错误，退出程序")
    exit()

try:
    u2 = open("run.dll", "r")
    run = u2.read
    if run == 'ok':
        pass
    else:
        raise Exception("运行库下载安装失败")
        print("运行库下载安装失败")
except:
    print("需下载运行库，是否下载运行库?按Y下载，按N退出")
    in_content = input("请输入：")
    if in_content == "Y"or in_content == "y":
        os.system('pip install -r requirements.txt')
        try:
            import getpass,hashlib,requests,os,time,sys,curses,random,turtle
        except:
            print("下载失败，5秒后退出！")
            u2 = open("run.dll", "a")
            u2.write("wrong")
            u2.close()
            time.sleep(5)
            exit(0)
        u2 = open("run.dll", "a")
        u2.write("ok")
        u2.close()
        os.system('cls')
        print("下载成功！")
        sign()
        sin()
    elif in_content == "N"or in_content == "n":
        print("已退出了该程序！")
        time.sleep(5)
        exit(0)
    else:
        print("你输入的内容有误，5秒后退出！")
        time.sleep(5)
        exit(0)

w = input("1.重新注册\n2.登录")
w = int(w)
if w == 1:
    sign()
    sin()
elif w == 2:
    sin()
else:
    print('wrong')
    print('exit')
    exit()
