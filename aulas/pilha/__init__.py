from aulas.node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        #insere um elemento

        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1


    def pop(self):
        # remove o último elemento
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        else:
            raise IndexError("the stack is empty")

    def peek(self):
        # retorna o ultimo elemento
        if self._size > 0:
            return self.top.data
        else:
            raise IndexError("the stack is empty")

    def __len__(self):
        """
        :return: Retorna o tamanho da lista encadeada
        """
        return self._size

    def __repr__(self):
        r = ""
        point = self.top

        while point:
            r = r + str(point.data) + '\n'

            point = point.next

        return r

    def __str__(self):
        return self.__repr__
