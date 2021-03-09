"""
@Author  : Lord_Bao
@Date    : 2021/3/9

"""


def get_rations(L1, L2):
    """
    Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[i]
    """
    result = []
    for index in range(len(L1)):
        try:
            result.append(L1[index] / L2[index])
        except ZeroDivisionError:
            result.append(float('nan'))
        except:
            raise ValueError("get_ratios called with bad arg")
    return result


if __name__ == '__main__':
    try:
        print(get_rations([1, 2, 3], [2, 4, 6]))
        print(get_rations([1, 2, 3], [2, 4, 0]))
        print(get_rations([1, 2, 3], [2, 4, 'a']))
    except ValueError as msg:
        print(msg)
