DAYS = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth')
GIFTS = ('a Partridge', 'two Turtle Doves',
         'three French Hens', 'four Calling Birds', 'five Gold Rings', 'six Geese-a-Laying', 'seven Swans-a-Swimming', 'eight Maids-a-Milking', 'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming')


def recite(start_verse, end_verse):
    if (start_verse > end_verse):
        raise ValueError(
            'The starting verse must be lower than the ending verse.')
    if (end_verse > 12):
        raise ValueError('There are only 12 verses.')
    if (start_verse < 1):
        raise ValueError('Verse must at least start at 1.')

    start_verse_offseted = start_verse - 1
    total_verses = end_verse - start_verse_offseted
    output = list()
    for verse in range(total_verses):
        curr_verse = start_verse_offseted + verse
        day_number = DAYS[curr_verse]
        gifts = ', '.join(GIFTS[curr_verse:0:-1]) + \
            f', and {GIFTS[0]}' if curr_verse > 0 else GIFTS[0]
        output.append(
            f'On the {day_number} day of Christmas my true love gave to me: {gifts} in a Pear Tree.')
    return output
