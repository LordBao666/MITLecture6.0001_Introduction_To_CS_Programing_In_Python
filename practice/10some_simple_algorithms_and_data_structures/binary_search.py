"""
@Author  : Lord_Bao
@Date    : 2021/3/14

"""


def binary_search1(L, e):
    """

    :param L:  A ordered list(Assume its elements are integers)
    :param e:  Assume it's an integer
    :return:   Return True if e  is an element of L ,otherwise False

    将L对折x次之后的元素为1个，那么 2^x = len(L),  也就是说 x = log(len(L))。将len(L)看做是n。那么就是logn次
    在worst_case情况下，每次都会递归复制传入实际参数L的一半。那么等价于 复杂度为 1/2 n + 1/4 n + .....(加法项数为 logn次）
    那么根据 等比数列的求和公式，可以估计 为 O（n) 。 当然，这仅仅是拷贝带来的复杂度，其他常数操作是O（1）,总共logn次，那么还有一项
    是O（logn）  。  O（n) + O(logn)  = O(n)
    即这种带copy的二分查找复杂度是 O(n)
    """
    if len(L) == 0:
        return False

    if len(L) == 1:
        return L[0] == e

    mid = len(L) // 2  # mid是坐标
    if L[mid] == e:
        return True
    elif L[mid] > e:
        return binary_search1(L[:mid], e)
    else:
        return binary_search1(L[mid:], e)


def binary_search2(L, e):
    """
    算法复杂度分析，worst_case下，递归logn次。  每次都有比较,赋值等判断，那么算法复杂度即为O(logn)。
    完毕
    """

    def binary_search2_helper(L, low, high, e):
        if low > high:
            return False
        if low == high:
            return L[low] == e
        mid = (high + low) // 2
        if L[mid] == e:
            return True
        else:
            if L[mid] > e:
                high = mid - 1
                return binary_search2_helper(L, low, high, e)
            else:
                low = mid + 1
                return binary_search2_helper(L, low, high, e)

    return binary_search2_helper(L, 0, len(L) - 1, e)


if __name__ == '__main__':
    L = [3, 5, 7, 9, 10]
    # L = [3, 5]
    print(binary_search1(L, 6))
    print(binary_search2(L, 6))
    print(binary_search1(L, 5))
    print(binary_search2(L, 5))
