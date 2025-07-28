#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习题 - 第1课：变量和数据类型
=============================

完成以下练习来巩固你对变量和数据类型的理解。
请在每个TODO标记处填写你的答案。

提示：运行这个文件查看你的答案是否正确！
"""

print("🎯 开始第1课练习题")
print("=" * 50)

# ==========================================
# 练习1：创建基本变量
# ==========================================
print("\n📝 练习1：创建基本变量")

# TODO: 创建以下变量
# 1. 创建一个名为 my_name 的变量，存储你的姓名
my_name = "请在这里填写你的姓名"

# 2. 创建一个名为 my_age 的变量，存储你的年龄
my_age = 0  # 请修改这个值

# 3. 创建一个名为 my_city 的变量，存储你所在的城市
my_city = "请填写你的城市"

# 4. 创建一个名为 is_student 的变量，表示你是否是学生（True或False）
is_student = True  # 请修改这个值

# 检查你的答案
print(f"我的姓名：{my_name}")
print(f"我的年龄：{my_age}")
print(f"我的城市：{my_city}")
print(f"是学生：{is_student}")

# ==========================================
# 练习2：数据类型识别
# ==========================================
print("\n📝 练习2：数据类型识别")

# 给定一些变量，请说出它们的数据类型
var1 = 42
var2 = 3.14
var3 = "Hello"
var4 = True
var5 = "123"

# TODO: 使用type()函数打印每个变量的类型
print(f"var1 = {var1}, 类型是：{type(var1)}")
# 请仿照上面的格式，打印其他变量的类型
print(f"var2 = {var2}, 类型是：{type(var2)}")
print(f"var3 = {var3}, 类型是：{type(var3)}")
print(f"var4 = {var4}, 类型是：{type(var4)}")
print(f"var5 = {var5}, 类型是：{type(var5)}")

# ==========================================
# 练习3：类型转换
# ==========================================
print("\n📝 练习3：类型转换")

# TODO: 完成以下类型转换
str_num = "456" 
# 1. 将 str_num 转换为整数，存储在 int_result 中
int_result = int(str_num)

# 2. 将 int_result 转换为浮点数，存储在 float_result 中
float_result = float(int_result)

# 3. 将数字 0 转换为布尔值，存储在 bool_result 中
bool_result = bool(0)

# 4. 将布尔值 True 转换为字符串，存储在 str_result 中
str_result = str(True)

print(f"'{str_num}' 转为整数：{int_result}")
print(f"{int_result} 转为浮点数：{float_result}")
print(f"0 转为布尔值：{bool_result}")
print(f"True 转为字符串：'{str_result}'")

# ==========================================
# 练习4：字符串操作
# ==========================================
print("\n📝 练习4：字符串操作")

first_name = "张"
last_name = "伟"

# TODO: 完成以下字符串操作
# 1. 将 first_name 和 last_name 拼接成完整姓名
full_name = first_name + last_name

# 2. 创建一个问候消息，格式为："你好，[姓名]！"
greeting = f"你好，{full_name}！"

# 3. 创建一个包含你年龄的消息，格式为："我今年[年龄]岁了。"
age_message = f"我今年{my_age}岁了。"

print(f"完整姓名：{full_name}")
print(f"问候消息：{greeting}")
print(f"年龄消息：{age_message}")

# ==========================================
# 练习5：数学运算
# ==========================================
print("\n📝 练习5：数学运算")

# TODO: 使用以下两个数字完成计算
num_a = 15
num_b = 4

# 1. 加法
addition = num_a + num_b

# 2. 减法
subtraction = num_a - num_b

# 3. 乘法
multiplication = num_a * num_b

# 4. 除法（结果为浮点数）
division = num_a / num_b

# 5. 整数除法（结果为整数）
floor_division = num_a // num_b

# 6. 取余数
remainder = num_a % num_b

print(f"{num_a} + {num_b} = {addition}")
print(f"{num_a} - {num_b} = {subtraction}")
print(f"{num_a} * {num_b} = {multiplication}")
print(f"{num_a} / {num_b} = {division}")
print(f"{num_a} // {num_b} = {floor_division}")
print(f"{num_a} % {num_b} = {remainder}")

# ==========================================
# 练习6：实际应用
# ==========================================
print("\n📝 练习6：实际应用")

# 假设你要买以下物品：
apple_price = 3.5      # 苹果每斤价格
apple_weight = 2       # 买2斤苹果

banana_price = 4.2     # 香蕉每斤价格
banana_weight = 1.5    # 买1.5斤香蕉

# TODO: 计算总费用
apple_total = apple_price * apple_weight
banana_total = banana_price * banana_weight
total_cost = apple_total + banana_total

print(f"苹果费用：{apple_weight}斤 × {apple_price}元/斤 = {apple_total}元")
print(f"香蕉费用：{banana_weight}斤 × {banana_price}元/斤 = {banana_total}元")
print(f"总费用：{total_cost}元")

# ==========================================
# 挑战题（可选）
# ==========================================
print("\n🏆 挑战题（可选）")

# 计算你活了多少天
# TODO: 填写你的出生年份
birth_year = 2000  # 请修改为你的出生年份

current_year = 2024
years_lived = current_year - birth_year
days_lived = years_lived * 365  # 简化计算，不考虑闰年

print(f"从{birth_year}年到{current_year}年，你大约活了{days_lived}天")

# 温度转换：摄氏度转华氏度
# 公式：华氏度 = 摄氏度 × 9/5 + 32
celsius = 25  # 摄氏度
fahrenheit = celsius * 9/5 + 32

print(f"{celsius}°C = {fahrenheit}°F")

# ==========================================
# 练习完成
# ==========================================
print("\n" + "=" * 50)
print("🎉 恭喜你完成了第1课的所有练习！")
print()
print("检查清单：")
print("✓ 创建了不同类型的变量")
print("✓ 学会了识别数据类型")
print("✓ 掌握了类型转换")
print("✓ 练习了字符串操作")
print("✓ 完成了数学运算")
print("✓ 解决了实际问题")
print()
print("下一步：继续学习第2课 - 控制流语句！")
print("💪 Keep coding!")