from BST import BST
import random


tree = BST()

for item in range(30000):
    tree.add(item)

# tree.display()

print(tree.root.height)
