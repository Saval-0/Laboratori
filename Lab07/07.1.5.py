# 07.1.5 Gli stessi elementi. 
# Scrivere la funzione same_set(a, b) che verifichi se due liste
# contengono gli stessi elementi, indipendentemente dall’ordine e ignorando la presenza di duplicati.
# Ad esempio, le due liste 1 4 9 16 9 7 4 9 11 e 11 11 7 9 16 4 1 devono essere
# considerate uguali. La funzione non deve modificare le liste che sono state passate come parametri.
# [P6.12]

import random

def main():
    one = [ 1, 4, 9, 16, 9, 7, 4, 9, 11 ]
    two = [ 11, 11, 7, 9, 16, 4, 1, 1, 3 ]
    # two = [ 11, 11, 7, 9, 16, 4, 1 ]

    if same_set(one, two):
        print("Le liste sono uguali.")
    else:
        print("Le liste sono diverse.")

    return

def same_set(a, b):
    dicA = {key: None for key in a}
    dicB = {key: None for key in b}

    print(dicA)
    print(dicB)

    for value in a:
        if value not in b:
            return False

    for value in b:
        if value not in a:
            return False

    return True


main()