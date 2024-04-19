# # 1.猜数字小游戏
# # 导入随机数模块
# import random
#
# # 设置随机生成数
# num = random.randint(0, 100)
# # 设置10次机会
# choice = 10
# print('欢迎来到猜数字小游戏，你一共有10次机会')
# # 用户需要输入猜测的数字
# for i in range(choice):
#     guess = int(input('请输入你要猜测的数字'))
#     if guess < num:
#         print('恭喜你猜小了')
#     elif guess > num:
#         print('恭喜你猜大了')
#     else:
#         print('恭喜你猜对了,游戏结束')
#         break
# else:
#     print(f'恭喜你猜错了,答案是{num},游戏结束,下次继续努力')


# '''2.剪刀石头布'''
# import random
#
#
# def play_game():
#     user_score = 100
#     computer_score = 100
#
#     while True:
#         user_choice = int(input('请出：1-剪刀，2-石头，3-布'))
#         computer_chice = random.randint(1, 3)
#
#         if user_choice not in [1, 2, 3]:
#             print('恭喜你输入错误，请重新输入')
#             continue
#         print('-' * 20)
#         print(f'你出的是{user_choice},电脑出的是{computer_chice}')
#
#         if user_choice == computer_chice:
#             print('恭喜平局，用一点点智慧')
#         elif (user_choice == 1 and computer_chice == 3) or (user_choice == 2 and computer_chice == 1) or (
#                 user_choice == 3 and computer_chice == 2):
#             print('恭喜你赢了')
#             user_score += 10
#             computer_score -= 10
#         else:
#             print('恭喜你输了')
#             user_score -= 10
#             computer_score += 10
#         print('-' * 20)
#         print(f'你的分数是{user_score},电脑的分数是{computer_score}')
#
#         if user_score <= 0:
#             print('你输了,你真棒')
#             break
#         elif computer_score <= 0:
#             print('电脑输了，你很棒')
#             break
#
#
# play_game()


# 3封装函数: 判断一个数组是对称数组 用 Python 判断，是对称数组打印 True，不是打印 False。函数说明文档也要写？
# arr1 = [1, 2, 3, 3, 2, 1]
#
#
# def is_integer(arr):
#     n = len(arr)
#     for i in range(n // 2):  # 遍历数组的一半长度
#         if arr[i] != arr[n - i - 1]:  # 检测对称位置的字符是否相等
#             return False
#     return True
#
#
# print(is_integer(arr1))
#
# # 4找出列表 a = [“hello”, “world”, “yoyo”, “congratulations”] 中单词最长的一个
# a = ['hello', 'world', 'yoyo', 'congratulations']
# longstr = max(a, key=len)
# print(longstr)
