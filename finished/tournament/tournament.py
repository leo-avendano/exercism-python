INITIAL_RESULTS = {
    'played': 0,
    'won': 0,
    'lost': 0,
    'drawn': 0,
    'points': 0
}


def add_win(results, team):
    results[team]['played'] += 1
    results[team]['won'] += 1
    results[team]['points'] += 3
    return results


def add_loss(results, team):
    results[team]['played'] += 1
    results[team]['lost'] += 1
    return results


def add_draw(results, team):
    results[team]['played'] += 1
    results[team]['drawn'] += 1
    results[team]['points'] += 1
    return results


def order_teams(results):
    results_list = sorted(
        ((results[team]['points'], team, results[team]) for team in results),
        key=lambda k: (-k[0], k[1])
    )
    return results_list


def show_table(results_list):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    for team in results_list:
        name = team[1].ljust(30)
        mp = str(team[2]['played']).rjust(2)
        w = str(team[2]['won']).rjust(2)
        d = str(team[2]['drawn']).rjust(2)
        l = str(team[2]['lost']).rjust(2)
        p = str(team[0]).rjust(2)
        table.append(f'{name} | {mp} | {w} | {d} | {l} | {p}')
    return table


def tally(rows):
    results = {}
    for row in rows:
        home, visitor, result = row.split(';')
        if home not in results:
            results[home] = INITIAL_RESULTS.copy()
        if visitor not in results:
            results[visitor] = INITIAL_RESULTS.copy()

        if result == 'win':
            results = add_win(results, home)
            results = add_loss(results, visitor)
        elif result == 'loss':
            results = add_loss(results, home)
            results = add_win(results, visitor)
        elif result == 'draw':
            results = add_draw(results, home)
            results = add_draw(results, visitor)

    results_list = order_teams(results)
    return show_table(results_list)
