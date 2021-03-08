"""
@Author  : Lord_Bao
@Date    : 2021/3/6

"""


def findExtremeDivisor(n1, n2):
    """
    找到n1和n2的最小公因子 和 最大公因子，如果不存在则返回(None,None)
    最小公因子不包括1
    """
    min_divisor, max_divisor = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if min_divisor is None:
                min_divisor = i
            max_divisor = i

    #  元组可以不用打括号
    return min_divisor, max_divisor


def main():
    min_divisor, max_divisor = findExtremeDivisor(2, 4)
    print(min_divisor)
    print(max_divisor)


if __name__ == '__main__':
    main()
