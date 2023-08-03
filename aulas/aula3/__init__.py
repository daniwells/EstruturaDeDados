from aulas.node import Node

#sequencial = []
#sequencial.append(10)

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            point = self.head
            while(point.next):
                point = point.next
            Node(elem)
            point.next = Node(elem)
        else:
            self.head = Node(elem)

        self._size += 1

    def __len__(self):
        """
        :return: Retorna o tamanho da lista encadeada
        """
        return self._size

    def _getnode(self, index):
        point = self.head
        for i in range(0, index):
            if point:
                point = point.next
            else:
                raise IndexError('list index out of range')
        return point

    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        point = self._getnode(index)


        if (point):
            return point.data
        else:
            raise IndexError('list index out of range')

    def __setitem__(self, index, elem):

        point = self._getnode(index)

        if (point):
            point.data = elem
        else:
            raise IndexError('list index out of range')

    def index(self, data):
        """
        :param data: Elemento que você busca na lista
        :return: Retorna o indice do element na lista
        """
        point = self.head
        i = 0
        while (point):

            if point.data == data:
                return i
            else:
                point = point.next
                i += 1
        else:
            raise ValueError(f"{data} is not in list!")

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        elif index == -1:
            point = self._getnode(self._size - 1)
            node.next = point.next
            point.next = node
        else:
            point = self._getnode(index - 1)
            node.next = point.next
            point.next = node
        self._size += 1

    def remove(self, elem):
        if self.head == None:
            raise ValueError(f"{elem} is not in list")
        elif elem == self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            point = self.head.next
            while point:
                if point.data == elem:
                    ancestor.next = point.next
                    point.next = None

                ancestor = point
                point = point.next
            self._size -= 1
            return True

    def __repr__(self):
        r = ""
        point = self.head

        while point:
            r = r + str(point.data) + '->'

            point = point.next

        return r

    def __str__(self):
        return self.__repr__


