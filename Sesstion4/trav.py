from Sesstion4 import Node, sample


def iterative_traverse(head: Node):
    temp = head
    while temp is not None:
        print(temp.data, end=" - ")
        temp = temp.next


def recursive_traverse(head: Node):
    if head is None:
        return
    print(head.data, end=" - ")
    recursive_traverse(head.next)


if __name__ == '__main__':
    print("Iter:")
    iterative_traverse(sample.head)
    print("\nRec:")
    recursive_traverse(sample.head)
