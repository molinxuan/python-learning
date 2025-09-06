#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python基础教程 - 第3课：函数
=========================

欢迎来到第三课！
这一课我们将学习如何使用函数来组织代码、复用逻辑和提高可读性。

学习目标：
1. 理解什么是函数、为何需要函数
2. 学会定义和调用函数（def、返回值、文档字符串）
3. 掌握参数：位置参数、关键字参数、默认参数、可变参数(*args, **kwargs)
4. 理解变量作用域：局部变量、全局变量、nonlocal
5. 了解匿名函数(lambda)、高阶函数(map/filter/reduce)、内置函数
6. 学会编写带类型注解和文档的函数
"""

# ==========================================
# 1. 为什么需要函数？
# ==========================================
print("=== 第1部分：为什么需要函数？ ===")
print()

# 没有函数的重复代码示例
print("没有函数时的重复代码示例：")
nums = [2, 5, 8]
double_1 = nums[0] * 2
double_2 = nums[1] * 2
double_3 = nums[2] * 2
print(double_1, double_2, double_3)

print("使用函数后：")
def double(x):
    """返回参数的两倍"""
    return x * 2

print(double(nums[0]), double(nums[1]), double(nums[2]))
print()

# ==========================================
# 2. 定义与调用函数
# ==========================================
print("=== 第2部分：定义与调用函数 ===")
print()

def greet(name: str) -> str:
    """返回一个问候消息。

    参数:
        name: 姓名
    返回:
        问候字符串
    """
    message = f"你好，{name}!"
    return message

result = greet("小明")
print(result)

def add(a: int, b: int) -> int:
    """返回两数之和"""
    return a + b

print(f"3 + 5 = {add(3, 5)}")
print()

# 返回多个值（本质是返回元组）
def divide_and_remainder(x: int, y: int):
    """返回商与余数"""
    q = x // y
    r = x % y
    return q, r

q, r = divide_and_remainder(17, 5)
print(f"17 ÷ 5 的商是 {q}，余数是 {r}")
print()

# ==========================================
# 3. 参数类型：位置、关键字、默认、可变
# ==========================================
print("=== 第3部分：函数参数 ===")
print()

# 位置参数与关键字参数
def describe_pet(animal_type: str, name: str) -> None:
    print(f"我有一只{animal_type}，它的名字叫{name}。")

describe_pet("小狗", "旺财")            # 位置参数
describe_pet(name="喵喵", animal_type="小猫")  # 关键字参数

# 默认参数
def power(base: float, exponent: float = 2) -> float:
    return base ** exponent

print(f"power(3) = {power(3)}")           # 默认平方
print(f"power(2, 3) = {power(2, 3)}")     # 立方

# 可变参数：*args（可变位置），**kwargs（可变关键字）
def sum_all(*numbers: float) -> float:
    total = 0
    for number in numbers:
        total += number
    return total

print(f"sum_all(1, 2, 3, 4) = {sum_all(1, 2, 3, 4)}")

def build_profile(name: str, **extra_info):
    profile = {"name": name}
    profile.update(extra_info)
    return profile

user_profile = build_profile("Alice", city="Shanghai", hobby="music")
print(f"用户资料：{user_profile}")
print()

# 位置仅参数、关键字仅参数（进阶语法，了解）
def area(width: float, /, height: float, *, unit: str = "cm^2") -> str:
    value = width * height
    return f"面积：{value} {unit}"

print(area(3, height=4, unit="m^2"))
print()

# ==========================================
# 4. 变量作用域：局部、全局、nonlocal
# ==========================================
print("=== 第4部分：变量作用域 ===")
print()

level = "global"

def scope_demo():
    level = "enclosing"

    def inner():
        nonlocal level
        print("进入 inner 前：", level)
        level = "modified by inner"
        print("离开 inner 后：", level)

    print("函数开始：", level)
    inner()
    print("函数结束：", level)

scope_demo()
print("函数外部：", level)

# global 示例
counter = 0

def increase():
    global counter
    counter += 1

increase()
increase()
print(f"全局计数器：{counter}")
print()

# ==========================================
# 5. 匿名函数与高阶函数
# ==========================================
print("=== 第5部分：匿名函数与高阶函数 ===")
print()

# 匿名函数（lambda）
square = lambda n: n * n
print(f"square(6) = {square(6)}")

# map / filter / reduce 示例
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"原始列表：{numbers}")
print(f"平方列表：{squares}")
print(f"偶数列表：{evens}")

try:
    from functools import reduce
    total = reduce(lambda acc, x: acc + x, numbers, 0)
    print(f"reduce 累加结果：{total}")
except Exception as e:
    print("reduce 示例运行失败：", e)

print()

# ==========================================
# 6. 文档字符串与类型注解
# ==========================================
print("=== 第6部分：文档与类型注解 ===")
print()

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """计算并返回 BMI 指数。

    公式：BMI = 体重(kg) / 身高(m)^2
    返回值保留两位小数。
    """
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

print(f"身高1.75m，体重68kg 的 BMI：{calculate_bmi(68, 1.75)}")
print()

# ==========================================
# 7. 常见错误与最佳实践
# ==========================================
print("=== 第7部分：常见错误与最佳实践 ===")
print()

# 1) 可变默认参数陷阱
def append_item(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items

print(append_item(1))
print(append_item(2))  # 不会和上一行共享列表

# 2) 函数要短小、职责单一；命名要动宾清晰
# 3) 使用类型注解和文档字符串提升可读性

print()

# ==========================================
# 8. 实践练习
# ==========================================
print("=== 第8部分：实践练习 ===")
print()
print("练习1：编写函数 is_even(n) 判断是否为偶数")
print("练习2：编写函数 factorial(n) 计算阶乘")
print("练习3：编写函数 find_max(*nums) 返回最大值")
print("练习4：编写函数 safe_divide(a, b) 对零做健壮处理")
print("练习5：编写函数 normalize_name(name) 规范化人名（去空格、首字母大写）")

print()

# ==========================================
# 9. 小结
# ==========================================
print("=== 学习小结 ===")
print("""
恭喜你完成了第三课的学习！

你学到了：
✓ 函数的作用与基本用法（定义、调用、返回值）
✓ 参数类型：位置、关键字、默认、*args 与 **kwargs
✓ 变量作用域：局部、全局、nonlocal
✓ 匿名函数与高阶函数(map/filter/reduce)
✓ 文档字符串与类型注解的最佳实践

下一课预告：
我们将学习常用数据结构（list、dict、tuple、set），
让你的数据组织更高效！

继续加油！🚀
""")

# ==========================================
# 作业
# ==========================================
print("=== 课后作业 ===")
print("""
请完成以下作业：

1. 实现并测试以下函数：
   - is_even(n) -> bool
   - factorial(n) -> int（非负整数，使用循环或递归）
   - find_max(*nums) -> number（任意个数参数）
   - safe_divide(a, b) -> float | None（b 为 0 时返回 None）
   - normalize_name(name) -> str（去掉前后空格，首字母大写，其他小写）

2. 为以上函数编写简要文档字符串和类型注解。

3. 选做：使用 map/filter/reduce 对列表进行以下操作：
   - 对 [1, 2, 3, 4, 5] 求平方
   - 过滤出偶数
   - 计算所有元素之和

提示：可以在 exercises/beginner/lesson03_exercises.py 中完成。
""")


