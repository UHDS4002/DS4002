
# Recursive Functions
from typing import Optional, List


def sum_recursive(a: int, b: int) -> int:
    if b == 0:
        return a
    return sum_recursive(a, b-1) + 1


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next: Optional[Node] = None


def search(node: Node, key):
    if node is None:
        return False
    if node.key == key:
        return node.data
    return search(node.next, key)


class Hanoi:
    class Disk:
        def __init__(self, size: int):
            self.size = size

        def __str__(self):
            return f'Disk{self.size}'
        __repr__ = __str__

    class Tower:
        def __init__(self, name):
            self.arr: List[Hanoi.Disk] = []
            self.name = name

        def push(self, disk: "Hanoi.Disk"):
            if self.arr and self.arr[-1].size <= disk.size:
                raise ValueError(f"Append Disk {disk.size} on {self.arr[-1].size},"
                                 f" Tower: {self.name}")
            self.arr.append(disk)

        def pop(self) -> "Hanoi.Disk":
            return self.arr.pop()

        def __len__(self):
            return len(self.arr)

        def __str__(self):
            return str(self.arr)
        __repr__ = __str__

    def __init__(self, size: 3):
        self.a = Hanoi.Tower("A")
        for i in range(size, 0, -1):
            self.a.push(Hanoi.Disk(i))
        self.b = Hanoi.Tower("B")
        self.c = Hanoi.Tower("C")

    def move(self, tower1: "Hanoi.Tower", tower2: "Hanoi.Tower",
             tower3: "Hanoi.Tower", count: int):
        if count == 0:
            return
        self.move(tower1, tower3, tower2, count - 1)
        disk = tower1.pop()
        tower2.push(disk)
        self.move(tower3, tower2, tower1, count - 1)


if __name__ == '__main__':
    head = Node(97, "Esmail")
    t = head
    for index, name in enumerate(["Ali", "Reza", "Hassan"]):
        t.next = Node(index, name)
        t = t.next
