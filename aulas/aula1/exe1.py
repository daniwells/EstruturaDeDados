def inverter_lista(list):
    size = len(list)
    limit = size // 2
    for i in range(limit):
        aux = list[i]
        list[i] = list[n-i]
        list[size-i] = aux
    print(list)



