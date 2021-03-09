"""
@Author  : Lord_Bao
@Date    : 2021/3/9

"""


class Coordinate(object):
    """
        坐标 ： 两个属性 x ,y ,类型均为float
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """
            other 和 self 都是Coordinate对象，此方法返回两点之间的距离
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        """
             当print(Coordinate)对象时，返回此方法的string
        """
        return "<" + str(self.x) + "," + str(self.y) + ">"


if __name__ == '__main__':
    a = Coordinate(3, 4)
    b = Coordinate(0, 0)
    print(a.distance(b))  # 自动传入自己的变量
    print(Coordinate.distance(a, b))  # 这样做并不常见

    print(a)
    print(type(a))
    print(Coordinate)
    print(type(Coordinate))
