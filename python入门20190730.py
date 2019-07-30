#!/usr/bin/env python
# coding: utf-8

# In[1]:

var1="hello world!"
var1[0]

name = 'Python语言程序设计'
name.find('语言')
name.find('none')

list1 = [1,2,3,4,5]
list1   #显示列表

list2 = [1,2,3,'a','b']
list2[3]     #显示列表中元素，注意是012345

del list1[4]   #删除列表中的元素
list2

list2.append('c')  #添加一个元素到列表
list2

list2.extend(list1) #新列表扩展到原有列表中
list2

list2.index('c')  #找到某个值的索引值
list2.count(2)  #统计某个元素出现的次数，注意字符串要用'。
list1.sort()  #列表内容排序，从小到大
list1


# In[19]:
d={'a':1,'b':2,'c':3,'d':4,'e':5}
d["e"]
d['f']=6
d

del d['f']
d

#单分支if语句
R = eval(input("请输入实数值："))
if R < 0
print("绝对值",R) 


# 判断用户输入数字的奇偶性 
s = eval(input("请输出一个整数："))
if s % 2 == 0:
    print("这是个偶数")
print("输入数字是:", s)

# 判断用户输入数字的特定 
s = eval(input("请输出一个整数："))
if s % 3 == 0 and s % 5 == 0:     #多个条件用and火or进行逻辑组合
    print("这个数字既能被3整除，又能被5整除")
print("输入数字是:", s)

#if else
pm = eval(input("请输入PM2.5数值："))
print("空气{}污染！".format("存在" if pm >= 75 else "没有"))

# 将百分制成绩转换为五分制成绩
# 将百分制成绩转换为五分制成绩
score = eval(input("请输出一个百分制成绩："))
if score >= 90.0:
	grade = "A"
elif score >= 80.0:
	grade = "B"
elif score >= 70.0:
	grade = "C"
elif score >= 60.0:
	grade = "D"
else:
      grade = "E"
print("对应的五分制成绩是：{}".format(grade))


4<5

0 == False

a = 80
( a > 100) or ( a > 50 and a < 90)


#for
for i in range(5):
    print(i)
 
    
for s in "PY":    #遍历结构可以是字符串、文件、range()函数或组合数据类型等。

    print("循环执行中: " + s)
else:
    s = "循环正常结束"
print(s)

#
n = 0
while  n < 10:
    print(n)
    n = n + 3


while True:
    s = input("请输入一个名字(按Q退出): ")
if s == "Q":
    break
print("输入的名字是:", s)
print("程序退出")


for s in "PYTHON":
    if s == "Y" or s == "Y":
        continue
print(s, end="")


import random
target = random.randint(1,1000)
count = 0
while True:
    guess = eval(input('请输入一个猜测的整数(1至1000)：'))
count = count + 1
if guess > target:
    print('猜大了')
elif guess < target:
    print('猜小了')
else:
    print('猜对了')
break
print("此轮的猜测次数是:", count)
