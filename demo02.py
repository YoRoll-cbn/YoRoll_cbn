"""
a=2
b=3
if a>b:
    print("a比b大")
else :
    print("a比b小")
c=input("请输入：")
if type(c) is str:
    c=int(c)
print(type(c))

a, b = map(int, input().split())
if a>=0 and b<=10**8 :
    print(a+b)
print(10**8)
a=[1,2,3,4,"zyq","lyj",True,(1,"YoRoll-cbn")]
for i in a:
    print(i)
num1=1
num2=2
sum=num1+num2
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))

#99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,end="     ")
    print()

#红绿灯
light={"红灯":30,"绿灯":35,"黄灯":3}
for i in light:
    for j in range(light[i]):
        print(i,"还有",light[i]-j,"秒")
"""
#写一个方法计算一个数的阶乘
# def Factorial(num):
#     """
#     这个方法是计算阶乘
#     """
#     for i in range(1,num):
#         num=num*i
#     return num
# num=int(input("请输入一个整数："))
# print(Factorial(num))
try:
    print(1+"1")
except Exception as e:
    print("代码出现错误",e)
    print(e)