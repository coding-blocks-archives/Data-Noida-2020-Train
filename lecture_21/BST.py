class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1


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

            node.height = max(BST.height(node.left), BST.height(node.right)) + 1

        return node

    @staticmethod
    def height(node):

        if node == None:
            return 0
        else:
            return node.height


    def display(self):
        self.__display(self.root)


    def __display(self, node, indent="", position="root"):

        if node == None:
            return

        print(indent, node.value, position, node.height)
        self.__display(node.left, indent+"\t", "left")
        self.__display(node.right, indent+"\t", "right")


