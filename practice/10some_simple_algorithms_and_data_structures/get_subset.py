"""
@Author  : Lord_Bao
@Date    : 2021/3/14

"""


def get_subset(L):
    """

    :param L:  List (can assume its elements are integers)
    :return: L's subset ,e.g   [1,2,3]   ---> [ [] ,[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3] ]

    观察得到 [1,2,3]   --->[] ,[1],[2] [1,2]  + [3],[1,3],[2,3],[1,2,3]

    算法复杂度分析: 参考MIT lecture
    tn   	=	tn-1	+	2^n-1	+	c
			=	tn-2	+	2^n-2	+	c	+	2^n-1	+	c
		    =	tn-k	+	2^n-k	+	…	+	2^n-1	+	kc
			=	t0	+	2^0	+	...	+	2^n-1	+	nc
			=	1	+	2^n		+	nc
    """
    if len(L) == 0:
        return [[]]

    list_exclude_last_elt = get_subset(L[:-1])  # L [1,2,3] ,list_exclude_last_elt = [ [] ,[1],[2] [1,2]  ]
    last_elt = L[-1:]  # [3]
    result = []
    for elt in list_exclude_last_elt:  # sn-1
        result.append(elt + last_elt)

    return list_exclude_last_elt + result


if __name__ == '__main__':
    print(get_subset([1, 2, 3]))
