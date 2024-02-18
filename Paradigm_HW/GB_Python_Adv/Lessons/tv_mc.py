from random import randint, shuffle
import random
from statistics import median


def create_mutl(n, a, b, pov=None, dr=0):
    if pov is None:
        pp = [1] * n
    else:
        pp = pov + [1] * (n - sum(pov))
    fl = 0
    while fl == 0:
        fl = 1
        ll = [i for i in range(a, b + 1)]
        li_r = []
        for i in pp:
            v = randint(0, len(ll) - 1)
            li_r += [ll.pop(v)] * i
        shuffle(li_r)
        if n % 2 == 1:
            med_f = li_r[int((n - 1) / 2 + 0.5)]
        else:
            med_f = (li_r[int(n / 2 + 0.5)] + li_r[int(n / 2 + 0.5) - 1]) / 2
            lir_rr = sorted(li_r)
            if lir_rr[int(n / 2 + 0.5)] == lir_rr[int(n / 2 + 0.5) - 1]:
                fl = 0
        med_t = median(li_r)
        mod = max(set(li_r), key=li_r.count)
        max_l = max(li_r)
        min_l = min(li_r)
        if med_t == med_f or med_t == mod or li_r[0] == min_l or li_r[-1] == max_l or sum(li_r)/n == int(sum(li_r)/n):
            fl = 0
        for i in range(n - 1):
            if li_r[i] == li_r[i + 1]:
                fl = 0
        print(li_r)
    if med_t == int(med_t):
        med_t = int(med_t)
    return li_r, med_t, mod, max_l - min_l, sum(li_r)/n

a, b, c, d, e = create_mutl(4, 3, 20, [1])
print(' '.join(map(str, a)))
print(b)
print(c)
print(d)
print(e)
l = [5, 4, 5, 12, 3]
l1 = sorted(l)
print(l1)