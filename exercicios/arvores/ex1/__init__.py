from exercicios.filas.queue import Takeoff_Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data, n=None):
        if n == None:
            n = self.root
        if self.root == None:
            self.root = Node(data)
        else:
            node = Node(data)
            if data < n.data:
                if n.left != None:
                    n = self.insert(data, n.left)
                    return n
            elif data > n.data:
                if n.right != None:
                    n = self.insert(data, n.right)
                    return n

            if data > n.data:
                n.right = node
                return n.right
            elif data < n.data:
                n.left = node
                return n.left

    def search(self, value):
        return self._search(value)

    def _search(self, value, point=None):
        if self.root == None:
            raise IndexError('The tree is empty!')
        else:
            if point == None:
                point = self.root

            if value < point.data:
                if point.left != None:
                    point = self._search(value, point.left)
                if point == f'The value {value} not in list!':
                    return f'The value {value} not in list!'

            if value > point.data:
                if point.right != None:
                    point = self._search(value, point.right)
                if point == f'The value {value} not in list!':
                    return f'The value {value} not in list!'

            if value == point.data:
                return point
            else:
                return f'The value {value} not in list!'

    def inorder(self, point=None):
        if point is None:
            point = self.root

        if point.left:
            self.inorder(point.left)
        print(point, end=' ')
        if point.right:
            self.inorder(point.right)

    def posOrder(self, point=None):
        if point == None:
            point = self.root

        if point.left:
            self.posOrder(point.left)

        if point.right:
            self.posOrder(point.right)

        print(point, end=' ')

    def levelOrder(self, point=None):
        if point == None:
            point = self.root

        q = Takeoff_Queue()
        q.enqueue(point)

        while len(q):
            point = q.dequeue()
            if point.left:
                q.enqueue(point.left)

            if point.right:
                q.enqueue(point.right)

            print(point, end=' ')





tree = BinarySearchTree()

tree.insert(35)
tree.insert(32)
tree.insert(45)
tree.insert(33)
tree.insert(2)
tree.insert(97)
tree.insert(43)
tree.insert(1)

print(tree.root.right)
print(tree.root.left)
print(tree.root.left.right)
print(tree.root.left.left)
print(tree.root.left.left.left)


#print(tree.search(45))
"""
tree.inorder()
print()
tree.posOrder()
print()
tree.levelOrder()"""

"""
print(tree.root)
print(tree.root.left)
print(tree.root.left.right)
print(tree.root.right)
f'The value {value} is in position {cont}°.'
f'The value {value} not in list...'
"""