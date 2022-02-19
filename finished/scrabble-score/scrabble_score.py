LETTER_SCORES = {
    "AEIOULNRST": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10
}

scores = {}
for letters, points in LETTER_SCORES.items():
    scores.update({letter: points for letter in letters})


def score(word):
    return sum(scores.get(letter) for letter in word.upper())
