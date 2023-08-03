from exercicios.node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert0(self, elem):
        node = Node(elem)

        node.next = self.head
        self.head = node

        self._size += 1

    def append(self, elem):
        node = Node(elem)
        if self.head is None:
            node.next = self.head
            self.head = node
        else:
            point = self.head
            while point.next is not None:
                point = point.next

            point.next = node

        self._size += 1

    def insert(self, index, elem):
        node = Node(elem)
        if self.head is None:
            node.next = self.head
            self.head = node
        else:
            point = self.head

            if index <= self._size:

                for e in range(0, index - 1):
                    point = point.next

                node.next = point.next
                point.next = node


            else:
                raise IndexError('list index out of range')

    def index(self, elem):
        if self.head is None:
            raise IndexError("the list is empty!")
        else:
            point = self.head
            cont = 0

            while point:
                point = point.next
                cont += 1

                if point.data == elem:
                    return f'{elem} is in position {cont}'
            else:
                raise ValueError(f"{elem} is not in list!")

    def remove(self, elem):
        if self.head is None:
            raise IndexError("the list is empty!")
        else:
            point = self.head
            point2 = self.head
            cont = 0

            while point:
                point2 = point
                point = point.next
                cont += 1

                if point.data == elem:
                    point2.next = point.next
                    break
            else:
                raise ValueError(f"{elem} is not in list!")

    def del0(self):
        if self.head is None:
            raise IndexError("the list is empty!")
        else:
            vr = self.head
            self.head = self.head.next
            return vr.data

    def pop(self):
        if self.head is None:
            raise IndexError("the list is empty!")
        else:
            point = self.head
            point2 = self.head

            while point.next is not None:
                point2 = point
                point = point.next

            point2.next = None
            return point.data


    def __repr__(self):
        r = ""
        point = self.head

        while point:
            r = r + str(point.data) + '->'

            point = point.next

        return r

    def __str__(self):
        return self.__repr__

"""

from exercicios.linkedlist import LinkedList
list = LinkedList()
list.insert(0, 2)
list.append(3)
list.append(4)
list.append(7)
list.append(10)
list.insert(2, 45)
list.remove(45)
list.del0()

"""