from aulas.fila import Queue
import random

root = 'root'

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = TreeNode(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        #percurso em ordem simétrica
        if node is None:
            node = self.root

        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    def inorder_traversal(self, node=None):
        #percurso em ordem simétrica
        if node is None:
            node = self.root

        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)

        print(node, end='')

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)

        if node.right:
            hright = self.height(node.right)

        if hright > hleft:
            return hright + 1
        return hleft + 1

    def levelorder_traversal(self, node=root):
        if node == root:
            node = self.root
        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)

            if node.right:
                queue.push(node.right)
            print(node, end=" ")

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = TreeNode(value)
        elif value < parent.data:
            parent.left = TreeNode(value)
        else:
            parent.right = TreeNode(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def min(self, node=root):
        if node == root:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=root):
        if node == root:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node=root):
        if node == root:
            node = self.root

        if node is None:
            return node

        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                subst = self.min(node.right)
                node.data = subst
                node.right = self.remove(subst, node.right)

        return node

list = [34, 56, 32, 76, 877, 12, 4, 0, 90, 45, 491, 65]
tree = BinarySearchTree()

for e in list:
    tree.insert(e)

print(tree.max())
print(tree.min())

tree.inorder_traversal()

tree.remove(90)
print()
tree.inorder_traversal()
############################################
"""
vlist = [34, 56, 32, 76, 877, 12, 4, 0, 90, 45, 491, 65]

tree = BinarySearchTree()

for v in vlist:
    tree.insert(v)

bst = tree
bst.inorder_traversal()
print()
print('-' * 20)
bst.levelorder_traversal()

"""

############################################

"""def search(self, value, node=0):
    if node == 0:
        node = self.root
    if node is None or node.data == value:
        return BinarySearchTree(node)
    if value < node.data:
        return self.search(value, node.left)
    return self.search(node.right)"""

#############################################
"""
random.seed(77)

values = random.sample(range(1, 100), 42)

bst = BinarySearchTree()

for v in values:
    bst.insert(v)

items = [1, 3, 54, 12, 67, 1000]
for i in items:
    r = bst.search(i)
    if r is None:
        print(i, 'não encontrado')
    else:
        print(r.root.data, 'encontrado')
"""

#########################################

"""
tree = BinaryTree()

n1 = TreeNode('I')
n2 = TreeNode('N')
n3 = TreeNode('S')
n4 = TreeNode('C')
n5 = TreeNode('R')
n6 = TreeNode('E')
n7 = TreeNode('V')
n8 = TreeNode('A')
n85 = TreeNode('-')
n9 = TreeNode('5')
n0 = TreeNode('3')

n0.left = n6
n0.right = n9
n6.left = n1
n6.right = n5
n5.left = n2
n5.right = n4
n4.right = n3
n9.right = n85
n85.right = n8
n8.right = n7

tree.root = n0
tree.postorder_traversal()
print()
print(tree.height())
"""
#########################################

"""tree = BinaryTree()
n1 = TreeNode('a')
n2 = TreeNode('+')
n3 = TreeNode('*')
n4 = TreeNode('b')
n5 = TreeNode('-')
n6 = TreeNode('/')
n7 = TreeNode('c')
n8 = TreeNode('d')
n9 = TreeNode('e')

n6.left = n7
n6.right = n8
n5.left = n6
n5.right = n9
n3.left = n4
n3.right = n5
n2.left = n1
n2.right = n3

tree.root = n2

tree.simetric_traversal()
"""

###################################################

"""tree = BinaryTree(7)
tree.root.left = TreeNode(14)
tree.root.right = TreeNode(0)

print(tree.root)
print(tree.root.left)
print(tree.root.right)"""