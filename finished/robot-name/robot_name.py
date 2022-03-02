import random
import string


def random_letters(amount):
    letters = ''
    for _ in range(amount):
        letters += random.choice(string.ascii_uppercase)
    return letters


def random_numbers(amount):
    numbers = ''
    for _ in range(amount):
        numbers += str(random.choice(range(10)))
    return numbers


def random_robotname():
    return random_letters(2) + random_numbers(3)


class Robot:
    existing_names = []

    def __init__(self):
        self.name = random_robotname()
        while self.name in Robot.existing_names:
            self.name = random_robotname()
        Robot.existing_names.append(self.name)

    def reset(self):
        previous_name = self.name
        self.name = random_robotname()
        while self.name in Robot.existing_names:
            self.name = random_robotname()
        Robot.existing_names.remove(previous_name)
