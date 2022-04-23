from typing import Optional


class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next: Node = next_

    def __repr__(self):
        return f"(Node:{self.data}, next: {self.next.data if self.next else 'None'})"


class SLL:
    def __init__(self):
        self.head: Optional[Node] = None

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)

    def __str__(self):
        t = self.head
        x = []
        while t:
            x.append(t.data)
            t = t.next
        return f"[{','.join(str(e) for e in x)}]"


sample = SLL()
for i in range(5, 0, -1):
    sample.prepend(i)

