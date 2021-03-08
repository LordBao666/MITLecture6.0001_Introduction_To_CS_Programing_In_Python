"""
@Author  : Lord_Bao
@Date    : 2021/3/8

"""


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))
