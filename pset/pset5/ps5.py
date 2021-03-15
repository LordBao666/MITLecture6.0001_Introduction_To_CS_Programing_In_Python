# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


# -----------------------------------------------------------------------

# ======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
# ======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
        #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
        #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret


# ======================
# Data structure design
# ======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        """

        :param guid: globally unique identifier (GUID) - a string
        :param title: a string
        :param description: a string
        :param link: link to more content - a string
        :param pubdate: a datetime
        """
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


# ======================
# Triggers
# ======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        """
        :param phrase:  a string
        """
        self.phrase = phrase

    def is_phrase_in(self, text):
        """

        :param text:  a string
        :return:  Return True when phrase is entirely in the text ,otherwise return False

        """
        # lowercase  phrase
        lowercase_phrase = self.phrase.lower()

        # 将text中的所有标点符号都替换为 " "
        for char in string.punctuation:
            text = text.replace(char, " ")

        # text 转为 list ,此步是为了去掉空格 ，具体参见help(str.split)
        word_list = text.lower().split()

        # 此步是将处理后的word_list 转为只含" "分隔的字符串
        text = " ".join(word_list)

        # 这种情况  'bee'   'bees'就是不行的 所以下面这个不对
        # return lowercase_phrase in text

        # 解决方案 可以用 'bee '判断是否是text子串,如果为True，那么返回True。
        # 否则判断bee 是否是text的结尾，既然如此，何不将text加一个空格呢?
        text += " "
        return (lowercase_phrase + " ") in text


# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        """

        :param story: a object of type NewsStory
        :return: Return True when phrase is in story's title,otherwise False
        """
        return self.is_phrase_in(story.get_title())


# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        """

        :param story: a object of type NewsStory
        :return: Return True when phrase is in story's description,otherwise False
        """
        return self.is_phrase_in(story.get_description())


# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, date_string):
        """
        :param time: time in EST as a string in the format of "3 Oct 2016 17:00:10"
                      也就是说3 Oct 2016 17:00:10 是一个EST格式的String

        """
        #  下面的time是  offset-aware datetimes 类型，即有时区， 这个是通过replace指定的
        self.time = datetime.strptime(date_string, "%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone("EST"))


# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        """

        :param story: a object of type NewsStory
        :return: return True when a story is published strictly before the trigger’s time
        """
        return self.time > story.get_pubdate()


class AfterTrigger(TimeTrigger):

    def evaluate(self, story):
        """
            :param story: a object of type NewsStory
            :return: return True when a story is published strictly after the trigger’s time
        """
        return self.time < story.get_pubdate()


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        """

        :param trigger:  a object of Type Trigger
        """
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)


# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)


# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)


# ======================
# Filtering
# ======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    # return stories
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered_stories.append(story)
                break
    return filtered_stories


# ======================
# User-Specified Triggers
# ======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """

    def create_trigger_by_config(config, dic):
        """

        :param config:创建一个Trigger的配置信息 ，类型为string 类似于't1,TITLE,election'。假设用户传的配置是有效的
        :param dic : 存储trigger的字典
        :return: 分析config，返回新的dic
        """
        # ['t1','TITLE','election']
        config_list = config.split(',')
        # TITLE
        trigger_type = config_list[1]
        trigger = None
        if "TITLE" == trigger_type:
            trigger = TitleTrigger(config_list[2])
        elif "DESCRIPTION" == trigger_type:
            trigger = DescriptionTrigger(config_list[2])
        elif "AFTER" == trigger_type:
            trigger = AfterTrigger(config_list[2])
        elif "BEFORE" == trigger_type:
            trigger = BeforeTrigger(config_list[2])
        elif "NOT" == trigger_type:
            trigger = NotTrigger(dic[config_list[2]])
        elif "AND" == trigger_type:
            tmp_1 = dic[config_list[2]]
            tmp_2 = dic[config_list[3]]
            trigger = AndTrigger(tmp_1, tmp_2)
        elif "OR" == trigger_type:
            trigger = OrTrigger(dic[config_list[2], dic[config_list[3]]])

        dic[config_list[0]] = trigger

        return dic

    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    # print(lines)  # for now, print it so you see what it contains!
    dic = {}
    add_line = ""
    for line in lines:
        if not line.startswith("ADD"):
            dic = create_trigger_by_config(line, dic)
        else:
            add_line = line
            break

    # 分析add_line
    trigger_to_be_added_list_str = add_line.split(",")
    trigger_to_be_added_list = []
    for key in trigger_to_be_added_list_str[1:]:
        trigger_to_be_added_list.append(dic[key])

    return trigger_to_be_added_list


SLEEPTIME = 10  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # hard code
        # t1 = TitleTrigger("election")
        # t2 = DescriptionTrigger("Trump")
        # t3 = DescriptionTrigger("Clinton")
        # t4 = AndTrigger(t2, t3)
        # t5 = TitleTrigger("biden")
        # t6 = DescriptionTrigger("Covid-19")
        # triggerlist = [t1,t5,t6]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title() + "\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:
            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
