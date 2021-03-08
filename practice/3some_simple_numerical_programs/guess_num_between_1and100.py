"""
@Author  : Lord_Bao
@Date    : 2021/3/8

"""
import random

"""
   随机生成1到100的数字,然后由用户输入数字进行猜测,根据用户猜测提醒是否大于随机生成的数字。
"""
# ######################## 手动猜测 ############################
# num = random.randint(1, 100)
# print("Welcome to Guess Number Between 1 and 100 Game!")
# guess = int(input("Please enter your number (between 1  and 100):"))
# guess_num = 1

#  # manually
# while guess != num:
#     guess_num += 1
#     if guess > num:
#         guess = int(input("Oops! your guess  " + str(guess) + " is HIGHER than the answer,try another one:"))
#     else:
#         guess = int(input("Oops! your guess  " + str(guess) + " is LOWER than the answer,try another one:"))
# print("Nice guess,you've guessed for " + str(guess_num) + " times")
# ######################## 手动猜测 ############################

# ######################## 分别用普通的方法(每次在原基础上+1或-1)和二分法猜测 ############################
# from 0  to 100 one by one
num = random.randint(1, 100)
print("Welcome to Guess Number Between 1 and 100 Game!")
print("Try UNUSUAL method!")
# temp用保存guess，方便采用二分法的时候再用
temp = guess = int(input("Please enter your number (between 1  and 100):"))
guess_num = 1

while guess != num:
    guess_num += 1
    if guess > num:

        print("Oops! your guess  " + str(guess) + " is HIGHER than the answer,try another one:" + str(guess - 1))
        guess -= 1
    else:

        print("Oops! your guess  " + str(guess) + " is LOWER than the answer,try another one:" + str(guess + 1))
        guess += 1

print("Nice guess,you've guessed " + str(num) + " for " + str(guess_num) + " times by unusual method ")

print("-------------")
print("Try BISEARCH method!")
# bisearch
guess = temp
guess_num = 1
begin = 0
end = 100
while guess != num:
    guess_num += 1
    if guess > num:
        end = guess - 1
        print(
            "Oops! your guess  " + str(guess) + " is HIGHER than the answer,try another one:" + str((begin + end) // 2))

    else:
        begin = guess + 1
        print(
            "Oops! your guess  " + str(guess) + " is LOWER than the answer,try another one:" + str((begin + end) // 2))
    guess = (begin + end) // 2

print("Nice guess,you've guessed " + str(num) + " for " + str(guess_num) + " times by bisearch method ")
