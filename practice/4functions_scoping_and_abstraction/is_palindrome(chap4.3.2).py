"""
@Author  : Lord_Bao
@Date    : 2021/3/7

"""

"""
   忽略大小写,空格,标点符号。检查是否是回文
"""


def is_palindrome(s):
    def to_chars(s):
        s = s.lower()  # 忽略大小写
        letters = ""
        for char in s:
            if char in "abcdefghijklmnopqrstuvwxyz": # 忽略符号,空格符等
                letters += char

        return letters

    def is_pal(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))


if __name__ == '__main__':
    print(is_palindrome("dogGOD"))
    print(is_palindrome("dogOOD"))
    print(is_palindrome("Able	was	I,	ere	I	saw	Elba"))
    print(is_palindrome("Are	we	not	drawn	onward,	we	few,	drawn	onward	to	new	era?"))
