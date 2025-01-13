# 07.1.4 Massimi locali. Leggere una sequenza di numeri interi conclusa da una riga vuota. Stampare
# la posizione dei massimi locali (numeri maggiori sia del valore precedente che di quello successivo)
# se ce ne sono, altrimenti stampare il messaggio 'Non ci sono massimi locali'.
# Estensione: se sono presenti più coppie di massimi locali, individuare i due massimi locali più vicini
# fra loro e stampare la loro posizione.

def main():
    vals = []
    locMaxes = []
    in_str = input("Ins num (stop con vuoto): ")
    while in_str != "":
        vals.append(float(in_str))
        in_str = input("Ins num (stop con vuoto): ")
    
    for i in range(len(vals) - 1):
        if i == 0 and vals[i] > vals[i + 1]:
            locMaxes.append([ vals[0], 0 ])
        elif i == (len(vals) - 1) and vals[i] > vals[i - 1]:
            locMaxes.append([ vals[len(vals) - 1], len(vals) - 1 ])
        elif vals[i] > vals[i + 1] and vals[i] > vals[i - 1]:
            locMaxes.append([ vals[i], i ])

    if len(locMaxes) == 0:
        print("Non ci sono massimi locali")
    elif len(locMaxes) == 1 or len(locMaxes) == 2:
        print("Massimi locali: ")
        for el in locMaxes:
            print(" - " + str(el[0]))
    else:
        print("Massimi locali: ")
        for el in locMaxes:
            print(" - " + str(el[0]))

        minDist = [ abs(locMaxes[0][0] - locMaxes[1][0]), [0, 1] ]
        for i in range(1, len(locMaxes) - 1):
            dist = abs(locMaxes[i][0] - locMaxes[i + 1][0])
            if dist < minDist[0]:
                minDist[0] = dist
                minDist[1] = [ i, i + 1 ]

        print("I due massimi locali più vicini sono alle posizioni " + str(locMaxes[minDist[1][0]][1]) + " e " + str(locMaxes[minDist[1][1]][1]) + " (partendo da 0)")
    return

main()