#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单项目：智能猜数字游戏
====================

这是一个综合运用第2课知识的项目，包含：
- 条件判断
- 循环控制
- 用户交互
- 游戏逻辑

项目功能：
1. 计算机随机生成一个1-100的数字
2. 玩家有限次机会猜测
3. 提供智能提示
4. 记录游戏统计信息
5. 支持多轮游戏
"""

import random

print("🎮 智能猜数字游戏")
print("=" * 40)
print("欢迎来到猜数字游戏！")
print("我会想一个1到100之间的数字，你来猜猜看！")
print()

# 游戏统计
total_games = 0
total_guesses = 0
best_score = float('inf')  # 最少猜测次数
games_won = 0

# 游戏主循环
while True:
    total_games += 1
    print(f"🎯 第 {total_games} 轮游戏开始！")
    print("-" * 30)
    
    # 生成随机数
    secret_number = random.randint(1, 100)
    max_attempts = 7  # 最大尝试次数
    attempts = 0
    guessed_numbers = []  # 记录已猜测的数字
    
    print(f"我已经想好了一个1到100之间的数字")
    print(f"你有 {max_attempts} 次机会来猜测")
    print()
    
    # 猜测循环
    game_won = False
    while attempts < max_attempts:
        attempts += 1
        total_guesses += 1
        
        # 获取用户输入（在实际使用中取消注释下面这行）
        # guess = int(input(f"第 {attempts} 次猜测，请输入你的猜测（1-100）："))
        
        # 演示用：模拟用户输入
        if attempts == 1:
            guess = random.randint(1, 100)
        elif attempts == 2:
            if secret_number > 50:
                guess = random.randint(51, 100)
            else:
                guess = random.randint(1, 50)
        else:
            # 智能猜测演示
            if len(guessed_numbers) >= 2:
                last_guess = guessed_numbers[-1]
                if last_guess < secret_number:
                    guess = random.randint(last_guess + 1, 100)
                else:
                    guess = random.randint(1, last_guess - 1)
            else:
                guess = random.randint(1, 100)
        
        print(f"第 {attempts} 次猜测：{guess}")
        
        # 检查是否已经猜过这个数字
        if guess in guessed_numbers:
            print("⚠️  你已经猜过这个数字了！")
            continue
        
        guessed_numbers.append(guess)
        
        # 判断猜测结果
        if guess == secret_number:
            print("🎉 恭喜你！猜对了！")
            print(f"答案确实是 {secret_number}")
            print(f"你用了 {attempts} 次就猜中了！")
            
            # 更新统计信息
            game_won = True
            games_won += 1
            if attempts < best_score:
                best_score = attempts
                print(f"🏆 新纪录！这是你目前最少的猜测次数！")
            
            break
        elif guess < secret_number:
            print("📈 太小了！答案比这个大")
        else:
            print("📉 太大了！答案比这个小")
        
        # 提供智能提示
        difference = abs(guess - secret_number)
        if difference <= 5:
            print("🔥 非常接近了！")
        elif difference <= 10:
            print("🌡️  比较接近")
        elif difference <= 20:
            print("🌊 还有些距离")
        else:
            print("❄️  还很远呢")
        
        # 显示剩余机会
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"还剩 {remaining} 次机会")
            
            # 给出范围提示
            if len(guessed_numbers) >= 2:
                min_guess = min([g for g in guessed_numbers if g < secret_number], default=1)
                max_guess = max([g for g in guessed_numbers if g > secret_number], default=100)
                if min_guess < secret_number < max_guess:
                    print(f"💡 提示：答案在 {min_guess} 和 {max_guess} 之间")
        
        print()
    
    # 游戏结束
    if not game_won:
        print("😅 很遗憾，机会用完了！")
        print(f"答案是 {secret_number}")
        print("不过没关系，多练习就会进步的！")
    
    print()
    print("📊 本轮游戏统计：")
    print(f"   猜测次数：{attempts}")
    print(f"   猜测的数字：{guessed_numbers}")
    print(f"   游戏结果：{'胜利' if game_won else '失败'}")
    
    # 显示总体统计
    print("\n📈 总体统计：")
    print(f"   总游戏次数：{total_games}")
    print(f"   获胜次数：{games_won}")
    print(f"   胜率：{games_won/total_games*100:.1f}%")
    print(f"   总猜测次数：{total_guesses}")
    print(f"   平均每轮猜测次数：{total_guesses/total_games:.1f}")
    if best_score != float('inf'):
        print(f"   最佳成绩：{best_score} 次")
    
    # 询问是否继续游戏
    print()
    print("是否继续游戏？")
    print("1. 继续游戏")
    print("2. 查看游戏技巧")
    print("3. 退出游戏")
    
    # 演示用：随机选择
    choice = random.choice([1, 1, 1, 2, 3])  # 大概率继续游戏
    print(f"选择：{choice}")
    
    if choice == 1:
        print("\n" + "="*40)
        continue
    elif choice == 2:
        print("\n🎯 猜数字游戏技巧：")
        print("1. 使用二分法：从50开始猜，根据大小调整范围")
        print("2. 记住已经猜过的数字，避免重复")
        print("3. 注意提示信息，缩小猜测范围")
        print("4. 保持冷静，不要被连续错误影响判断")
        print("5. 利用概率：在剩余范围内选择中间值")
        print()
        
        # 演示二分法
        print("🔍 二分法演示：")
        demo_target = 73
        low, high = 1, 100
        demo_attempts = 0
        
        print(f"假设答案是 {demo_target}")
        while low <= high:
            demo_attempts += 1
            mid = (low + high) // 2
            print(f"第{demo_attempts}次：猜测 {mid}", end="")
            
            if mid == demo_target:
                print(" - 正确！")
                break
            elif mid < demo_target:
                print(f" - 太小，调整范围为 {mid+1}-{high}")
                low = mid + 1
            else:
                print(f" - 太大，调整范围为 {low}-{mid-1}")
                high = mid - 1
        
        print(f"二分法只需要 {demo_attempts} 次就能猜中！")
        print()
        continue
    else:
        break

print("👋 感谢游戏！")
print("\n🎓 这个项目用到的第2课知识点：")
print("✓ if-elif-else 条件判断")
print("✓ while 循环控制游戏流程")
print("✓ for 循环处理列表数据")
print("✓ break 和 continue 控制循环")
print("✓ 逻辑运算符组合复杂条件")
print("✓ 嵌套结构处理复杂逻辑")

print("\n💡 项目扩展建议：")
print("1. 添加难度选择（调整数字范围和尝试次数）")
print("2. 实现真实的用户输入功能")
print("3. 添加排行榜系统")
print("4. 支持多人游戏模式")
print("5. 添加图形界面")
print("6. 实现智能AI对战模式")

print("\n🚀 恭喜你完成了第二个Python项目！")