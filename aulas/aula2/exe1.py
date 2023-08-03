list = [5, 234, 8, 29, 67]

print(list[-1])
print(list[len(list) - 1])

def busca(list, e):
    """
    :param list: Lista que deseja realizar a função
    :param e: Elemento que deseja procurar na lista
    :return: Retorna a posição do elemento que deseja encontrar na lista ou None caso o elemento não esteja na lista.
    """
    if e in list:
        return list.index(e)
    else:
        return None

lists = [4, 67, 123, 2, 19, 57, 21]
list2 = busca(lists, 2)

if list2 is not None:
    print(f'O elemento {lists} foi encontrado na lista, a posição dele é {list2}.')
else:
    print('Não encontramos o elemento na lista.')