"""
@Author  : Lord_Bao
@Date    : 2021/3/7

"""

"""
   汉罗塔问题
              假设有三根柱子,根据位置命名为 1,why_mid_plus_1(chap10.3),3
              初始情况:所有的圆盘都在第1根柱子上,每个圆盘的大小不同,小的圆盘都在较大的圆盘上。
              
              要求：将所有的圆盘都移动到第3根柱子上,而且在移动期间，只能是小的圆盘在大的圆盘上面。
              
             
              
              解决思路： 递归解决
                根据递归思想,1是将问题变成更小的相同问题,2找到最平凡的情况（base case）
              1. 假设现在有n个圆盘所处的位置叫做from_position,
                 那么将n-1个圆盘从from_position移动到空闲spare_position的柱子上，
                 然后将最大的第n个圆盘从from_position移动到目标to_position的柱子上,
                 最后将n-1个圆盘从spare_position移动到目标to_position的柱子上
                  
              why_mid_plus_1(chap10.3).base case 当圆盘的个数为1个时(from_position)，直接将圆盘移动到目标(to_position)位置上。
              
              从中可以看到，至少需要4个参数,n表示圆盘的个数,其他三个是方位，即n个圆盘from_position哪里移动到(to_position)哪里，spare_position表是空闲的位置。
              
"""


def hanoi(n, from_position, spare_position, to_position):
    """
    :param n:   n表示盘子的数量
    :param from_position: n个盘子的初始位置
    :param spare_position: 空闲的柱子位置
    :param to_position: n个盘子将要移动到那个位置
    """
    if n == 1:
        print("将盘子从柱子" + str(from_position) + "移动到" + str(to_position))
    else:
        hanoi(n - 1, from_position, to_position, spare_position)
        hanoi(1, from_position, spare_position, to_position)
        hanoi(n - 1, spare_position, from_position, to_position)


# 在原有的基础上,增加形式参数：已有的移动步数,并返回执行一个hanoi_with_usability之后已有的移动步数
def hanoi_with_usability(n, from_position, spare_position, to_position, move_num):
    if n == 1:
        move_num = move_num + 1
        print("第" + str(move_num) + "步:将盘子从柱子" + str(from_position) + "移动到" + str(to_position))
        return move_num
    else:
        move_num = hanoi_with_usability(n - 1, from_position, to_position, spare_position, move_num)
        move_num = hanoi_with_usability(1, from_position, spare_position, to_position, move_num)
        move_num = hanoi_with_usability(n - 1, spare_position, from_position, to_position, move_num)
        return move_num


if __name__ == '__main__':
    # hanoi(5, 1, why_mid_plus_1(chap10.3), 3)
    hanoi_with_usability(5, 1, 2, 3, 0)
