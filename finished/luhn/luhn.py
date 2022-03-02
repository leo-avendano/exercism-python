class Luhn:
    def __init__(self, card_num):
        card_num = card_num.replace(' ', '')
        self.luhn_number = 0
        if len(card_num) > 1 and card_num.isnumeric():
            for index, number_str in enumerate(card_num[::-1]):
                number = int(number_str)
                if index % 2 == 0:
                    self.luhn_number += number
                else:
                    if number * 2 < 10:
                        self.luhn_number += number * 2
                    else:
                        self.luhn_number += (number * 2) - 9
        else:
            self.luhn_number = -1

    def valid(self):
        return self.luhn_number % 10 == 0
