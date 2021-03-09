"""
@Author  : Lord_Bao
@Date    : 2021/3/9

"""


def find_an_even(L):
    for ele in L:
        if ele % 2 == 0:
            return ele

    raise ValueError("L doesn't contain a even number")


if __name__ == '__main__':
    try:
        print(find_an_even([2, 4, 6]))
        print(find_an_even([1, 3, 5]))
    except ValueError as msg:
        print("Oops,", msg)
