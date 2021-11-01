from itertools import groupby
_inp = '1222311'
print(*[(len(list(c)), int(k)) for k, c in groupby(_inp)])