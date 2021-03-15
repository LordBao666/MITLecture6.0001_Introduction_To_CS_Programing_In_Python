# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    e.g
    secret_word = apple ,letters_guessed = ['a','p','m','n','l','e'] ,返回True
    secret_word = apple ,letters_guessed = ['p','m','n','l','e'] ,返回False
    '''

    # 存储已经在letters_guessed检测通过的字母
    already_checked_list = []
    for char in secret_word:
        #  如果单词已经在检查通过的单词中出现过，那么直接跳出当次循环
        #  比如 secret_word 为 apple,letters_guessed为 ['a','p',......]时
        #  检测第2个p时,此时的already_checked_list = ['a','p'],如果p已经在里面出现，那么没必要继续检查
        if char in already_checked_list:
            continue

        # 每个单词是否在letters_guessed的标志
        is_fond = False
        for ele in letters_guessed:
            if char == ele:
                is_fond = True
                already_checked_list.append(char)
                break
        if not is_fond:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.

    e.g
    secret_word ="apple",letters_guessed = ['a','l','e'] ,返回"a_ _ le"
    secret_word ="apple",letters_guessed = ['p','m','e'] ,返回"_ pp_ e"
    '''
    # 存储已经在letters_guessed检测通过的单词
    already_checked_list = []
    guessed_word = ""
    for char in secret_word:

        if char in already_checked_list:
            guessed_word += char
            continue

        is_fond = False
        for ele in letters_guessed:
            if char == ele:
                is_fond = True
                already_checked_list.append(char)
                guessed_word += char
                break
        if not is_fond:
            guessed_word += "_ "

    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
      e.g letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']  return "abcdfghjlmnoqtuvwxyz"

    '''

    available_letters = string.ascii_lowercase
    for char in letters_guessed:
        available_letters = available_letters.replace(char, '')
    return available_letters


def handle_invalid_input_letter(current_guess_letter, letters_guessed, warning_left, guesses_left):
    '''
    :param guesses_left: int , the number of times that the user still can guess
    :param warning_left: int, the number of  warnings left
    :param current_guess_letter: string（length ==1）,the current guess letter
    :param letters_guessed : list of letters ,letters which have been guessed
    :return: a tuple(warning_left,guesses_left,valid_type)  valid_type 0 表示正常 1表示不是字母 2表示是已经猜过的字母
    '''
    valid_type = 0
    # 如果当前猜的不是字母或者说是已经猜过的字母
    if not str.isalpha(current_guess_letter) or str.lower(current_guess_letter) in letters_guessed:
        if not str.isalpha(current_guess_letter):
            valid_type = 1
        elif str.lower(current_guess_letter) in letters_guessed:
            valid_type = 2

        if warning_left > 0:
            warning_left -= 1
        else:
            guesses_left -= 1
    return warning_left, guesses_left, valid_type


def total_score(secret_word, guesses_remaining):
    """
    secret_word: string, the word the user is guessing
    guesses_remaining : int,the number of times that the user still can guess
    return the score based on secret_word and guesses_remaining
    e.g secret_word = "apple", 去掉重复字母，那么就有4个字母。假设guesses_remaining = 4. 那么返回3*4 = 12
    """
    letter_list = []
    for char in secret_word:
        if char not in letter_list:
            letter_list.append(char)
    return len(letter_list) * guesses_remaining


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)  # 初始化(_ 的长度取决于secret_word大小）为 _ _ ..._ _

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings_left) + " warnings left. ")
    print("-------------")

    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:
        print("You have " + str(guesses_left) + " guesses left. ")
        print("Available letters: " + get_available_letters(letters_guessed))
        # 根据题目 用户肯定会输入一个字符,也就是不考虑输入的字符是0个或是大于1个的情况
        current_guess_letter = input("Please guess a letter:")
        warnings_left_tmp, guesses_left_tmp, valid_type = handle_invalid_input_letter(current_guess_letter,
                                                                                      letters_guessed,
                                                                                      warnings_left, guesses_left)

        if valid_type == 0:  # 0表示正常
            # 下面两行不设置也没有问题
            # warnings_left = warnings_left_tmp
            # guesses_left = guesses_left_tmp

            current_guess_letter = str.lower(current_guess_letter)
            letters_guessed.append(current_guess_letter)
            tmp = get_guessed_word(secret_word, letters_guessed)

            # 说明用户再次猜错
            if tmp == guessed_word:
                print("Oops! That letter is not in my word:" + guessed_word)
                if current_guess_letter in ["a", "e", "i", "o", "u"]:  # 元音扣 2个 guess
                    guesses_left -= 2
                else:
                    guesses_left -= 1
            else:
                guessed_word = tmp
                print("Good guess:" + guessed_word)

        elif valid_type == 1:  # 1表示  字符输入不是字母
            if warnings_left != warnings_left_tmp:  # 因非法字符输入是扣的warnings
                warnings_left = warnings_left_tmp
                print("Oops! That is not a valid letter. You have " + str(warnings_left) + " warnings left: " + str(
                    guessed_word))
            else:
                guesses_left = guesses_left_tmp  # 因非法字符输入是扣的guesses
                print("Oops! That is not a valid letter. You have no warnings left: " + str(
                    guessed_word))

        elif valid_type == 2:  # 2表示 字符是已经输入过的字母
            if warnings_left != warnings_left_tmp:  # 因重复输入是扣的warnings
                warnings_left = warnings_left_tmp
                print(
                    "Oops!  You've already guessed that letter. You have " + str(
                        warnings_left) + " warnings left: " + str(
                        guessed_word))
            else:  # 因重复输入是扣的guesses
                guesses_left = guesses_left_tmp
                print(
                    "Oops!  You've already guessed that letter. You have no warnings left: " + str(
                        guessed_word))

        print("-------------")

    if guesses_left > 0:  # 成功猜出答案
        print("Congratulations, you won! ")
        print("Your total score for this game is: " + str(total_score(secret_word, guesses_left)))
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    # 去掉空白符
    my_word = my_word.replace(' ', '')

    # 处理 ("a_ ple", "apple") 这种情况，需要用 guessed_list来记录已经猜测过的单词
    guessed_list = []
    if len(my_word) == len(other_word):

        for i in range(len(my_word)):
            if my_word[i] == "_":
                continue
            elif my_word[i] != other_word[i]:
                return False
            else:
                if my_word[i] not in guessed_list:
                    guessed_list.append(my_word[i])

        # 处理 ("a_ ple", "apple") 这种情况，到这里 guessed_list为 ['a','p','l','e']
        for i in range(len(my_word)):
            if my_word[i] == "_":
                if other_word[i] in guessed_list:
                    return False

    else:
        return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matched_list = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            possible_matched_list.append(other_word)
    if len(possible_matched_list) == 0:
        print("No matches found")
    else:
        count = 0
        s1 = ""
        for ele in possible_matched_list:
            count += 1
            if count % 15 == 0:
                s1 += ele + "\n"
            else:
                s1 += ele + " "
        #  单纯是为了格式好看，以15为一个换行，当刚好15个的倍数结尾时，去掉最后一个换行符
        if count % 15 == 0:
            s1 = s1[:-1]
        print(s1)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)  # 初始化(_ 的长度取决于secret_word大小）为 _ _ ..._ _

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings_left) + " warnings left. ")
    print("-------------")

    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:
        print("You have " + str(guesses_left) + " guesses left. ")
        print("Available letters: " + get_available_letters(letters_guessed))
        # 根据题目 用户肯定会输入一个字符,也就是不考虑输入的字符是0个或是大于1个的情况
        current_guess_letter = input("Please guess a letter:")
        if current_guess_letter == "*":
            show_possible_matches(guessed_word)
            print("-------------")
            continue

        warnings_left_tmp, guesses_left_tmp, valid_type = handle_invalid_input_letter(current_guess_letter,
                                                                                      letters_guessed,
                                                                                      warnings_left, guesses_left)

        if valid_type == 0:  # 0表示正常
            # 下面两行不设置也没有问题
            # warnings_left = warnings_left_tmp
            # guesses_left = guesses_left_tmp

            current_guess_letter = str.lower(current_guess_letter)
            letters_guessed.append(current_guess_letter)
            tmp = get_guessed_word(secret_word, letters_guessed)

            # 说明用户再次猜错
            if tmp == guessed_word:
                print("Oops! That letter is not in my word:" + guessed_word)
                if current_guess_letter in ["a", "e", "i", "o", "u"]:  # 元音扣 2个 guess
                    guesses_left -= 2
                else:
                    guesses_left -= 1
            else:
                guessed_word = tmp
                print("Good guess:" + guessed_word)

        elif valid_type == 1:  # 1表示  字符输入不是字母
            if warnings_left != warnings_left_tmp:  # 因非法字符输入是扣的warnings
                warnings_left = warnings_left_tmp
                print("Oops! That is not a valid letter. You have " + str(warnings_left) + " warnings left: " + str(
                    guessed_word))
            else:
                guesses_left = guesses_left_tmp  # 因非法字符输入是扣的guesses
                print("Oops! That is not a valid letter. You have no warnings left: " + str(
                    guessed_word))

        elif valid_type == 2:  # 2表示 字符是已经输入过的字母
            if warnings_left != warnings_left_tmp:  # 因重复输入是扣的warnings
                warnings_left = warnings_left_tmp
                print(
                    "Oops!  You've already guessed that letter. You have " + str(
                        warnings_left) + " warnings left: " + str(
                        guessed_word))
            else:  # 因重复输入是扣的guesses
                guesses_left = guesses_left_tmp
                print(
                    "Oops!  You've already guessed that letter. You have no warnings left: " + str(
                        guessed_word))

        print("-------------")

    if guesses_left > 0:  # 成功猜出答案
        print("Congratulations, you won! ")
        print("Your total score for this game is: " + str(total_score(secret_word, guesses_left)))
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    # secret_word = "apple"
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # letters_guessed = ['e', 'a', 'l', 'p', 'r', 's']
    # print(is_word_guessed(secret_word,letters_guessed))

    # secret_word = "apple"
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # letters_guessed = ['e', 'a', 'l', 'p', 'r', 's']
    # print(get_guessed_word(secret_word, letters_guessed))

    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # print(get_available_letters(letters_guessed))
    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # print(match_with_gaps("te_ t", "tact"))
    # print(match_with_gaps("a_ _ le", "banana"))
    # print(match_with_gaps("a_ _ le", "apple"))
    # print(match_with_gaps("a_ ple", "apple"))
    # show_possible_matches("t_ _ t")
    # show_possible_matches("abbbb_ ")
    # show_possible_matches("a_ pl_ ")

    # hangman_with_hints("apple")
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
