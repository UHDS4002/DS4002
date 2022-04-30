from typing import Optional


class Node:
    def __init__(self, value):
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BST:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, value: int):
        new = Node(value)
        if not self.root:
            self.root = new
            return
        t = self.root
        while True:
            if value > t.value:
                if not t.right:
                    t.right = new
                    return
                t = t.right
            else:
                if not t.left:
                    t.left = new
                    return
                t = t.left

    def sorted(self, root: Node = 10):
        # this method prints in order traversal
        if root == 10:
            root = self.root
        if not root:
            return
        self.sorted(root.left)  # this prints lefts
        print(root.value)
        self.sorted(root.right)


class BSTNode:
    def __init__(self, value: int):
        self.value = value
        self.right: Optional[BSTNode] = None
        self.left: Optional[BSTNode] = None

    def insert(self, value: int):
        if value > self.value:
            if not self.right:
                self.right = BSTNode(value)
                return
            self.right.insert(value)
        elif value < self.value:
            if not self.left:
                self.left = BSTNode(value)
                return
            self.left.insert(value)
        else:
            raise ValueError("How do you want me to add repetitive elements in BST??")

    def sorted(self):
        if self.left:
            self.left.sorted()
        print(self.value)
        if self.right:
            self.right.sorted()


if __name__ == '__main__':
    my_bst = BSTNode(10)
    for i in [36, 15, 30, 2, 17]:
        my_bst.insert(i)
    my_bst.sorted()

    bst = BST()
    bst.insert(10)
    bst.insert(8)
    bst.insert(7)
    bst.insert(9)
    bst.insert(15)
    bst.insert(14)
    bst.sorted()

