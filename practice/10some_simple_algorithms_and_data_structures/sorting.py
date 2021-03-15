"""
@Author  : Lord_Bao
@Date    : 2021/3/14

"""


def bubble_sort(L):
    """
    基本思想：  对L进行一次遍历，如果前面的元素比后面的元素大，那么进行一次交换，一次迭代后。数组最后的元素是最大的。
                这种排序就很像 是冒泡。

    """
    #  ########### 下面这种方法不管是 worst_case,best_case,average_case都是 O（n^2） #########
    # for i in range(len(L)):
    #     for j in range(len(L)-1):
    #         if L[j] > L[j + 1]:
    #             L[j], L[j + 1] = L[j + 1], L[j]
    # return L
    # ##################################################################

    # #############下面这种情况 best_case即顺序的时候 为O(1),worst_case即倒序的时候 为O（n^2)#############
    # 设置一个swap, 在循环中设置为False,如果产生一次swap，那么就设置swap为True。如果为False，
    # 那么表示 第1个元素 比 第2个元素,第2个元素比第3个元素小,如此类推,即表明列表元素已经有序，退出循环。
    swap = True
    while swap:
        swap = False
        for index in range(1, len(L)):
            if L[index - 1] > L[index]:
                L[index - 1], L[index] = L[index], L[index - 1]
                swap = True
    return L


def selection_sort(L):
    """
    选择排序 每次从list挑选最小的元素放在最前面，然后从子list再挑选最小的元素。
    算法复杂度 O（n^2）  best_case avg_case,worst_case都是O(n^2)
    """

    for i in range(len(L)):

        small_index = i
        for j in range(i, len(L)):
            if L[j] < L[small_index]:
                small_index = j
        L[i], L[small_index] = L[small_index], L[i]
    return L


def merge_sort(L):
    """
           规定排序的基本思想是将L拆分为两半，然后分别对两半进行排序，然后再对两半进行归并。
           base_case 为 当一个L的大小为1或0时，直接返回。

           算法分析， 一个size为n的列表。那么将会分为logn层。最坏的情况是，处于同一级的left_part和 right_part将在
           merge中执行 len(right_part) + len(left_part) 操作。 也就是说在每一层都是 执行 O(n)次操作。那么总的是
           O(n) * O(logn) = O(nlogn)
    """

    def merge(left_part, right_part):
        i = 0
        j = 0
        result = []

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                result.append(left_part[i])
                i += 1
            else:
                result.append(right_part[j])
                j += 1

        if i < len(left_part):
            for elt in left_part[i:]:
                result.append(elt)
        if j < len(right_part):
            for elt in right_part[j:]:
                result.append(elt)
        return result

    if len(L) < 2:  # base_case
        return L[:]
    else:
        mid = len(L) // 2
        left_part = merge_sort(L[:mid])
        right_part = merge_sort(L[mid:])
        return merge(left_part, right_part)


if __name__ == '__main__':
    list1 = [9, 6, 7, 5, 4]

    print(bubble_sort(list1[:]))
    print(selection_sort(list1[:]))
    print(merge_sort(list1[:]))
