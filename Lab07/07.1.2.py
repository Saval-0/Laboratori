# 07.1.2 Lista di numeri casuali. Scrivere un programma che inizializzi una lista con dieci numeri interi
# casuali tra 1 e 100 e poi visualizzi, su quattro righe successive:
# I. Tutti gli elementi di indice pari;
# II. Tutti gli elementi di valore pari;
# III. Tutti gli elementi in ordine inverso;
# IV. Il primo e l’ultimo elemento.
import random

def main():
    i = 0
    numbers = []
    while i < 10:
        numbers.append(random.randint(1, 100))
        i += 1

    print("I. Tutti gli elementi di indice pari")
    i = 0
    while i < 10:
        if (i % 2) == 0:
            print(" - " + str(numbers[i]))
        i += 1

    print("II. Tutti gli elementi di valore pari")
    i = 0
    while i < 10:
        if (numbers[i] % 2) == 0:
            print(" - " + str(numbers[i]))
        i += 1

    print("III. Tutti gli elementi in ordine inverso")
    for el in numbers[::-1]:
        print(" - " + str(el))


    print("IV. Il primo e l'ultimo elemento")
    print(" - " + str(numbers[0]))
    print(" - " + str(numbers[-1]))
    
    return

main()