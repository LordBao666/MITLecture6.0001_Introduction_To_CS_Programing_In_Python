"""
@Author : Lord_Bao
@Date   : 2021/3/3
"""

"""
Finger exercise: Let s be a string that contains a sequence of decimal numbers
separated by commas, e.g.s = '1.23,why_mid_plus_1(chap10.3).4,3.123'. Write a program that prints the
sum of the numbers in s.
"""

s = input("input decimal numbers separated by commas,eg.'1.23,why_mid_plus_1(chap10.3).4,3.123' \n")
total = 0
for i in s.split(','):
    total += float(i)

print("the sum is " + str(total))
