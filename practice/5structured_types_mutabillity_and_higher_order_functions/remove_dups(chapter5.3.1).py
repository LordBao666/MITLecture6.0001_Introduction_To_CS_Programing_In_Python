"""
@Author  : Lord_Bao
@Date    : 2021/3/6


  用 pythontutor  查看
"""


def remove_dups(list1, list2):
    """
       Assumes that list1 and list2 are lists.
       Removes any element from list1 that also occurs in list2
    """

    # for e1 in list1:
    #     if e1 in list2:
    #         list1.remove(e1)
    list1_tmp = list1[:]
    # list1_tmp = list(list1)
    for e1 in list1_tmp:
        if e1 in list2:
            list1.remove(e1)


list1 = [1, 2, 3, 4]
list2 = [1, 2, 5, 6]
remove_dups(list1, list2)
print('list1 =', list1)
