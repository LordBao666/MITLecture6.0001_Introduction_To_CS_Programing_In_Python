"""
@Author : Lord_Bao
@Date   : 2021/3/3
"""

"""
Finger exercise: Write a program that examines three variables- x, y, and z- and
prints the largest odd number among them. If none of them are odd, it should
print a message to that effect.
"""

"""
思路：
1.判断3个数字是不是奇数
2.在1基础上，如果有奇数,则进行比较。没有奇数，则打印提示。
"""

# 我们假设这些变量是整型,并提示用户输入整型变量值。不考虑浮点，字符串等复杂类型
print("input 3 integers\n")

x, y, z = int(input("first:")), int(input("second:")), int(input("third:"))

x_is_odd_flag = x % 2 != 0
y_is_odd_flag = y % 2 != 0
z_is_odd_flag = z % 2 != 0

exists_odd_flag = x_is_odd_flag or y_is_odd_flag or z_is_odd_flag

if exists_odd_flag:
    largest_odd = -1
    confirm_the_current_largest_odd_yet = False

    if x_is_odd_flag:
        #  由于x是第一个奇数，那么可以这样写
        largest_odd = x
        confirm_the_current_largest_odd_yet = True

    if y_is_odd_flag:
        if not confirm_the_current_largest_odd_yet:
            largest_odd = y
            confirm_the_current_largest_odd_yet = True
        else:
            if largest_odd < y:
                largest_odd = y

    if z_is_odd_flag:
        if not confirm_the_current_largest_odd_yet:
            largest_odd = z
            confirm_the_current_largest_odd_yet = True
        else:
            if largest_odd < z:
                largest_odd = z

    print("\nthe largest odd number is " + str(largest_odd))
else:
    print("\nno odd integer")
