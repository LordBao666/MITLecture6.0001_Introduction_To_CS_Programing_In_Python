"""
@Author  : Lord_Bao
@Date    : 2021/3/14

"""


def int_to_str(i):
    """

    :param i: Assume i is a non-negative integer
    :return: return i in the format of string
    算法复杂度分析 ，输入规模即为i （注意：算法规模既可以是显式的，比如list的大小，也可以是隐式的，比如这个demo
    当算法规模为n的时候，while循环会执行 logn次。所以 O(logn)
    """
    result = ""
    if i == 0:
        return '0'
    else:
        while i != 0:
            result += str(i % 10)
            i = i // 10
        return result


if __name__ == '__main__':
    print(int_to_str(666))
    print(int_to_str(0))
    print(type(int_to_str(0)))