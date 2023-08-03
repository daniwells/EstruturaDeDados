from exercicios.node import Node

class OrdenedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert(self, elem):
        node = Node(elem)
        if self.head is None:
            self.head = node
            self._size += 1
        else:
            point = self.head

            while point is not None:
                if point.next is not None:
                    if point.data < node.data <= point.next.data:
                        node.next = point.next
                        point.next = node
                        self._size += 1
                        break
                elif node.data > point.data:
                    node.next = point.next
                    point.next = node
                    self._size += 1
                    break

                point = point.next

            else:
                node.next = self.head
                self.head = node
                self._size += 1

    def index(self, elem):
        if self.head is None:
            raise IndexError('The list is empty')
        else:
            point = self.head
            cont = 0
            while point:
                if elem == point.data:
                    return f"{point.data} is in list, and it's in position {cont}."
                cont += 1
                point = point.next
            else:
                raise ValueError(f'{elem} not in list!')

    def remove(self, elem):
        if self.head is None:
            raise IndexError('The list is empty')
        else:
            point = self.head

            if elem == point.data:
                self.head = point.next
                self._size -= 1
            else:
                while point:
                    point2 = point
                    point = point.next
                    if elem == point.data:
                        point2.next = point.next
                        self._size -= 1
                        return f'{elem} was deleted!'
                raise ValueError(f'{elem} not in list!')

    def copy(self, l1, l2):
        if l2.head is not None:
            point = l2.head
            while point:
                l1.insert(point.data)
                point = point.next

    def __repr__(self):
        r = ""
        point = self.head

        while point:
            r = r + str(point.data) + '->'

            point = point.next

        return r

    def __str__(self):
        return self.__repr__

list = OrdenedList()
list.insert(2)
list.insert(5)
list.insert(1)
list.insert(3)


print(list.__repr__())

list2 = OrdenedList()
list2.insert(4)
list2.insert(6)
list2.insert(0)

print(list2.__repr__())
list2.copy(list2, list)
print(list2.__repr__())
"""
list.copy(list,list2)
print(list.__repr__())
"""

"""
from exercicios.listas_encadeadas.ordenedlist import OrdenedList
list = OrdenedList()
list.insert(2)
list.insert(5)
list.insert(1)
list.insert(3)
list.remove(3)
"""