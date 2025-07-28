#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单项目：个人信息卡片生成器
==========================

这是一个简单的Python项目，用于创建个人信息卡片。
这个项目帮助你练习第1课学到的变量和数据类型。

项目目标：
- 收集个人基本信息
- 进行简单的计算
- 生成格式化的信息卡片
"""

print("🎫 个人信息卡片生成器")
print("=" * 40)

# ==========================================
# 1. 收集个人信息
# ==========================================

# 基本信息
name = "李小明"              # 请修改为你的姓名
age = 22                    # 请修改为你的年龄
birth_year = 2002           # 请修改为你的出生年份
height = 175.5              # 请修改为你的身高（厘米）
weight = 65.0               # 请修改为你的体重（公斤）
city = "北京"               # 请修改为你的城市
is_student = True           # 请修改：你是否是学生
hobby = "编程"              # 请修改为你的爱好

# ==========================================
# 2. 计算派生信息
# ==========================================

# 计算当前年份（假设是2024年）
current_year = 2024
calculated_age = current_year - birth_year

# 计算BMI（体重指数）
# BMI = 体重(kg) / (身高(m))²
height_in_meters = height / 100
bmi = weight / (height_in_meters * height_in_meters)

# 判断BMI范围
if bmi < 18.5:
    bmi_category = "偏瘦"
elif bmi < 24:
    bmi_category = "正常"
elif bmi < 28:
    bmi_category = "偏胖"
else:
    bmi_category = "肥胖"

# 计算理想体重（简化公式）
ideal_weight = (height - 100) * 0.9

# 学生状态文字
student_status = "学生" if is_student else "非学生"

# ==========================================
# 3. 生成信息卡片
# ==========================================

print("\n🎯 正在生成你的个人信息卡片...")
print()

# 打印漂亮的信息卡片
print("┌" + "─" * 38 + "┐")
print("│" + " " * 10 + "个人信息卡片" + " " * 16 + "│")
print("├" + "─" * 38 + "┤")
print(f"│ 姓名：{name:<20} │")
print(f"│ 年龄：{age}岁 (出生于{birth_year}年){' ' * (15 - len(str(age)) - len(str(birth_year)))}│")
print(f"│ 身高：{height}cm{' ' * (25 - len(str(height)))}│")
print(f"│ 体重：{weight}kg{' ' * (25 - len(str(weight)))}│")
print(f"│ 城市：{city:<20} │")
print(f"│ 状态：{student_status:<20} │")
print(f"│ 爱好：{hobby:<20} │")
print("├" + "─" * 38 + "┤")
print("│" + " " * 12 + "健康信息" + " " * 16 + "│")
print("├" + "─" * 38 + "┤")
print(f"│ BMI指数：{bmi:.1f} ({bmi_category}){' ' * (18 - len(str(bmi_category)))}│")
print(f"│ 理想体重：{ideal_weight:.1f}kg{' ' * (16 - len(str(int(ideal_weight))))}│")
print("└" + "─" * 38 + "┘")

# ==========================================
# 4. 额外统计信息
# ==========================================

print("\n📊 有趣的统计信息：")
print("-" * 30)

# 计算活了多少天（简化计算）
days_lived = calculated_age * 365
print(f"你大约活了 {days_lived:,} 天")

# 计算心跳次数（假设平均每分钟70次）
heartbeats = days_lived * 24 * 60 * 70
print(f"你的心脏大约跳动了 {heartbeats:,} 次")

# 计算睡眠时间（假设每天睡8小时）
sleep_hours = days_lived * 8
print(f"你大约睡了 {sleep_hours:,} 小时")

# 计算体重与身高比例
weight_height_ratio = weight / height * 100
print(f"体重身高比：{weight_height_ratio:.2f}")

print("\n" + "=" * 40)
print("🎉 信息卡片生成完成！")
print()
print("💡 项目扩展建议：")
print("1. 添加更多个人信息字段")
print("2. 实现用户输入功能")
print("3. 添加更多健康指标计算")
print("4. 美化输出格式")
print("5. 保存信息到文件")

# ==========================================
# 5. 项目总结
# ==========================================

print("\n📚 这个项目用到的知识点：")
print("✓ 变量定义和赋值")
print("✓ 不同数据类型的使用（int, float, str, bool）")
print("✓ 数学运算（加减乘除）")
print("✓ 字符串格式化（f-string）")
print("✓ 条件判断（if-elif-else）")
print("✓ 类型转换")
print("✓ 格式化输出")

print("\n🚀 恭喜你完成了第一个Python项目！")