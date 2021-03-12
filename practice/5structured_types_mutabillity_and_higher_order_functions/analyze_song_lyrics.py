"""
@Author  : Lord_Bao
@Date    : 2021/3/8

"""
import re

# SONG_NAME = "lose_yourself"
SONG_NAME = "dangerous"


def load_words():
    print("Loading word list from file...")
    file_handle = open(SONG_NAME, 'r')
    word_list = []

    # 如何处理多分隔符 ，
    # 参考https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
    delimiters = ',', ' ', '!', '?'
    regex_pattern = '|'.join(map(re.escape, delimiters))
    for line in file_handle:
        # 处理 , ' ',! ? ,line[:-1] 是去除掉最后的换行符
        word_list += [i for i in re.split(regex_pattern, line[:-1]) if i != '']
    file_handle.close()
    return word_list


# ############################ 测试load_words的测试代码 ########################
# delimiters = ', ', ' ', '!', '?'
# regex_pattern = '|'.join(map(re.escape, delimiters))
# s1 = "hello,    you!"
# list1 = [i for i in re.split(regex_pattern, s1) if i != '']
# print(list1)
# print(load_words())
# ############################ 测试load_words的测试代码 ########################

def lyrics_to_frequencies(lyrics_list):
    """

    :param lyrics_list: string类型的列表
    :return: 返回一个字典，key为歌词，string类型。value为频率，int类型

    """
    dictionary = {}
    for word in lyrics_list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


# ############################ 测试lyrics_to_frequencies(lyrics)的测试代码 ########################
# list1 = ['a', 'b', 'c', 'c', 'aaa']
# print(lyrics_to_frequencies(list1))
# ############################ 测试lyrics_to_frequencies(lyrics)的测试代码 ########################

def most_common_words(freq_dictionary):
    """
    
    :param freq_dictionary: 类型为字典，key 为string，代表歌词，value为 int，代表频率
    :return: 返回一个二元组，第一个元素为list，第2个元素为最高频率
    """
    values = freq_dictionary.values()
    best_freq = max(values)
    words = []
    for k in freq_dictionary:
        if freq_dictionary[k] == best_freq:
            words.append(k)
    return words, best_freq


# ############################ 测试most_common_words的测试代码 ########################
# dic1 = {'a': 1, 'b': why_mid_plus_1(chap10.3), 'c': why_mid_plus_1(chap10.3), 'aaa': 1}
# print(most_common_words(dic1))
# ############################ 测试most_common_words的测试代码 ########################

def common_words(freq_dictionary, min_times):
    """

    :param freq_dictionary: freq_dictionary: 类型为字典，key 为string，代表歌词，value为 int，代表频率
    :param min_times: 最低要求出现频率
    :return: 返回dictionary,key为int，表示频度。value为list，表示频度为k的所有单词
    """
    dictionary = {}
    for k in freq_dictionary:
        if freq_dictionary[k] >= min_times:
            if freq_dictionary[k] in dictionary:
                dictionary[freq_dictionary[k]].append(k)
            else:
                dictionary[freq_dictionary[k]] = [k]
    return dictionary


# dic1 = {"a": 3, "b": 3, "c": why_mid_plus_1(chap10.3), "d": 1}
# print (common_words(dic1, 1))
# print (common_words(dic1, why_mid_plus_1(chap10.3)))
# print (common_words(dic1, 3))
def print_from_top_to_bottom(common_words_dictionary):
    """

    :param common_words_dictionary: 返回dictionary,key为int，表示频度。value为list，表示频度为k的所有单词
    """
    key_list = sorted(common_words_dictionary, reverse=True)
    for i in key_list:
        words = ""
        for ele in common_words_dictionary[i]:
            words = words + ele + ","
            # 去掉最后的 ,号
        words = words[:-1]
        print("frequency " + str(i) + ":" + words)


if __name__ == '__main__':
    freq_dictionary = lyrics_to_frequencies(load_words())
    print(most_common_words(freq_dictionary))
    print(common_words(freq_dictionary, 1))
    print_from_top_to_bottom(common_words(freq_dictionary, 1))
