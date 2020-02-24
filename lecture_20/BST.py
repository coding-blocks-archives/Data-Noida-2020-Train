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

    def contains(self, value):
        self.__contains(value, self.root)

    def __contains(self, value, node):

        if node == None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self.__contains(value, node.left)
        else:
            return self.__contains(value, node.right)

    def display(self):
        self.__display(self.root)

    def __display(self, node, indent="", position="root"):

        if node == None:
            return

        print(indent, node.value, position)
        self.__display(node.left, indent+"\t", "left")
        self.__display(node.right, indent+"\t", "right")

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if node == None:
            return 0

        left = self.__height(node.left)
        right = self.__height(node.right)

        return max(left, right) + 1


    def sum(self):
        return self.__sum(self.root)

    def __sum(self, node):
        if node == None:
            return 0

        left = self.__sum(node.left)
        right = self.__sum(node.right)

        return left + right + node.value

    def mirror(self):
        self.__mirror(self.root)

    def __mirror(self, node):
        if node == None:
            return

        temp = node.left
        node.left = node.right
        node.right = temp

        self.__mirror(node.left)
        self.__mirror(node.right)


if __name__ == "__main__":
    tree = BST()

    tree.add(20)

    tree.add(10)

    tree.add(30)

    tree.add(13)

    tree.display()

    tree.mirror()

    tree.display()

