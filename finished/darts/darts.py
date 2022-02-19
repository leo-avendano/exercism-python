from multiprocessing.sharedctypes import Value


OUTER_RADIUS = 10
MIDDLE_RADIUS = 5
INNER_RADIUS = 1


def score(x, y):
    distance = (x ** 2 + y ** 2) ** (1/2)
    print(distance)
    if distance > OUTER_RADIUS:
        return 0
    elif distance > MIDDLE_RADIUS:
        return 1
    elif distance > INNER_RADIUS:
        return 5
    elif distance <= INNER_RADIUS:
        return 10
    raise ValueError('Input values out of range')
