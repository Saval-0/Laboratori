# 07.1.3 Rimuovere il valore minimo. Scrivere una funzione remove_min(v) che rimuova il valore
# minimo da una lista v senza usare la funzione min() né il metodo remove(). 

import random
def main():
    # Create a list of random values.
    random_values = []
    for i in range(10):
        random_values.append(random.randint(0, 10))

    print(random_values)
    random_values = remove_min(random_values)
    print(random_values)
    return

def remove_min(v):
    smol_idx = 0
    smolst = v[0]

    for i in range(1, len(v)):
        if v[i] < smolst:
            smolst = v[i]
            smol_idx = i
    return v[:smol_idx] + v[smol_idx + 1:]

main()