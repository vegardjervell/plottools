def mix_2_name(id_tuple):
    if type(id_tuple[0]) is list:
        id_tuple = id_tuple[0]
    if type(id_tuple) is str:
        id_tuple = id_tuple.split(',')

    id_2_name_map = {'D2': r'D${_2}$', 'H2': r'H${_2}$', 'HE': 'He', 'NE': 'Ne', 'O2': r'O${_2}$', 'CO2': r'CO${_2}$',
                 'N2': r'N${_2}$', 'AR': 'Ar', 'C1': r'CH${_4}$', 'KR' : 'Kr', 'XE' : 'Xe'}

    if len(id_tuple) == 1:
        return id_2_name_map[id_tuple[0]]
    return '/'.join([id_2_name_map[id] for id in id_tuple])

def unit(u, pre=0):
    # pre: prefactor 10^pre
    # u : unit type
    if u == 'cond':
        u = r'W m$^{-1}$ K$^{-1}$'
    elif u == 'visc':
        u = r'Pa s'
    elif u == 'diff':
        u = r'm$^2$ s$^{-1}$'
    else:
        raise KeyError('Invalid unit type ' + str(u))

    if pre == -6:
        pre = r'$\mu$'
    elif pre == -3:
        pre = 'm'
    elif pre == -2:
        pre = 'c'
    elif pre == 0:
        pre = ''
    elif pre == 3:
        pre = 'k'
    elif pre == 6:
        pre = 'M'
    else:
        pre = r'$10^{' + str(pre) + '}$ '

    return '[' + pre + u + ']'