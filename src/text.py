# This file is for any kind of text manipulation method to display things 
# correctly on a screen, and to break up the monotony of white text black
# background.

import textwrap

from termcolor import colored

def ex(exit):
    # This method is for specifying exits in a room's
    # exit list.

    return colored(exit.upper(), "yellow")

def intr(entity):
    # This method colorizes any items of interest.

    return colored(entity, "light_cyan")

def title(title):
    # This method colors titles of screens. 
    return colored(title, "cyan")

def topic(topic):
    # This method colors keyword topics that are saved to the journal
    return colored(topic, "red")

def proper(full_name):
    # This method takes a lowercase string and capitalizes the right 
    # words based on g r a m m a r.

    full_name = full_name.split(' ')
    split_name = list()

    split_name.append(full_name.pop(0).capitalize())

    for word in full_name:
        if word in ["the", "to", "a", "an", "of"]: 
            split_name.append(word)
        else: 
            split_name.append(word.capitalize())

    return ' '.join(split_name)

def numstr(number):
    # This method will take a number and return a string. If the number is
    # less than eleven, it will return the word of the number.
    numwords = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
    if number in numwords.keys():
        return numwords[number]
    else: return str(number)

wrapper = textwrap.TextWrapper(width=118)

def wraptxt(txt):
    # This method takes textwrapper and wraps a long string.
    return wrapper.wrap(text=txt)

def swap_items(item1, item2):
    # This method takes two items and swaps their position. It can do this
    # with any item type, but its meant for swapping door objects with their
    # opened counterparts.
    cache = item2
    item2 = item1
    item1 = cache

    return item1, item2
