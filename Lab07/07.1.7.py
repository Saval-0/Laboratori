# 07.1.7 Somma senza il minimo. 
# Scrivere la funzione sum_without_smallest(v) che calcoli la
# somma di tutti i valori di una lista v, escludendo il valore minimo. [P6.6]

import random

def main():
    elms = gen_rand_list(10, 0, 100)
    print(elms)
    print(sum_without_smallest(elms))
    return


def gen_rand_list(num_el, bot_range, top_range):
    rand_list = []
    for i in range(num_el):
        rand_list.append(random.randint(bot_range, top_range))
    return rand_list


def sum_without_smallest(v):
    v.sort()
    return v[:len(v) - 1]


main()