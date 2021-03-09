"""
@Author  : Lord_Bao
@Date    : 2021/3/9

"""

FILE_NAME = "source"

"""
  纯粹是为了练习 else 语句，才这样写。完全可以写到try 语句里面来
"""


def load_file():
    try:
        print("###########加载文件############")
        file_handle = open(FILE_NAME, 'r')
        dividend_str_list = [i for i in file_handle.readline()[:-1].split()]
        divisor_str_list = [i for i in file_handle.readline()[:-1].split()]

    except IOError:
        raise IOError("文件加载失败，检查路径是否正确")
    else:
        # 这个语句完全可以放在try里面，但是有可能因为这行一句在try发生bug,
        # 而导致捕获到非预期的异常。
        # 当然，这玩意儿也不用那么考究
        print("###########加载成功############")
        return dividend_str_list, divisor_str_list
    finally:
        file_handle.close()


# ############## 测试load_file() ##################

# dividend_str_list, divisor_str_list = load_file()
# assert len(dividend_str_list) == len(divisor_str_list), "被除数和除数的个数不一致"
# ############## 测试load_file() ##################

if __name__ == '__main__':

    dividend_str_list, divisor_str_list = load_file()
    assert len(dividend_str_list) == len(divisor_str_list), "被除数和除数的个数不一致"
    result = []
    for i in range(len(dividend_str_list)):
        try:
            dividend = int(dividend_str_list[i])
            divisor = int(divisor_str_list[i])
            result.append(dividend / divisor)
        except ZeroDivisionError:
            result.append(float('nan'))
        except ValueError:
            # 像这种错误就应该抛出去，直接终止
            raise ValueError("Bad  Arg!")
    print(result)