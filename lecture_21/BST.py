class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:

    def __init__(self):
        self.root = None

    def add(self, value):
        self.root = self.__add(value, self.root)

    def __add(self, value, node):

        if node == None:
            node = Node(value)
        else:
            if node.value > value:
                node.left = self.__add(value, node.left)
            if node.value < value:
                node.right = self.__add(value, node.right)

        return node


    def display(self):
        self.__display(self.root)


    def __display(self, node, indent="", position="root"):

        if node == None:
            return

        print(indent, node.value, position)
        self.__display(node.left, indent+"\t", "left")
        self.__display(node.right, indent+"\t", "right")


