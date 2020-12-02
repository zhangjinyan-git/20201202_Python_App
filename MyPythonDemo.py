# import random
#
# number = random.randint(0, 100)
# guess = 0
# print("来玩猜数字游戏啦！")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#     if guess == number:
#         print("恭喜你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")


# a = '123'
# print(id(a))
#
# a = 'a'
# print(id(a))


# # 可写函数说明
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
#
#
# # 调用printinfo函数
# printinfo(age=50, name="runoob")
# print("------------------------")
# printinfo("runoob")


# 可写函数说明
# def printinfo(arg1, **vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1 + vartuple)
#     print(vartuple)
#
#
# # 调用printinfo 函数
# printinfo(70, a = 60, b = 50)


# tup1 = ('Google', 'Runoob', 1997, 2000)
# tup1[0] = 'a'
#
# print(tup1)


# list = [1, 2, 3, "a", "b"]
# list[0] = 0
# list.append("c")
# print(list)
#
#
# dict = {}
# dict

# def f(a,b,*,c):
#     print(a + b + c)
#
# f(1, 2, c = 3)

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = ['Google', 'Runoob', "abc", "2000", "100"]
# list1.extend(list2)
# print(list2.pop(1))
list2.sort()
print(list2)