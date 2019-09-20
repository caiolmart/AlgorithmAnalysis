def next_strips(this_strip, n_left, previous_strip=None):
    next = []
    if this_strip == 'B':
        next.append('V')
        if n_left > 1:
            next.append('A')
    if this_strip == 'V':
        next.append('B')
        if n_left > 1:
            next.append('A')
    if this_strip == 'A':
        if previous_strip == 'B':
            next.append('V')
        elif previous_strip == 'V':
            next.append('B')
    return next

def n_next_strips(this_strip, n_left, previous_strip=None):
    n_next = 0
    if this_strip == 'B':
        n_next += 1
        if n_left > 1:
            n_next += 1
    if this_strip == 'V':
        n_next += 1
        if n_left > 1:
            n_next += 1
    if this_strip == 'A':
        if previous_strip == 'B':
            n_next += 1
        elif previous_strip == 'V':
            n_next += 1
    return n_next

def get_combinations(combination, n_left):
    if n_left == 0:
        print(combination)
    elif len(combination) > 1:
        nexts = next_strips(combination[-1], n_left, combination[-2])
        for next in nexts:
            aux = combination.copy()
            aux.append(next)
            get_combinations(aux, n_left - 1)
    elif len(combination) == 1:
        nexts = next_strips(combination[-1], n_left)
        for next in nexts:
            aux = combination.copy()
            aux.append(next)
            get_combinations(aux, n_left - 1)
    else:
        auxs = [['B'], ['V']]
        for aux in auxs:
            get_combinations(aux, n_left - 1)


def count_combinations(combination, n_left):
    n_combinations = 0
    if n_left == 0:
        return 1
    elif len(combination) > 1:
        nexts = next_strips(combination[-1], n_left, combination[-2])
        for next in nexts:
            aux = combination.copy()
            aux.append(next)
            n_combinations += count_combinations(aux, n_left - 1)
    elif len(combination) == 1:
        nexts = next_strips(combination[-1], n_left)
        for next in nexts:
            aux = combination.copy()
            aux.append(next)
            n_combinations += count_combinations(aux, n_left - 1)
    elif combination == []:
        auxs = [['B'], ['V']]
        for aux in auxs:
            n_combinations += count_combinations(aux, n_left - 1)
    return n_combinations
