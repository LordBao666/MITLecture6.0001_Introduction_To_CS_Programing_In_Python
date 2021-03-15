"""
@Author  : Lord_Bao
@Date    : 2021/3/14

"""


def fact_iter(n):
    """

    :param n:  Assume n is a positive integer
    :return: n!
    算法复杂度分析  循环执行n次  ，故O（n)
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fact_recur(n):
    """
       算法复杂度也为n
    """
    if n == 1:
        return n
    else:
        return n * fact_recur(n - 1)


if __name__ == '__main__':
    print(fact_iter(5))
    print(fact_recur(5))
