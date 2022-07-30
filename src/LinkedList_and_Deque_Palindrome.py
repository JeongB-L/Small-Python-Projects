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

def luxury_runner_solution(head) -> bool:
    rev = None
    #   both slow and fast runners start at the same point
    slow = head
    fast = head
    #   while fast and fast.next are not None(null)
    while fast and fast.next:
        #   fast runner moves by 2 nodes
        #   fast runner exists as a flag that
        #   make sures that the slow runner(essential one) reaches the middle of the linkedlist
        fast = fast.next.next
        #   rev is now slow
        #   previous rev is moved to rev,next
        rev, rev.next, slow = slow, rev, slow.next
    #   if fast is not None; if the length of the given linkedlist is not an even number
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        #   as both traverse, if the given is a palindrome,
        #   there should be nothing left in each of them
        slow = slow.next
        rev = rev.next
    return not rev

#   Note: Runner is a method of using 2 pointers while traversing the linkedlist. A pointer exceeds
#   the other one, allowing the other one to be used for determining some needed values.
#   if the fast one goes by 2 and slow one goes by 1,
#   when fast reaches the end, the slow one reaches the middle point of it


if '__main__' == __name__:
    list = LinkedList()
    list.head = Node('1')
    e2 = Node("2")
    e3 = Node("3")
    e4 = Node("2")
    e5 = Node("1")
    list.head.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    print(convert_linkedlist_to_list(list.head))
    print(convert_deque_to_list(list.head))
    print(luxury_runner_solution(list.head))
