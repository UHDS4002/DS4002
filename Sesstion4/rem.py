from Sesstion4 import Node, sample


def remove(head: Node):
    t = head
    a = 0
    while t:
        # operation - we can see every node here.
        k = t
        prev = k
        while k and k.next:
            k = k.next
            if t.data == k.data:
                prev.next = k.next
            else:
                prev = k
        t = t.next


if __name__ == '__main__':
    sample.prepend(3)
    sample.prepend(3)
    sample.prepend(5)
    sample.prepend(3)
    print("Before:", sample)
    remove(sample.head)
    print("After:", sample)

