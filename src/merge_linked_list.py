class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

def linkedlist_to_list(list1, list2):
    q = []
    if not list1 and not list2:
        return None
    elif not list1 and list2:
        return list2
    else:
        return list1
    node1 = list1
    node2 = list2
    while node1 is not None:
        q.append(node1.val)
        node1 = node1.next
    while node2 is not None:
        q.append(node2.val)
        node2 = node2.next
    return q


def merge_two_linkedlist(list1, list2) -> Node:
    if (not list1) or (list2 and list1.val > list2.val):
        #   if list1's value is bigger, than swap it so the smaller value of list2 goes into list1
        list1, list2 = list2, list1
    if list1:
        #   swapping the node eventually connects them
        list1.next =merge_two_linkedlist(list1.next, list2)
        #   list1 is simply poiting to the beginning of the given list1, and
        #   now list1 is mutated and it is still a list1
        #   so returned list1 is the merged one with list2

        #   list2 is still pointing to 1, 3, 4 but list1 is connected to those
    return list1

if '__main__' == __name__:
    list1 = LinkedList()
    list1.head = Node('1')
    e2 = Node("2")
    e3 = Node("4")
    #e4 = Node("2")
    #e5 = Node("1")
    list1.head.next = e2
    e2.next = e3
    #e3.next = e4
    #e4.next = e5

    list2 = LinkedList()
    list2.head = Node('1')
    e22 = Node("3")
    e33 = Node("4")
    #e44 = Node("2")
    #e55 = Node("1")
    list2.head.next = e22
    e22.next = e33
    #e33.next = e44
    #e44.next = e55

    a = merge_two_linkedlist(list1.head, list2.head)
    while a is not None:
        print(a.val)
        a = a.next