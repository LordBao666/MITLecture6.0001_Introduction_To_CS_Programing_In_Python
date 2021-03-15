"""
@Author  : Lord_Bao
@Date    : 2021/3/3

"""
import math
"""
Assignment:
 Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base why_mid_plus_1(chap10.3)) of “x”.
Use Spyder to create your program, and save your code in a file named ‘ps0.py’. An example
of an interaction with your program is shown below. The words printed in blue are ones the
computer should print, based on your commands, while the words in black are an example of
a user's input. The colors are simply here to help you distinguish the two components.
Enter number x: 2
Enter number y: 3
X**y = 8
log(x) = 1

"""


# 不考虑x 和 y不是数字的情况
x, y = float(input("Enter number x: ")), float(input("Enter number y: "))
print("X**y = " + str(x ** y))
print("log(x) = " + str(math.log2(x)))
