import unicodedata
from exercicios.node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        if self.top is None:
            self.top = node
            self._size += 1
        else:
            node.next = self.top
            self.top = node
            self._size += 1

    def pop(self):
        if self.top is None:
            raise IndexError('The stack is empty')
        else:
            self.top = self.top.next
            self._size -= 1

    def palindromo(self):
        r1 = ""
        r2 = ""
        point = self.top

        while point:
            r1 = r1 + str(point.data)
            r2 = str(point.data) + r2

            point = point.next

        if r1 == r2:
            return 'This phrase is a palíndromo'
        else:
            return 'This phrase not is a palíndromo'

    def __repr__(self):
        r = ""
        point = self.top

        while point:
            r = r + str(point.data)

            point = point.next

        return r

    def __str__(self):
        return self.__repr__()


txt = str(input('Enter a text: '))
pt = Stack()

process = unicodedata.normalize("NFD", txt)
process = process.encode("ascii", "ignore")
process = process.decode("utf-8")

for c in process:
    if c != ' ':
        pt.push(c)

print(pt.__repr__())
print(pt.palindromo())

"""
from exercicios.pilhas.ex2 import Stack
pilha = Stack()
pilha.push(2)

"""