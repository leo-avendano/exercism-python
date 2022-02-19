def leap_year(year):
    is_div_4 = year % 4 == 0
    is_div_100 = year % 100 == 0
    is_div_400 = year % 400 == 0

    if is_div_400 or (is_div_4 and not is_div_100):
        return True
    return False
