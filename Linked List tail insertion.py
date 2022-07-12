
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def print_List(Head):
    ptr = Head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next

    print('None')



def appendNode(Head, key):
    current = Head
    node = Node(key)


    if current is None:
        Head = node

    else:

        while current.next:
            current = current.next
        current.next = node

    return Head


if __name__ == '__main__':


    keys = [1, 2, 3, 4]


    Head = None
    for key in keys:
        Head = appendNode(Head, key)


    print_List(Head)






















