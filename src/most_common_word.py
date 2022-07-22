#   find the most frequently appearing word, excluding the banned word in a given string
import collections
import re

def word_count(given_list, word):
    counter = 0
    for a in given_list:
        if a == word:
            counter += 1
    return counter

def common_word_with_banned_word1(banned, s):
    s = s.replace(",", "")
    sentence = s.split()
    sentence1 = []
    #   remove the banned word
    for i in sentence:
        if i == banned:
            sentence.remove(i)
    #   find the most common word
    max = ''
    max_counter = 0
    for i in sentence:
        crr = word_count(sentence, i)
        if crr > max_counter:
            max_counter = crr
            max = i
    return max

def common_word_with_banned_word2(banned, s):
    #   cleanse the given sentence
    words = [word for word in re.sub(r'[^\w]', ' ', s).lower().split() if word not in banned]
    counter = collections.defaultdict(int)
    #   loop the dic by the word
    for word in words:
        counter[word] += 1
    return max(counter, key=counter.get())
    


if '__main__' == __name__:
    s = 'bob hit a ball, the hit ball flew far after it was hit'
    banned = 'hit'
    common = common_word_with_banned_word1(banned, s)
    print(common)
