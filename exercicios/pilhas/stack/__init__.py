from exercicios.node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.top_discard = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self.top_discard = self.top

    def pop(self):
        if self.top is None:
            raise IndexError("the list is empty!")
        else:
            self.top = self.top.next


    def undo(self):
        if self.top_discard != self.top:
            self.top_discard.next = self.top
            self.top = self.top_discard

    def __repr__(self):
        r = ""
        point = self.top

        while point:
            r = str(point.data) + ' ' + r

            point = point.next

        return r

    def __str__(self):
        return self.__repr__

sta = Stack()
while True:
    txt = str(input('Enter a text: '))

    if txt == '_stop':
        break
    else:
        if txt == 'ctrl+z':
            sta.pop()

        elif txt == 'ctrl+y':
            sta.undo()

        else:
            sta.push(txt)

        print(sta.__repr__())


print('END')





"""

from exercicios.stack import Stack
pilha = Stack()
pilha.push(2)
pilha.push(4)
pilha.push(22)
pilha.push(1)
pilha.pop()
pilha.push(43)
pilha.push(12)
pilha.pop()

"""