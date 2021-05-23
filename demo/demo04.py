# import time
# now=time.strftime("%y-%m-%d %H:%M:%S")
# print(now)
# txt=input("请输入今天的文案：")
# with open("文案.txt","a",encoding="utf-8") as f:
#     f.write(txt+"\n")
with open("文案.txt","r",encoding="utf-8") as f:
    text=f.readlines()
for i in text:
    print(i)