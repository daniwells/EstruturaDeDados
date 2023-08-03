class Node:
    def __init__(self, name, link):
        self.name = name
        self.link = link
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, name, link):
        node = Node(name, link)
        if self.head is None:
            self.head = node
        else:
            point = self.head
            while point. next is not None:
                point = point.next

            point.next = node

        self._size += 1

    def index(self, name):
        if self.head is None:
            raise IndexError('Sorry. The list is empty!')
        else:
            point = self.head
            while point:
                if point.name == name:
                    print(f'{point.name}: {point.link}')
                    break
                point = point.next
            else:
                raise ValueError(f'The site "{name}" not in list.')


list = LinkedList()

list.append('youtube', 'https://www.youtube.com/')
list.append('roadmap', 'https://roadmap.sh/')
list.append('pudim', 'http://www.pudim.com.br/')

list.index('pudim')