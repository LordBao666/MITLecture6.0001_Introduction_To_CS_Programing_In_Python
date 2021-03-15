"""
@Author  : Lord_Bao
@Date    : 2021/3/15

"""


class MySupClass(object):
    def __init__(self):
        pass

    def method_to_be_implemented(self):
        raise NotImplementedError


class Offspring(MySupClass):
    def method_to_be_implemented(self):
        pass

    def special_method(self):
        pass


if __name__ == '__main__':
    son = Offspring()
