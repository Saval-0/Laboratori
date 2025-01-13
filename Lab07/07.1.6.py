# 07.1.6 Lista ordinata. 
# Scrivere un programma che generi una sequenza di 20 valori interi casuali
# compresi tra 0 e 99, poi visualizzi la sequenza generata, la ordini e la visualizzi di nuovo, ordinata.
# Usate il metodo sort(). [P6.17]

import random

def main():
    elms = gen_rand_list()
    print(elms)

    elms.sort()
    print(elms)

    return

def gen_rand_list():
    rand_list = []
    for i in range(20):
        rand_list.append(random.randint(0, 99))
    return rand_list

main()