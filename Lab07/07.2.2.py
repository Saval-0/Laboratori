# 07.2.2 Distanziamenti. Le persone che parcheggiano la propria automobile in una fila di parcheggi di
# solito preferiscono massimizzare la distanza tra il posto che occupano e i posti che sono già occupati
# da altri veicoli. Tendono quindi ad occupare il posto centrale della fila più lunga di posti liberi a
# disposizione.
# Ad esempio, si consideri la situazione in cui dieci posti sono liberi:
# _ _ _ _ _ _ _ _ _ _
# La prima persona che arriva occuperà, col proprio veicolo, un posto nella parte centrale della fila:
# _ _ _ _ _ X _ _ _ _
# La persona successiva lo posizionerà a metà della fila lasciata libera più lunga (cioè quella di sinistra):
# _ _ X _ _ X _ _ _ _
# Scrivere un programma che riceva in input il numero di posti auto di cui si compone la fila di
# parcheggi e che, ogni volta che un nuovo posto viene occupato secondo la regola indicata, visualizzi
# la fila nel formato indicato sopra. Suggerimento: utilizzare un elenco di valori booleani per indicare
# se un posto auto è occupato o meno. [P6.19]

def main():
    slots = [ False ] * 10
    car_num = 0

    print_park(slots)

    in_str = input("")
    while in_str == "":
        car_num += 1

        while False in slots:
            longest_length = 0
            longest_pos = 0

            for i in range(len(slots)):
                if not slots[i]:
                    current_length = 1

        
    return

def print_park(slots):
    for el in slots:
        if el:
            print("X", end='')
        else:
            print("_", end='')
    print("\n")
    return

main()