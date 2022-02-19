def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[:3]


scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
expected = [100, 90, 70]
print(personal_top_three(scores))
