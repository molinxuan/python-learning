#
year=[1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,]
yearRUN=0
for i in year:
    if i % 4 == 0 and i % 400 !=0:
        yearRUN = i
        print(f"{yearRUN}是闰年")
        continue
if yearRUN == 0:
    print("没有闰年")
print()
num=3
res=0
while num<=20:
        for i in range(2,num):
            if num % i !=0:
                res = num
            else:
                res = 0
                break
        if res != 0:
            print(f"{res}是质数")
            num += 1
        else:
            num += 1

n1 = int(input("请输入一个数字："))
n2 = int(input("请输入另一个数字："))
i = int(input("请选择一个运算符，加1减2乘3除4："))
if i == 1:
    print(f"{n1} + {n2} = {n1 + n2}")
elif i == 2:
    print(f"{n1} - {n2} = {n1 - n2}")
elif i == 3:
    print(f"{n1} * {n2} = {n1 * n2}")
elif i == 4:
    if n2 != 0:
        print(f"{n1} / {n2} = {n1 / n2}")
    else:
        print("除数不能为零")

l=1
s=1
while l <=5:
    while s<=5:
        print("*",end="")
        s += 1 
    print()
    l += 1
    s = 1

p=2
y=[]
r=0
while p <= 100:
    for i in range(1,p):
        if p % i == 0:
            y.append(i)
    for s in y:
        r=r+s
    if p == r:
        print(f"{p}是完全数")
    r=0
    p+= 1
    y.clear()

        
    

 
        
        
