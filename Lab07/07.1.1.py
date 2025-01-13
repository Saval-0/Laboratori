# 07.1.1 Somma a segni alterni. Scrivere un programma che riceva in input una sequenza di numeri
# interi (terminata da una riga vuota), e che calcoli la somma alternata dei suoi elementi. Ad esempio,
# se il programma legge i dati 1 4 9 16 9 7 4 9 11, deve calcolare e visualizzare 1 – 4 + 9 –
# 16 + 9 – 7 + 4 – 9 + 11 = –2.

def main():
    values = []
    input_str = input("Enter values (blank line to quit): ")
    while input_str != "":
        values.append(float(input_str))
        input_str = input("Enter values (blank line to quit): ")
    
    total = 0
    for i in range(len(values)):
        if (i % 2) == 0:
            total += values[i]
        else:
            total -= values[i]

    print("Somma alternata: " + str(total))
    return

main()