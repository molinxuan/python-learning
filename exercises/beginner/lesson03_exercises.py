#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习题 - 第3课：函数
===================

完成以下练习来巩固你对函数的理解与应用。
请在每个 TODO 标记处补全代码或修改变量。

提示：运行这个文件查看输出是否与预期一致！
"""

print("🎯 开始第3课练习题")
print("=" * 50)

# ==========================================
# 练习1：定义与调用
# ==========================================
print("\n📝 练习1：定义与调用")

# TODO: 定义一个函数 greet(name) -> str，返回 "你好，{name}!"
def greet(name: str) -> str:
    return f"你好，{name}!"

print(greet("小明"))  # 期望：你好，小明!


# ==========================================
# 练习2：返回多个值
# ==========================================
print("\n📝 练习2：返回多个值")

# TODO: 定义一个函数 divide_and_remainder(x, y)，返回(商, 余数)
def divide_and_remainder(x: int, y: int):
    q = x // y
    r = x % y
    return q, r

q, r = divide_and_remainder(20, 6)
print(f"20 ÷ 6 -> 商：{q}，余数：{r}")


# ==========================================
# 练习3：参数类型与默认参数
# ==========================================
print("\n📝 练习3：参数类型与默认参数")

# TODO: 定义 power(base, exponent=2) -> float，返回 base ** exponent
def power(base: float, exponent: float = 2) -> float:
    return base ** exponent

print(power(3))      # 期望：9
print(power(2, 3))   # 期望：8


# ==========================================
# 练习4：可变参数 *args 与 **kwargs
# ==========================================
print("\n📝 练习4：可变参数 *args 与 **kwargs")

# TODO: 定义 sum_all(*nums) -> float，返回所有参数的和
def sum_all(*nums: float) -> float:
    total = 0
    for n in nums:
        total += n
    return total

print(sum_all(1, 2, 3, 4))  # 期望：10

# TODO: 定义 build_profile(name, **extra) -> dict，返回合并信息
def build_profile(name: str, **extra) -> dict:
    profile = {"name": name}
    profile.update(extra)
    return profile

print(build_profile("Alice", city="Shanghai", hobby="music"))


# ==========================================
# 练习5：变量作用域
# ==========================================
print("\n📝 练习5：变量作用域")

counter = 0

# TODO: 编写 increase() 使用 global 修改 counter 使其自增1
def increase():
    global counter
    counter += 1

increase()
increase()
print(f"counter = {counter}")  # 期望：2


# ==========================================
# 练习6：匿名函数与高阶函数
# ==========================================
print("\n📝 练习6：匿名函数与高阶函数")

numbers = [1, 2, 3, 4, 5]

# TODO: 使用 map + lambda 生成平方列表
squares = list(map(lambda x: x * x, numbers))
print(f"平方：{squares}")  # 期望：[1, 4, 9, 16, 25]

# TODO: 使用 filter + lambda 筛选偶数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数：{evens}")    # 期望：[2, 4]

# TODO: 使用 reduce 计算累加和
from functools import reduce
total = reduce(lambda acc, x: acc + x, numbers, 0)
print(f"求和：{total}")     # 期望：15


# ==========================================
# 练习7：实现小型工具函数
# ==========================================
print("\n📝 练习7：实现小型工具函数")

# TODO: 实现 is_even(n) -> bool 判断偶数
def is_even(n: int) -> bool:
    return n % 2 == 0

# TODO: 实现 factorial(n) -> int 计算阶乘（非负整数）
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n 必须是非负整数")
    result = 1
    for i in range(1, n + 1):
        result += 0  # 故意占位，下一行替换
        result = result * i
    return result

# TODO: 实现 find_max(*nums) 返回最大值（至少一个数）
def find_max(*nums):
    if not nums:
        raise ValueError("至少提供一个数字")
    m = nums[0]
    for x in nums[1:]:
        if x > m:
            m = x
    return m

# TODO: 实现 safe_divide(a, b) -> float | None，b 为0时返回 None
def safe_divide(a: float, b: float):
    if b == 0:
        return None
    return a / b

# TODO: 实现 normalize_name(name) -> str 去前后空格，首字母大写，其他小写
def normalize_name(name: str) -> str:
    name = name.strip()
    if not name:
        return ""
    return name[0].upper() + name[1:].lower()

print(is_even(4), is_even(5))               # 期望：True False
print(factorial(5))                          # 期望：120
print(find_max(3, 9, 2, 7))                 # 期望：9
print(safe_divide(10, 2), safe_divide(10, 0))  # 期望：5.0 None
print(normalize_name("  aLICE  "))            # 期望：Alice


# ==========================================
# 挑战题（可选）
# ==========================================
print("\n🏆 挑战题（可选）")

# TODO: 编写一个高阶函数 make_multiplier(factor) -> function
# 返回一个新函数 new(x) 使得 new(x) = x * factor
def make_multiplier(factor: float):
    def new(x: float) -> float:
        return x * factor
    return new

times3 = make_multiplier(3)
print(times3(10))  # 期望：30


# ==========================================
# 练习完成
# ==========================================
print("\n" + "=" * 50)
print("🎉 恭喜你完成了第3课的所有练习！")
print()
print("检查清单：")
print("✓ 会定义、调用函数并返回多个值")
print("✓ 掌握参数、默认参数与可变参数")
print("✓ 理解作用域与全局变量用法")
print("✓ 能使用 lambda、map、filter、reduce")
print("✓ 完成多个实用小函数的实现")
print()
print("下一步：继续学习第4课 - 数据结构！")
print("💪 Keep coding!")


