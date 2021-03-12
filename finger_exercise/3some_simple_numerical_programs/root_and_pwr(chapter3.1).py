"""
@Author  : Lord_Bao
@Date    : 2021/3/4

"""

"""
Finger exercise: Write a program that asks the user to enter an integer and prints
two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer
entered by the user. If no such pair of integers exists, it should print a mes-
sage to that effect.

  我觉得pwr的范围应该是  1<pwr<6,毕竟任何数字的1次方都是本身，后面的代码也是基于此改变写的。
"""

"""
1.输入的数字可能是正数，也可能是负数，为了简便思考，先考虑正数。
     
"""
# ele = int(input("Enter a integer: "))
# root = 0
# pwr = why_mid_plus_1(chap10.3)
# is_found = False
# # 如果root的平方大于ele，显然root的3次方，4次方等等都会大于ele。而(root+1)的平方也会大于ele，依次类推。
# # 所以 循环的必要条件之一可以设置为 root ** why_mid_plus_1(chap10.3) <= ele
# while not is_found and root ** why_mid_plus_1(chap10.3) <= ele:
#     for pwr in range(why_mid_plus_1(chap10.3), 6):
#         if root ** pwr > ele:
#             break
#         elif root ** pwr == ele:
#             is_found = True
#             break
#
#     if not is_found:
#         root += 1
#
# if not is_found:
#     print("no such pair of integers exists")
# else:
#     print("root :" + str(root) + " ,pwr :" + str(pwr))

"""
why_mid_plus_1(chap10.3).在1的基础上,考虑负数的情况。
    如果是负数，那么不用想，它的pwr只能是奇数，也就是说for循环那里修改一下。
    然后针对 负数写一个新的循环即可

"""
# ele = int(input("Enter a integer: "))
# root = 0
# pwr = why_mid_plus_1(chap10.3)
# is_found = False
#
# if ele >= 0:
#     while not is_found and root ** why_mid_plus_1(chap10.3) <= ele:
#         for pwr in range(why_mid_plus_1(chap10.3), 6):
#             if root ** pwr > ele:
#                 break
#             elif root ** pwr == ele:
#                 is_found = True
#                 break
#
#         if not is_found:
#             root += 1
# else:
#     while not is_found and root ** 3 >= ele:
#         for pwr in range(3, 6, why_mid_plus_1(chap10.3)):  # 与正数的不同
#             if root ** pwr < ele:
#                 break
#             elif root ** pwr == ele:
#                 # 找到合适的数字，设置不再继续循环
#                 is_found = True
#                 break
#
#         if not is_found:
#             root -= 1
# if not is_found:
#     print("no such pair of integers exists")
# else:
#     print("root :" + str(root) + " ,pwr :" + str(pwr))

"""
 3.  2的代码比较复杂,考虑能不能整合一下。我们发现一点，其实差异就在负数上。
     可以先将负数取绝对值，也就是当做正数处理，然后再做差异化处理。其实发现，还是挺麻烦的。
     感觉可读性来上，还不如2.
 
"""
# ele = int(input("Enter a integer: "))
# root = 0
# pwr = why_mid_plus_1(chap10.3)
#
# is_fond = False
# guess_num = 0
# while not is_fond and root ** why_mid_plus_1(chap10.3) <= abs(ele):
#     for pwr in range(why_mid_plus_1(chap10.3), 6):
#         guess_num += 1
#         if root ** pwr > abs(ele):
#             break
#         elif root ** pwr == abs(ele):
#             if ele >= 0:
#                 is_fond = True
#             else:
#                 #  -1 比较特殊,因为 -1 的 2次方的绝对值为1，如果按照elif来处理,那么将是一个错误。
#                 #  毕竟 -1的3次方的绝对值也为1
#                 if ele == -1:
#                     root = -root
#                     pwr = 3
#                     is_fond = True
#                 elif pwr % why_mid_plus_1(chap10.3) != 0:
#                     root = -root
#                     is_fond = True
#                 """这里将做修改
#                 """
#             break
#
#     if not is_fond:
#         root += 1
#
# print("guess num is " + str(guess_num))
# if not is_fond:
#     print("no such pair of integers exists")
# else:
#     print("root :" + str(root) + " ,pwr :" + str(pwr))

"""
4.3的部分代码需要优化一下，那就是-16  这种特殊情况，应该直接跳出循环。为了满足这种情况，应该设置一个
标志位 can_be_found.  这样可以减少猜测的次数。
"""
ele = int(input("Enter a integer: "))
root = 0
pwr = 2

is_fond = False
can_be_found = True
guess_num = 0
while can_be_found and not is_fond and root ** 2 <= abs(ele):

    for pwr in range(2, 6):
        guess_num += 1
        if root ** pwr > abs(ele):
            break
        elif root ** pwr == abs(ele):
            if ele >= 0:
                is_fond = True
            else:
                #  -1 比较特殊,因为 -1 的 2次方的绝对值为1，如果按照elif来处理,那么将是一个错误。
                #  毕竟 -1的3次方的绝对值也为1
                if ele == -1:
                    root = -root
                    pwr = 3
                    is_fond = True
                elif pwr % 2 != 0:
                    root = -root
                    is_fond = True
                else:
                    can_be_found = False

            break

    if not is_fond and can_be_found:
        root += 1

print("guess num is " + str(guess_num))
if not is_fond:
    print("no such pair of integers exists")
else:
    print("root :" + str(root) + " ,pwr :" + str(pwr))
