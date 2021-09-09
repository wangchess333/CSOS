q1 = open("信息.txt","w")
w = input("1.注册 2.登录")
w = int(w)
if(w == 1):
    name = input("请输入您的用户名")
    mimaq = input("请输入密码")
    mimaw = input("请再输入密码")
    while(mimaq != mimaw):
        mimaq = input("请输入密码")
        mimaw = input("请再输入密码")
        if(mimaq == mimaw):
         q1 = open("name.txt","w")
         q2 = open("mima.txt","w")
         q1.write(name)
         q2.write(mimaw)
         q1.close()
         q2.close()
         print("注册成功!")
        else:
            print("两次输入密码错误,请再输入密码")
if(w == 2):
    f1 = open("name.txt","r")
    f2=open("mima.txt","r")
    n = f1.read()
    s = f2.read()
    f1.close()
    f2.close()
    for i in range(30000):
        name = input("请输入用户名:")
        mima = input("请输入密码:")
        if(n == name):
            if(s == mima):
                print("登录成功")
                for i in range(10):
                    w = input("1.写入 2.读取")
                    w = int(w)
                    if(w == 1):
                        q2 = open("信息.txt","a")
                        xinxi = input("加入信息")
                        q2.write(xinxi)
                        q2.close()
                        print("写入成功")
                    if(w == 2):
                        w1=open("信息.txt","r")
                        g = w1.read()
                        w1.close()
                        print(g)
            else:
                print("密码错误")
        else:
            print("用户名错误")
    print("三次错误，退出程序")
    exit()
            
          
       
                 
       
        
       
        
      
