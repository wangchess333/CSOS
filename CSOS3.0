
def sign():
    name = input("请输入您的用户名")
    mimaq = input("请输入密码")
    mimaw = input("请再输入密码")
    if(mimaq == mimaw):         
                 q1 = open("name.password","w")
                 q2 = open("mima.password","w")
                 q1.write(name)
                 q2.write(mimaw)
                 q1.close()
                 q2.close()
                 print("注册成功!")
                 q1 = open("信息.xinxi", "w")
    else:
        print("两次输入密码错误，退出程序")
        exit()

              

def write():
    q2 = open("信息.xinxi", "a")
    xinxi = input("加入信息")
    xin = xinxi +'\n'
    q2.write(xin)
    q2.close()
    print("写入成功")
def read():
    w1 = open("信息.xinxi", "r")
    g = w1.read()
    w1.close()
    print(g)
    r1 = open("win.xinxi", "r")
    q = r1.read()
    r1.close()
    print(q)
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
                w = "打平"
                e = "电脑赢"
                r = "你赢"
                r2 = open("win.xinxi", "a")
                r2.write(w)
                r2.close()
            elif (b == 2):
                print(e)
                w = "打平"
                e = "电脑赢"
                r = "你赢"
                p = open("win.xinxi", "a")
                p.write(e)
                p.close()

            elif (b == 3):
                print(r)
                w = "打平"
                e = "电脑赢"
                r = "你赢"
                q2 = open("win.xinxi", "a")
                q2.write(r)
                q2.close()
            else:
                print("输入错误")
                exit()
        elif (a == "剪刀"):
            if (b == 1):
                print(r)
                w = "打平"
                e = "电脑赢"
                r = "你赢"
                l2 = open("win.xinxi", "a")
                l2.write(r)
                l2.close()
            elif (b == 2):
                print(w)
                w = "打平"
                e = "电脑赢"
                r = "你赢"
                n2 = open("win.xinxi", "a")
                n2.write(w)
                n2.close()
            elif (b == 3):
                print(e)
                w = "打平"
                e = "电脑赢"
                r = "你赢"
                g2 = open("win.xinxi", "a")
                g2.write(e)
                g2.close()
            else:
                print("输入错误")
                exit()
        elif (a == "布"):
            if (b == 1):
                print(e)
                w = "打平"
                e = "电脑赢"
                r = "你赢"
                u2 = open("win.xinxi", "a")
                u2.write(e)
                u2.close()
            elif (b == 2):
                print(r)
                w = "打平"
                e = "电脑赢"
                r = "你赢"
                q2 = open("win.xinxi", "a")
                q2.write(r)
                q2.close()
            elif (b == 3):
                print(w)
                w = "打平"
                e = "电脑赢"
                r = "你赢"
                y2 = open("win.xinxi", "a")
                y2.write(w)
                y2.close()
            else:
                print("输入错误")
                exit()

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
            print("恭喜你答对了!")
            break
        elif (b > w):
            print("大了！")
        elif (b < w):
            print("小了！")

def sin():
    q1 = open("信息.xinxi", "w")
    f1 = open("name.password","r")
    f2=open("mima.password","r")
    n = f1.read()
    s = f2.read()
    f1.close()
    f2.close()
    name = input("请输入用户名:")
    mima = input("请输入密码:")
    if(n == name):
        if(s == mima):
            print("登录成功")
            for i in range(30000):
                d = input('选择应用\n1.写入信息\n2.读取信息\n3.石头剪刀布\n4.随机画图\n5.数字炸弹\n6.退出')
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
                else:
                    exit()


            else:
                print("密码错误")
        else:
            print("用户名错误")
    print("三次错误，退出程序")
    exit()



w = input("1.注册\n2.登录")
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


          
       
                 
       
        
       
        
      
