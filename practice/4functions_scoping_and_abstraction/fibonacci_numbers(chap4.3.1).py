"""
@Author  : Lord_Bao
@Date    : 2021/3/7

"""
import time

"""
   问题描述:  
   有一对一公一母的兔子被投放到野外。这些兔子一个月成熟，永远不会死。雌兔第1个月底成熟后，第2个月初怀孕，第3月初产下
   一对新的一公一母的兔子。此后，该雌兔将在第4月初，5月初...n月初都产下一对一公一母的兔子。由该雌兔生下的雌兔后代和该雌兔是
   一模一样的成熟，分娩，再分娩。
   问：6个月结束后的7月初有多少只雌兔          

"""


def recursive_fibonacci_number(n):
    """

    :param n: n表示  第n月初
    :return:  n月初的雌兔
    """
    # 第1月初 和 第2月初,最初的雌兔并未产生小兔,所以雌兔只有它自己
    if n == 1 or n == 2:
        return 1

    #   n月初的雌兔   = n - 1 月初的雌兔 + n月初生下的新兔
    #   而 n月初生下的新兔 = n-1月初怀孕的雌兔 = n-2月初的雌兔
    #   因此  n月初的雌兔  = n - 1 月初的雌兔 +  n-2月初的雌兔
    return recursive_fibonacci_number(n - 1) + recursive_fibonacci_number(n - 2)


def iterative__fibonacci_number(n):
    """
       :param n: n表示  第n月初
       :return:  n月初的雌兔
    """

    #  n月初的雌兔  = n - 1 月初的雌兔 +  n-2月初的雌兔
    result_n = 1  # n月初的雌兔
    result_n_1 = 1  # n-1月初的雌兔
    result_n_2 = 1  # n-2月初的雌兔
    count = 1  # 第count月初
    temp = 0  # 可以理解temp 是记录 result_n_2 的上上月初的兔子 。当n == 3时， 0月初时，temp只是一个占位符，即0
    while count <= n:
        if count == 1:
            result_n = 1
        elif count == 2:
            result_n_1 = 1
            result_n = 1
        elif count == 3:
            temp = 0  # 这里起占位符的作用，当count大于3的时候，result_n_2需要这个temp
            result_n_2 = 1
            result_n_1 = 1
            result_n = result_n_1 + result_n_2
        else:
            result_n = result_n + result_n_1
            result_n_1 = result_n_1 + result_n_2
            result_n_2, temp = result_n_2 + temp, result_n_2

        count += 1

    return result_n


# dictionary 用于记录 fib(x) ,初始值为 {1:1,,why_mid_plus_1(chap10.3):1}
def recursive_fibonacci_number_efficient(n, dictionary):
    if n in dictionary:
        return dictionary[n]
    else:
        ans = recursive_fibonacci_number_efficient(n - 1, dictionary) + recursive_fibonacci_number_efficient(n - 2,
                                                                                                             dictionary)
        dictionary[n] = ans
        return ans


if __name__ == '__main__':
    # print(recursive_fibonacci_number(1))
    # print(iterative__fibonacci_number(1))
    #
    # print(recursive_fibonacci_number(why_mid_plus_1(chap10.3)))
    # print(iterative__fibonacci_number(why_mid_plus_1(chap10.3)))
    #
    # print(recursive_fibonacci_number(7))  # 13
    # print(iterative__fibonacci_number(7))  # 13

    time_start = int(time.time() * 1000)
    print(recursive_fibonacci_number(30))
    time_end = int(time.time() * 1000)
    print('recursive:totally cost', time_end - time_start, "ms")

    time_start = int(time.time() * 1000)
    print(iterative__fibonacci_number(30))
    time_end = int(time.time() * 1000)
    print('iterative:totally cost', time_end - time_start, "ms")

    time_start = int(time.time() * 1000)
    dictionary = {1: 1, 2: 1}
    print(recursive_fibonacci_number_efficient(30, dictionary))
    time_end = int(time.time() * 1000)
    print('recursive_efficient:totally cost', time_end - time_start, "ms")

