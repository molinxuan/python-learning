#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习题 - 第2课：控制流语句
========================

完成以下练习来巩固你对控制流语句的理解。
请在每个TODO标记处填写你的答案。

提示：运行这个文件查看你的答案是否正确！
"""

print("🎯 开始第2课练习题")
print("=" * 50)

# ==========================================
# 练习1：基本条件判断
# ==========================================
print("\n📝 练习1：基本条件判断")

# TODO: 完成年龄判断程序
age = 16  # 你可以修改这个值来测试

# 请根据年龄判断并打印相应信息：
# 0-12岁：儿童
# 13-17岁：青少年  
# 18-59岁：成年人
# 60岁以上：老年人

if age <= 12:
    category = "儿童"
elif age <= 17:
    category = "青少年"
elif age <= 59:
    category = "成年人"
else:
    category = "老年人"

print(f"年龄 {age} 岁，属于：{category}")

# TODO: 完成成绩等级判定
score = 85  # 你可以修改这个值来测试

# 请根据分数判断等级：
# 90-100：A
# 80-89：B
# 70-79：C
# 60-69：D
# 0-59：F

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"分数 {score}，等级：{grade}")

# ==========================================
# 练习2：逻辑运算符
# ==========================================
print("\n📝 练习2：逻辑运算符")

# TODO: 判断三角形类型
a, b, c = 3, 4, 5  # 三角形三边长，你可以修改测试

# 首先判断是否能构成三角形（任意两边之和大于第三边）
if a + b > c and a + c > b and b + c > a:
    print(f"边长 {a}, {b}, {c} 能构成三角形")
    
    # TODO: 进一步判断三角形类型
    # 等边三角形：三边相等
    # 等腰三角形：两边相等
    # 普通三角形：三边都不相等
    
    if a == b == c:
        triangle_type = "等边三角形"
    elif a == b or b == c or a == c:
        triangle_type = "等腰三角形"
    else:
        triangle_type = "普通三角形"
    
    print(f"这是一个{triangle_type}")
else:
    print(f"边长 {a}, {b}, {c} 不能构成三角形")

# TODO: 用户权限检查
username = "admin"
password = "123456"
is_active = True

# 请完成登录验证逻辑
if username == "admin" and password == "123456" and is_active:
    print("登录成功")
else:
    print("登录失败")

# ==========================================
# 练习3：for循环基础
# ==========================================
print("\n📝 练习3：for循环基础")

# TODO: 计算1到10的和
total = 0
for i in range(1, 11):
    total += i

print(f"1到10的和是：{total}")

# TODO: 打印偶数
print("1到20的偶数：", end="")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# TODO: 倒数计数
print("倒数计数：", end="")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# TODO: 遍历字符串，统计元音字母
text = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"'{text}' 中有 {vowel_count} 个元音字母")

# ==========================================
# 练习4：while循环
# ==========================================
print("\n📝 练习4：while循环")

# TODO: 猜数字游戏（简化版）
import random
secret_number = random.randint(1, 10)
max_attempts = 3
attempts = 0

# 模拟几次猜测（在实际程序中可以用input()获取用户输入）
guesses = [5, 8, secret_number]  # 预设的猜测，最后一个肯定对

print(f"猜数字游戏开始！数字在1-10之间，你有{max_attempts}次机会")

for guess in guesses:
    if attempts >= max_attempts:
        break
        
    attempts += 1
    print(f"第{attempts}次猜测：{guess}")
    
    if guess == secret_number:
        print(f"恭喜你猜对了！答案是 {secret_number}")
        break
    elif guess < secret_number:
        print("太小了！")
    else:
        print("太大了！")
    
    if attempts == max_attempts:
        print(f"机会用完了！答案是 {secret_number}")

# TODO: 数字反转
number = 12345
reversed_number = 0

temp = number
while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp = temp // 10

print(f"数字 {number} 反转后是：{reversed_number}")

# ==========================================
# 练习5：break和continue
# ==========================================
print("\n📝 练习5：break和continue")

# TODO: 找出第一个能被7整除的数
numbers = [12, 15, 21, 8, 28, 35, 9]
print(f"在列表 {numbers} 中查找第一个能被7整除的数：")

for num in numbers:
    if num % 7 == 0:
        print(f"找到了：{num}")
        break
else:
    print("没有找到能被7整除的数")

# TODO: 跳过负数，计算正数的和
numbers = [5, -2, 8, -1, 3, -4, 7]
positive_sum = 0

print(f"计算列表 {numbers} 中所有正数的和：")
for num in numbers:
    if num < 0:
        print(f"跳过负数：{num}")
        continue
    positive_sum += num
    print(f"加上正数：{num}，当前和：{positive_sum}")

print(f"所有正数的和：{positive_sum}")

# ==========================================
# 练习6：嵌套循环
# ==========================================
print("\n📝 练习6：嵌套循环")

# TODO: 打印乘法表（1-5）
print("5以内的乘法表：")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j:2d}", end="  ")
    print()

# TODO: 绘制图案
print("\n星号三角形：")
for row in range(1, 6):
    for col in range(row):
        print("*", end=" ")
    print()

print("\n数字矩形：")
for i in range(4):
    for j in range(5):
        print(j + 1, end=" ")
    print()

# ==========================================
# 练习7：综合应用
# ==========================================
print("\n📝 练习7：综合应用")

# TODO: 质数判断
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("1到20中的质数：")
for num in range(1, 21):
    if is_prime(num):
        print(num, end=" ")
print()

# TODO: 统计字符类型
text = "Python123编程!"
letters = digits = chinese = others = 0

for char in text:
    if char.isalpha():
        if ord(char) > 127:  # 简单判断中文字符
            chinese += 1
        else:
            letters += 1
    elif char.isdigit():
        digits += 1
    else:
        others += 1

print(f"\n文本 '{text}' 的字符统计：")
print(f"英文字母：{letters}")
print(f"数字：{digits}")
print(f"中文字符：{chinese}")
print(f"其他字符：{others}")

# TODO: 数字游戏 - 找出数字中的最大和最小数字
number = 1847
digits_list = []

temp = number
while temp > 0:
    digits_list.append(temp % 10)
    temp = temp //= 10

max_digit = max(digits_list)
min_digit = min(digits_list)

print(f"\n数字 {number} 中：")
print(f"最大的数字是：{max_digit}")
print(f"最小的数字是：{min_digit}")

# ==========================================
# 挑战题（可选）
# ==========================================
print("\n🏆 挑战题（可选）")

# TODO: 闰年判断
year = 2024  # 可以修改这个值测试

# 闰年规则：能被4整除但不能被100整除，或者能被400整除
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")

# TODO: 完全数
print("\n1到100的完全数：")
for num in range(1, 101):
    divisor_sum = 0
    # 找出所有真因数（除了自己的因数）
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    
    # 如果真因数的和等于这个数，就是完全数
    if divisor_sum == num:
        print(f"{num} 是完全数")

# TODO: 数字金字塔
print("\n数字金字塔：")
rows = 5
for i in range(1, rows + 1):
    # 打印空格
    for space in range(rows - i):
        print(" ", end="")
    
    # 打印递增数字
    for j in range(1, i + 1):
        print(j, end="")
    
    # 打印递减数字
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    print()

# ==========================================
# 练习完成
# ==========================================
print("\n" + "=" * 50)
print("🎉 恭喜你完成了第2课的所有练习！")
print()
print("检查清单：")
print("✓ 掌握了if-elif-else条件判断")
print("✓ 学会了使用比较运算符和逻辑运算符")
print("✓ 熟练使用for循环遍历不同类型的数据")
print("✓ 掌握了while循环的使用场景")
print("✓ 理解了break和continue的作用")
print("✓ 能够编写嵌套循环结构")
print("✓ 解决了综合性的编程问题")
print()
print("下一步：继续学习第3课 - 函数！")
print("💪 Keep coding!")