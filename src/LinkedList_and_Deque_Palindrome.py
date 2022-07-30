#   return if the given linked list is a palindrome
import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
def convert_linkedlist_to_list(head) -> bool:
    q = []
    if not head:
        return True
    node = head
    #   just loop through until every element of the given linkedlist is stored in a list
    while node is not None:
        q.append(node.val)
        node = node.next
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True

def convert_deque_to_list(head) -> bool:
    #   apparently, using deque runs at O(1) when popping and using a list runs at O(n)
    q = collections.deque()
    #   if head == None
    if not head:
        return True
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    while len(q)> 1:
        if q.popleft() != q.pop():
            return False
    return True


if '__main__' == __name__:
    list = LinkedList()
    list.head = Node('a')
    e2 = Node("b")
    e3 = Node("a23")
    list.head.next = e2
    e2.next = e3

    print(convert_linkedlist_to_list(list.head))
    print(convert_deque_to_list(list.head))
