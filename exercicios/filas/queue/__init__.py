from exercicios.node import Node

class Takeoff_Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def enqueue(self, elem):
        node = Node(elem)
        if self.last is None:
            if self.first is None:
                self.first = node
                self._size += 1
            else:
                self.first.next = node
                self.last = node
                self._size += 1
        else:
            self.last.next = node
            self.last = node
            self._size += 1

    def dequeue(self):
        if self.first is None:
            raise IndexError('The list is empty!')
        else:
            c = self.first
            self.first = self.first.next
            self._size -= 1
            return c.data


    def repr_c(self):
        print('The first plane characteristics ->', end=' ')
        for i, e in self.first.data['caracteristicas'].items():
            print(f'\033[32m{i}\033[m : \033[32m{e}\033[m /', end=' ')

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        point = self.first

        while point:
            r = r + str(point.data['name']) + ' / '

            point = point.next

        return r

    def __str__(self):
        return self.__repr__()
"""
av1 = {'name':'Antonov An-124 Ruslan.', 'caracteristicas':{'cor':'azul', 'tamanho':'médio', 'velocidade':'rápido'}}
av2 = {'name':'Boeing 747-8 Freighter.', 'caracteristicas':{'cor':'vermelho', 'tamanho':'médio', 'velocidade':'rápido'}}
av3 = {'name':'Boeing 777-8 Freighter.', 'caracteristicas':{'cor':'amarelo', 'tamanho':'grande', 'velocidade':'lento'}}
av4 = {'name':'Boeing 747 Dreamlifter.', 'caracteristicas':{'cor':'roxo', 'tamanho':'pequeno', 'velocidade':'muito rápido'}}
av5 = {'name':'Airbus BelugaXL.', 'caracteristicas':{'cor':'branco', 'tamanho':'grande', 'velocidade':'rápido'}}

list = [av1, av2, av3, av4, av5]

planes = Takeoff_Queue()

for e in list:
    planes.enqueue(e)

print(planes.__repr__())
planes.repr_c()

print('\n')

planes.dequeue()
print(planes.__repr__())
"""