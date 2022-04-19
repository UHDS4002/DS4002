
def sum(a, b):
    for i in range(b):
        a += 1
    return a


def recursive_sum(a, b):
    if b == 0:
        return a
    return recursive_sum(a, b-1) + 1


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
head = Node(10,"esmaeil")
t1 = Node(12,"melika")
head.next = t1
for key,value in [(11,"hassan"),(14,"ali"),(15,"reza")]:
    a = Node(key,value)
    t1.next = a
    t1 = a
def search(head,key):
    temp = head
    while temp:
        if temp.key == key:
            return temp.value
        temp = temp.next
def recursive_search(head,key):
    if head is None:
        return False
    if head.key == key:
        return head.value
    return recursive_search(head.next,key)
