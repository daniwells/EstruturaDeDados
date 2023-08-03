from aulas.node import Node

class Queue:
    def __init__(self):
       self.first =  None
       self.last = None
       self._size = 0

    def push(self, elem):
        #insere um elemento
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size += 1

    def pop(self):
        # remove o primeiro elemento
        if self.first is not None:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem
        else:
            raise IndexError("the queue is empty!")

    def peek(self):
        # retorna o ultimo elemento
        if self.first is not None:
            return self.first.data
        else:
            raise IndexError("the queue is empty!")

    def __len__(self):
        """
        :return: Retorna o tamanho da lista encadeada
        """
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            point = self.first

            while point:
                r = r + str(point.data) + ' '

                point = point.next

            return r
        else:
            return "The queue is empty!"

    def __str__(self):
        return self.__repr__