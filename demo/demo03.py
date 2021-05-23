# import time
# import random  #生成随机数
# for i in range(10):
#     time.sleep(1)#每次停顿1s
#     print(i)
#     print(random.randint(0,100)) #随机生成0,100的数
class Boyfriend():
    def __init__(self,name,high,sex,age) :
        self.name=name
        self.high=high
        self.sex=sex
        self.age=age
    def rapper(self,num):
        """
        AKA YoRoll
        """
        if num==1:
            print("Let's Roll baby")
        elif num==2:
            print("生活他有时好也有时坏，我或许不太明白")
        else:
            print("这世界原本就不存在什么该也不该，也许你先问自己对这世界爱或不爱，如果说世界它本是一座山和一片海，你只有一次机会，选择只有来与不来")

#类的实例化
zyq=Boyfriend("张颜齐","183cm","男",22)
zyq.rapper(1)
zyq.rapper(2)
zyq.rapper(3)
print(zyq.name)
print("--------------------------")
#继承与重写
class Boy(Boyfriend):
     def rapper(self,num):
         if num==1:
             print("等待整个冬天")
         elif num==2:
            print("你没出现")
         else:
            print("现在依然下着雪")
#继承的类直接拥有被继承的类的所有方法与属性
lyj=Boy("林彦俊","181cm","男",25)
print(lyj.name)
lyj.rapper(1)
lyj.rapper(2)
lyj.rapper(3)