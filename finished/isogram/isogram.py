IGNORED_CHARACTERS = [' ', '-']


def is_isogram(string):
    previous_letters = set()
    for letter in string.lower():
        if letter in previous_letters:
            return False
        elif not letter in IGNORED_CHARACTERS:
            previous_letters.add(letter)
    return True
