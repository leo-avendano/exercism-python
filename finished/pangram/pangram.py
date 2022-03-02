import re


def is_pangram(sentence):
    letters = set(re.findall(r'[a-z]', sentence.lower()))
    return len(letters) == 26
