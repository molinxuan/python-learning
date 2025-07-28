#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python基础教程 - 第1课：变量和数据类型
=================================

欢迎开始你的Python学习之旅！
这一课我们将学习Python中的变量和基本数据类型。

学习目标：
1. 理解什么是变量
2. 掌握Python的基本数据类型
3. 学会变量的定义和使用
4. 了解类型转换
"""

# ==========================================
# 1. 什么是变量？
# ==========================================
print("=== 第1部分：什么是变量？ ===")
print()

# 变量就像一个容器，用来存储数据
# 在Python中，你不需要声明变量的类型，直接赋值即可

# 创建第一个变量
name = "张三"
print(f"我的名字是：{name}")

age = 25
print(f"我的年龄是：{age}")

print()

# ==========================================
# 2. Python的基本数据类型
# ==========================================
print("=== 第2部分：基本数据类型 ===")
print()

# 2.1 整数 (int)
my_age = 25
year = 2024
negative_num = -10

print(f"整数示例：{my_age}, {year}, {negative_num}")
print(f"my_age的类型是：{type(my_age)}")
print()

# 2.2 浮点数 (float)
height = 175.5
temperature = -3.2
pi = 3.14159

print(f"浮点数示例：{height}, {temperature}, {pi}")
print(f"height的类型是：{type(height)}")
print()

# 2.3 字符串 (str)
first_name = "李"
last_name = "明"
full_name = first_name + last_name  # 字符串拼接
message = "Hello, World!"

print(f"字符串示例：{first_name}, {last_name}, {full_name}")
print(f"消息：{message}")
print(f"message的类型是：{type(message)}")
print()

# 2.4 布尔值 (bool)
is_student = True
is_working = False

print(f"布尔值示例：{is_student}, {is_working}")
print(f"is_student的类型是：{type(is_student)}")
print()

# ==========================================
# 3. 变量命名规则
# ==========================================
print("=== 第3部分：变量命名规则 ===")
print()

# 正确的变量名示例
user_name = "王五"          # 推荐：使用下划线
userName = "赵六"           # 可以：驼峰命名
age2 = 30                  # 可以：包含数字（但不能以数字开头）
_private_var = "私有变量"   # 可以：以下划线开头

print(f"正确的变量名示例：")
print(f"user_name = {user_name}")
print(f"userName = {userName}")
print(f"age2 = {age2}")
print(f"_private_var = {_private_var}")
print()

# 注意：以下是错误的变量名（已注释，因为会导致错误）
# 2age = 30        # 错误：不能以数字开头
# my-name = "test" # 错误：不能包含连字符
# class = "test"   # 错误：不能使用Python关键字

# ==========================================
# 4. 类型转换
# ==========================================
print("=== 第4部分：类型转换 ===")
print()

# 字符串转数字
str_number = "123"
int_number = int(str_number)
float_number = float(str_number)

print(f"字符串 '{str_number}' 转换为整数：{int_number}")
print(f"字符串 '{str_number}' 转换为浮点数：{float_number}")
print()

# 数字转字符串
my_num = 456
str_from_int = str(my_num)

print(f"整数 {my_num} 转换为字符串：'{str_from_int}'")
print()

# 其他类型转换
bool_from_int = bool(1)    # 非0数字转为True
bool_from_zero = bool(0)   # 0转为False
int_from_bool = int(True)  # True转为1

print(f"数字1转布尔值：{bool_from_int}")
print(f"数字0转布尔值：{bool_from_zero}")
print(f"True转整数：{int_from_bool}")
print()

# ==========================================
# 5. 实践练习
# ==========================================
print("=== 第5部分：动手练习 ===")
print()

# 练习1：创建个人信息变量
print("练习1：创建你的个人信息")
student_name = "小明"  # 请改为你的名字
student_age = 20       # 请改为你的年龄
student_height = 170.0 # 请改为你的身高
is_male = True         # 请改为你的性别（True表示男性，False表示女性）

print(f"姓名：{student_name}")
print(f"年龄：{student_age}")
print(f"身高：{student_height}cm")
print(f"性别：{'男' if is_male else '女'}")
print()

# 练习2：计算和类型转换
print("练习2：简单计算")
num1 = 10
num2 = 3

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2  # 结果是浮点数

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print()

# ==========================================
# 6. 小结
# ==========================================
print("=== 学习小结 ===")
print("""
恭喜你完成了第一课的学习！

你学到了：
✓ 什么是变量，如何创建和使用变量
✓ Python的四种基本数据类型：int, float, str, bool
✓ 变量命名的规则和最佳实践
✓ 如何进行类型转换
✓ 简单的数学运算

下一课预告：
我们将学习控制流语句（if-else, for, while），
让你的程序能够做出判断和循环执行任务！

继续加油！🚀
""")

# ==========================================
# 作业
# ==========================================
print("=== 课后作业 ===")
print("""
请完成以下作业：

1. 创建变量存储你最喜欢的电影名称、上映年份和评分
2. 计算你出生到现在经过了多少天（假设一年365天）
3. 创建两个字符串变量，练习字符串拼接
4. 尝试不同的类型转换，观察结果

提示：可以修改这个文件中的练习部分来完成作业！
""")