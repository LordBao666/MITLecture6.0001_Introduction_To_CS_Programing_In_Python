"""
@Author  : Lord_Bao
@Date    : 2021/3/5

"""

"""
Finger exercise: Write a function isIn that accepts two strings as arguments and
returns True if either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operation in.
"""


def isIn(s1, s2):
    return s1 in s2 or s2 in s1


# s1 = input("enter the  first string :")
# s2 = input("enter the  second string :")
#
# print(isIn(s1, s2))
