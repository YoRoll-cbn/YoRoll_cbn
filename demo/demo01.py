'''
print("hello word！") #字符串
print(980702) #整数
print(98.0702) #小数
print(True) #布尔值
print(()) #元组
print([]) #数组
print({}) #字典啊
print("张颜齐",980702)
print("张颜齐"+"林彦俊")
print("张颜齐"*20)
print(((1+2)*300-99)/2)
a=input("请输入：")
print("input获取的内容",a)
print(type(980702),type(()),type([]),type({}))
print(type(int("980702")))
a=float(input("请输入："))
b=float(input("请输入："))
print("a+b=",a+b)
print(len("1323546"))

a=(1,2,3,4,"zyq","zyq","zyq","zyq","zyq","zyq","zyq","zyq","zyq","zyq","zyq","zyq","zyq","lyj",True,(1,"YoRoll-cbn"))
# print(a.index("lyj"))
# print(a.index("zyq"))
# print(a.count("zyq"))
# print(a[a.index((1,"YoRoll-cbn"))][1])
print(a[0:4])
print(a[4:17])
print(a[17:])
a=[1,2,3,4,"zyq","lyj",True,(1,"YoRoll-cbn")]
a.append("张颜齐")
print(a)
a={"name":"zyq","age":23,0:"哈哈"}
# #取值
# print(a["name"])
# #新增
# a["high"]="183cm"
# print(a)
# #修改
# a["age"]=22
print(a)
print(a.get("name"))
a.update(grade=90)
print(a)
b=a.pop("grade")
print(b)
print(a)
a.update(grade=90)
print(a)
a.update(grade=80)
a.update(name="张颜齐")
print(a)
a="zyq"+\
    "lyj"+\
        "YoRoll-cbn"
print(a)
a=[("123456","123456"),("123456","1234567"),("12345","12345"),("","666666"),("666666",""),("666666","666666")]
for i in a:
    print(i[1])
    print(type(i[0]))
a="成功删除"
b="网络错误！"'''
print(a+b)
c=0
def a():
    global c
    b=1
    if b==True:
        c=2
    print(c)
a()
print(c)
#create a function:
def myfunction():
  global x
  x = "hello"

#execute the function:
myfunction()
#x should now be global, and accessible in the global scope.
print(x)