def is_triangle(sides):
    if len(sides) > 3:
        return False
    if (sides[0] + sides[1]) < sides[2]:
        return False
    if (sides[0] + sides[2]) < sides[1]:
        return False
    if (sides[1] + sides[2]) < sides[0]:
        return False
    if 0 in sides:
        return False
    return True


def equilateral(sides):
    if is_triangle(sides):
        if sides[0] == sides[1] == sides[2]:
            return True
        else:
            return False
    return False


def isosceles(sides):
    if is_triangle(sides):
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            return True
        else:
            return False
    return False


def scalene(sides):
    if is_triangle(sides):
        if sides[0] != sides[1] != sides[2]:
            return True
        else:
            return False
    return False
