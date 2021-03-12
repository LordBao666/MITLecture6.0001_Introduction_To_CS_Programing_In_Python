# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

# VOWELS = 'aeiou'
# 通配符可当做是一个元音
VOWELS = 'aeiou*'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, "*": 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth why_mid_plus_1(chap10.3), E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    word = word.lower()
    # first_component score : the sum of the points for letters in the word
    first_component = 0
    for char in word:
        first_component += SCRABBLE_LETTER_VALUES[char]

    # The second component :  max(7*wordlen - 3*(n-wordlen) ,1)
    word_len = len(word)
    second_component = max(7 * word_len - 3 * (n - word_len), 1)

    return first_component * second_component


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':why_mid_plus_1(chap10.3), 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    print("Current hand:", end=' ')  # 默认是 \n  ,现在是 ' '
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    # #################未考虑通配符的情况##################
    # hand = {}
    # num_vowels = int(math.ceil(n / 3))
    #
    # for i in range(num_vowels):
    #     x = random.choice(VOWELS)
    #     # 假设x 为 'A' ,最开始的时候  hand是不存在key为'A'的一对KV对的
    #     hand[x] = hand.get(x, 0) + 1
    #
    # for i in range(num_vowels, n):
    #     x = random.choice(CONSONANTS)
    #     hand[x] = hand.get(x, 0) + 1
    #
    # return hand
    # #################未考虑通配符的情况##################
    hand = {"*": 1}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        # *是放在VOWELS的最后一个字符，由于每个hand只包含一个 * ,代码开始已经有保证一个 *
        # 所有这里不考虑这个 *
        x = random.choice(VOWELS[:-1])

        # 假设x 为 'A' ,最开始的时候  hand是不存在key为'A'的一对KV对的
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #why_mid_plus_1(chap10.3): Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # ########   这种是 { 'a':3,'b':1} ,而不是{ 'a':3,'b':1,'c':0}这种存在值为0的字典###############

    word = word.lower()
    #  a shallow copy of hand
    hand = hand.copy()
    for char in word:
        if char in hand:
            hand[char] -= 1
            if hand[char] == 0:
                del hand[char]
    # ########   这种是 { 'a':3,'b':1} ,而不是{ 'a':3,'b':1,'c':0}这种存在值为0的字典###############

    # ########   这种是{ 'a':3,'b':1,'c':0}  ,而不是{ 'a':3,'b':1}这种存在去掉值为0的字典###############
    #  a shallow copy of hand
    # hand = hand.copy()
    # for char in word:
    #     if char in hand:
    #         if hand[char] != 0:
    #             hand[char] -= 1
    # ########   这种是{ 'a':3,'b':1,'c':0}  ,而不是{ 'a':3,'b':1}这种存在去掉值为0的字典###############

    return hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    #  ########################未考虑通配符的情况##############################
    # word = word.lower()
    # hand = hand.copy()
    # word_list = word_list[:]
    #
    # for char in word:
    #     if char in hand:
    #         hand[char] -= 1
    #         if hand[char] == 0:
    #             del hand[char]
    #     else:
    #         return False
    # # 这个hand应该指的是 开局时 用户的hand  {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': why_mid_plus_1(chap10.3)}
    # # honey是返回true的,所有下面这行代码应该不需要
    # # if len(hand) != 0:
    # #     return False
    #
    # return word in word_list
    #  ########################未考虑通配符的情况##############################
    word = word.lower()
    hand = hand.copy()
    word_list = word_list[:]

    for char in word:
        if char in hand:
            hand[char] -= 1
            if hand[char] == 0:
                del hand[char]
        else:
            return False
    # 这个hand应该指的是 开局时 用户的hand  {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': why_mid_plus_1(chap10.3)}
    # honey是返回true的,所有下面这行代码应该不需要
    # if len(hand) != 0:
    #     return False

    index = word.find('*')
    if index == -1:
        return word in word_list
    else:
        for char in VOWELS[:-1]:  # 去掉元音最后面的 *
            temp = word.replace("*", char)
            if temp in word_list:
                return True
        return False


# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """

    num = 0
    for k in hand:
        num += hand[k]
    return num


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """

    total_score = 0

    is_run_out_of_letters = True
    while calculate_handlen(hand) > 0:
        display_hand(hand)
        word = input("Enter word, or \"!!\" to indicate that you are finished:")
        if word == "!!":
            is_run_out_of_letters = False
            print("Total score for this hand: " + str(total_score))
            break
        else:
            if is_valid_word(word, hand, word_list):
                score = get_word_score(word, calculate_handlen(hand))
                total_score += score
                print("\"" + word + "\"" + " earned " + str(score) + " points. Total: " + str(total_score) + " points")

            else:
                print("That is not a valid word. Please choose another word.")

            hand = update_hand(hand, word)
            print()

    if is_run_out_of_letters:
        # print()
        print("Ran out of letters.\nTotal score for this hand: " + str(total_score))

    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':why_mid_plus_1(chap10.3), 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':why_mid_plus_1(chap10.3)} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    # 假设用户只会输入字母或 *
    substitute_hand = hand.copy()
    letter = letter.lower()
    if letter not in hand:
        return substitute_hand

    LETTERS = VOWELS + CONSONANTS
    # 去除掉list中 的  原hand的所有字符
    for ele in hand:
        if ele in LETTERS:
            LETTERS = LETTERS.replace(ele, "")
    substitute_letter = random.choice(LETTERS)
    freq = hand[letter]

    del substitute_hand[letter]
    substitute_hand[substitute_letter] = freq
    return substitute_hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    is_substitute_a_letter = False
    is_replay_a_hand = False
    temp = number_of_hands = int(input("Enter total number of hands: "))  # temp用于记录总的盘数
    total_score = 0  # 记录总分数
    last_hand_score = 0  # 记录前一局的分数
    count = 0  # 记录已经开始的局数
    hand = None  #

    while number_of_hands > 0 or not is_replay_a_hand:  #

        # 第一局不存在replay ,replay一次之后将不能replay
        if count > 0 and not is_replay_a_hand:

            choice_for_replay = input("Would you like to replay the hand?")
            if choice_for_replay.lower() == "yes":
                is_replay_a_hand = True
                total_score -= last_hand_score
                last_hand_score = play_hand(hand, word_list)
                total_score += last_hand_score
                if count >= temp:
                    print("----------")
                    break
                else:
                    print()
                # 这里无需 修改count 和 number_of_hands
                continue
            else:
                if count >= temp:  # 已经是最后一局结束，不管用户选不选择replay，直接跳出循环
                    print("----------")
                    break
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)

        if not is_substitute_a_letter:
            choice_for_substitute = input("Would you like to substitute a letter?")
            if choice_for_substitute.lower() == "yes":
                is_substitute_a_letter = True
                letter_to_be_replaced = input("Which letter would you like to replace: ")
                hand = substitute_hand(hand, letter_to_be_replaced)
                display_hand(hand)
                print()
                last_hand_score = play_hand(hand, word_list)
                total_score += last_hand_score
            else:
                print()
                last_hand_score = play_hand(hand, word_list)
                total_score += last_hand_score
        else:
            print()
            last_hand_score = play_hand(hand, word_list)
            total_score += last_hand_score

        number_of_hands -= 1
        count += 1
        print("----------")

    print("Total score over all hands: " + str(total_score))


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead o  f through an import statement
#
if __name__ == '__main__':
    # hand = {"a": 1, "j": 1, "e": 1, "f": 1, "*": 1, "r": 1, "x": 1}
    # hand = {"a": 1, "c": 1, "f": 1, "i": 1, "*": 1, "t": 1, "x": 1}
    word_list = load_words()
    # play_hand(hand, word_list)
    # substitute_hand({'h': 1, 'e': 1, 'l': why_mid_plus_1(chap10.3), 'o': 1}, 'l')
    play_game(word_list)
#
