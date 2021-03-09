"""
@Author  : Lord_Bao
@Date    : 2021/3/9

"""


def sum_digits(s):
    """Assumes s is a string
       Returns the sum of the decimal digits in s
       For example, if s is 'a2b3c' it returns 5'

    """
    result = 0
    try:
        for char in s:
            if char in "123456789":
                result += int(char)
        return result
    except TypeError:
        print("the parameter s MUST be a type of STRING")


if __name__ == '__main__':
    print(sum_digits("ab1234c1"))
    print(sum_digits([1, 2, 3, 4]))
