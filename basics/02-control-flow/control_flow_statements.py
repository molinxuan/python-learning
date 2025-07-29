#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python基础教程 - 第2课：控制流语句
===============================

欢迎来到第二课！
这一课我们将学习如何让程序做出判断和重复执行任务。

学习目标：
1. 掌握条件判断（if-elif-else）
2. 学会使用比较运算符和逻辑运算符
3. 掌握for循环和while循环
4. 理解break和continue的用法
5. 学会嵌套结构的使用
"""

# ==========================================
# 1. 条件判断 - if语句
# ==========================================
print("=== 第1部分：条件判断 (if语句) ===")
print()

# 最简单的if语句
age = 18
if age >= 18:
    print("你已经成年了！")

print()

# if-else语句
weather = "晴天"
if weather == "下雨":
    print("记得带伞！")
else:
    print("天气不错，可以出门！")

print()

# if-elif-else语句
score = 85
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"你的分数是{score}，等级是：{grade}")
print()

# ==========================================
# 2. 比较运算符
# ==========================================
print("=== 第2部分：比较运算符 ===")
print()

a = 10
b = 20

print(f"a = {a}, b = {b}")
print(f"a == b (等于): {a == b}")
print(f"a != b (不等于): {a != b}")
print(f"a < b (小于): {a < b}")
print(f"a > b (大于): {a > b}")
print(f"a <= b (小于等于): {a <= b}")
print(f"a >= b (大于等于): {a >= b}")
print()

# 字符串比较
name1 = "张三"
name2 = "李四"
print(f"'{name1}' == '{name2}': {name1 == name2}")
print(f"'{name1}' != '{name2}': {name1 != name2}")
print()

# ==========================================
# 3. 逻辑运算符
# ==========================================
print("=== 第3部分：逻辑运算符 ===")
print()

# and 运算符 - 两个条件都为真时结果才为真
age = 20
has_license = True

if age >= 18 and has_license:
    print("可以开车")
else:
    print("不能开车")

# or 运算符 - 任一条件为真时结果就为真
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("今天可以休息")
else:
    print("今天需要工作")

# not 运算符 - 取反
is_raining = False
if not is_raining:
    print("没有下雨，可以出门")

print()

# 复杂的逻辑表达式
temperature = 25
humidity = 60

if temperature > 20 and temperature < 30 and humidity < 70:
    print("天气很舒适")
else:
    print("天气不太舒适")

print()

# ==========================================
# 4. for循环
# ==========================================
print("=== 第4部分：for循环 ===")
print()

# 遍历数字范围
print("数字1到5：")
for i in range(1, 6):
    print(f"数字：{i}")

print()

# 遍历字符串
name = "Python"
print(f"'{name}'中的每个字符：")
for char in name:
    print(f"字符：{char}")

print()

# 遍历列表
fruits = ["苹果", "香蕉", "橘子", "葡萄"]
print("水果列表：")
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

print()

# 使用enumerate获取索引
print("带索引的水果列表：")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

print()

# range的不同用法
print("range的用法示例：")
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

print("range(2, 8):", end=" ")
for i in range(2, 8):
    print(i, end=" ")
print()

print("range(0, 10, 2):", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")
print()
print()

# ==========================================
# 5. while循环
# ==========================================
print("=== 第5部分：while循环 ===")
print()

# 基本while循环
print("倒计时：")
count = 5
while count > 0:
    print(f"{count}...")
    count -= 1
print("发射！🚀")
print()

# 用户输入模拟（使用固定值演示）
print("猜数字游戏模拟：")
secret_number = 7
guess = 0
attempts = 0

# 模拟几次猜测
guesses = [3, 9, 7]  # 预设的猜测值
for guess in guesses:
    attempts += 1
    print(f"第{attempts}次猜测：{guess}")
    
    if guess == secret_number:
        print(f"恭喜！你在{attempts}次内猜对了！")
        break
    elif guess < secret_number:
        print("太小了！")
    else:
        print("太大了！")

print()

# 计算累加
print("计算1到10的和：")
total = 0
num = 1
while num <= 10:
    total += num
    print(f"当前数字：{num}，累计和：{total}")
    num += 1
print(f"最终结果：{total}")
print()

# ==========================================
# 6. break和continue
# ==========================================
print("=== 第6部分：break和continue ===")
print()

# break - 跳出循环
print("使用break跳出循环：")
for i in range(1, 10):
    if i == 5:
        print(f"遇到{i}，跳出循环")
        break
    print(f"数字：{i}")

print()

# continue - 跳过当前循环，继续下一次
print("使用continue跳过偶数：")
for i in range(1, 10):
    if i % 2 == 0:  # 如果是偶数
        continue    # 跳过这次循环
    print(f"奇数：{i}")

print()

# 在while循环中使用break和continue
print("处理数字列表（跳过负数，遇到0停止）：")
numbers = [1, 3, -2, 4, -5, 0, 6, 7]
i = 0
while i < len(numbers):
    num = numbers[i]
    
    if num == 0:
        print("遇到0，停止处理")
        break
    
    if num < 0:
        print(f"跳过负数：{num}")
        i += 1
        continue
    
    print(f"处理正数：{num}")
    i += 1

print()

# ==========================================
# 7. 嵌套结构
# ==========================================
print("=== 第7部分：嵌套结构 ===")
print()

# 嵌套if语句
print("成绩等级判定（考虑出勤率）：")
score = 88
attendance = 95  # 出勤率

if score >= 60:
    if attendance >= 80:
        if score >= 90:
            final_grade = "优秀"
        elif score >= 80:
            final_grade = "良好"
        else:
            final_grade = "及格"
    else:
        final_grade = "出勤不足，降级"
else:
    final_grade = "不及格"

print(f"分数：{score}，出勤率：{attendance}%，最终等级：{final_grade}")
print()

# 嵌套循环 - 打印乘法表
print("九九乘法表：")
for i in range(1, 10):
    for j in range(1, i + 1):
        result = i * j
        print(f"{j}×{i}={result:2d}", end="  ")
    print()  # 换行

print()

# 嵌套循环 - 图案打印
print("星号图案：")
for row in range(1, 6):
    # 打印空格
    for space in range(5 - row):
        print(" ", end="")
    # 打印星号
    for star in range(row):
        print("* ", end="")
    print()  # 换行

print()

# ==========================================
# 8. 实践练习
# ==========================================
print("=== 第8部分：实践练习 ===")
print()

# 练习1：判断数字性质
print("练习1：判断数字性质")
numbers_to_check = [12, 7, 0, -5, 15]

for num in numbers_to_check:
    print(f"\n数字 {num}：")
    
    # 判断正负零
    if num > 0:
        print("- 是正数")
    elif num < 0:
        print("- 是负数")
    else:
        print("- 是零")
    
    # 判断奇偶（零除外）
    if num != 0:
        if num % 2 == 0:
            print("- 是偶数")
        else:
            print("- 是奇数")

print()

# 练习2：查找特殊数字
print("练习2：在列表中查找第一个能被3整除的数字")
numbers = [7, 14, 21, 8, 12, 31]

found = False
for num in numbers:
    if num % 3 == 0:
        print(f"找到第一个能被3整除的数字：{num}")
        found = True
        break

if not found:
    print("没有找到能被3整除的数字")

print()

# 练习3：统计字符
print("练习3：统计字符串中的字符类型")
text = "Hello123World!"
letters = 0
digits = 0
others = 0

for char in text:
    if char.isalpha():  # 是字母
        letters += 1
    elif char.isdigit():  # 是数字
        digits += 1
    else:  # 其他字符
        others += 1

print(f"文本：'{text}'")
print(f"字母数量：{letters}")
print(f"数字数量：{digits}")
print(f"其他字符数量：{others}")

print()

# ==========================================
# 9. 常见模式和技巧
# ==========================================
print("=== 第9部分：常见模式和技巧 ===")
print()

# 模式1：计数器
print("计数器模式 - 统计偶数个数：")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1

print(f"列表中偶数的个数：{even_count}")
print()

# 模式2：累加器
print("累加器模式 - 计算平方和：")
square_sum = 0
for i in range(1, 6):
    square = i * i
    square_sum += square
    print(f"{i}² = {square}，累计和：{square_sum}")

print()

# 模式3：标志变量
print("标志变量模式 - 检查是否包含特定元素：")
fruits = ["苹果", "香蕉", "橘子"]
target = "香蕉"
found = False

for fruit in fruits:
    if fruit == target:
        found = True
        break

if found:
    print(f"找到了{target}")
else:
    print(f"没有找到{target}")

print()

# 模式4：最值查找
print("最值查找模式 - 找最大值：")
numbers = [23, 56, 12, 89, 34]
max_num = numbers[0]  # 假设第一个是最大值

for num in numbers:
    if num > max_num:
        max_num = num

print(f"列表 {numbers} 中的最大值是：{max_num}")
print()

# ==========================================
# 10. 小结
# ==========================================
print("=== 学习小结 ===")
print("""
恭喜你完成了第二课的学习！

你学到了：
✓ 条件判断（if-elif-else）让程序能做决定
✓ 比较运算符（==, !=, <, >, <=, >=）用于比较值
✓ 逻辑运算符（and, or, not）用于组合条件
✓ for循环用于遍历序列和重复执行
✓ while循环用于条件控制的重复执行
✓ break和continue用于控制循环流程
✓ 嵌套结构用于处理复杂逻辑
✓ 常见的编程模式和技巧

下一课预告：
我们将学习函数，让你能够组织代码、
避免重复，并创建可重用的代码块！

继续加油！🚀
""")

# ==========================================
# 作业
# ==========================================
print("=== 课后作业 ===")
print("""
请完成以下作业：

1. 编写程序判断一个年份是否为闰年
   （能被4整除但不能被100整除，或者能被400整除）

2. 使用循环打印1-20中所有的质数

3. 编写程序模拟简单的计算器
   （输入两个数字和运算符，输出结果）

4. 使用嵌套循环绘制一个5×5的星号正方形

5. 编写程序找出1-100中所有的完全数
   （完全数等于其所有真因数的和，如6=1+2+3）

提示：可以修改这个文件来完成作业，或者创建新文件！
""")