import re


def count_words(sentence):
    words = re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower())
    counter = dict()
    for word in words:
        if counter.get(word) != None:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter
