# 07.2.1 Rumore di misura. 
# Spesso i dati raccolti durante un esperimento vanno elaborati per
# rimuovere parte del rumore di misura. Un approccio semplice a questo problema prevede di
# sostituire, in una lista di valori, ciascun valore con la media tra il valore stesso e i due valori adiacenti
# (o dell’unico valore adiacente se il valore in esame si trova a una delle due estremità della lista).
# Scrivere un programma che svolga tale operazione, senza creare una seconda lista. [P6.36]

import random

def main():
    elms = gen_rand_list(10, 0, 100)
    print(elms)
    
    for i in range(len(elms) - 1):
        if i == 0:
            elms[i] = (elms[i] + elms[i + 1])/2
        elif len(elms) - 1:
            elms[i] = (elms[i] + elms[i - 1])/2
        else:
            elms[i] = (elms[i - 1] + elms[i] + elms[i - 1])/3

    print(elms)
    return


def gen_rand_list(num_el, bot_range, top_range):
    rand_list = []
    for i in range(num_el):
        rand_list.append(random.randint(bot_range, top_range))
    return rand_list


main()